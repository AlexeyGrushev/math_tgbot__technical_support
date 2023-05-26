from aiogram import types, Dispatcher

from settings.const import SUPPORT_CHAT
from aiogram.dispatcher.filters import Text
from tgbot.database.db_sqlite import DataBaseHelper

async def answer_to_user(message: types.Message):
    if message.chat.type != "group" or message.chat.type != "supergroup" and \
        str(message.chat.id) != SUPPORT_CHAT:
        await message.answer("Несоответствующий чат")
    db = DataBaseHelper()
    try:
        if message.reply_to_message:
            answer_data = [
                message.text,
                message.reply_to_message.text.split("\n")[0]
                ]
            await message.bot.send_message(
                int(message.reply_to_message.text.split("\n")[1]),
                f"🔔<b>Ответ от технической поддержки:</b>\n\n{message.text}"
            )
            db.answer_to_ticket(answer_data)
            await message.answer(
                "Обращение обработано успешно"
            )
        else:
            await message.answer("Для ответа пользователю выберите ответ на сообщение")
    except Exception:
        await message.answer(
            "Не является обращением"
        )



async def show_actual(message: types.Message):
    await message.answer("<u>Актуальные обращения:</u>")
    db = DataBaseHelper()
    data = db.show_active_ticket()
    if data == []:
        await message.answer(
            "На данный момент обращений нет"
        )
    for i in data:
        await message.answer(
            f"{i[0]}\n" + \
            f"{i[1]}\n" + \
            "Идентификаторы обращения\n" + \
            f"{i[2]}"
                )

def register_support_handlers(dp: Dispatcher):
    dp.register_message_handler(
        show_actual,
        Text("Показать активные🔃")
    )
    dp.register_message_handler(
        answer_to_user,
        state="*",
        chat_type=types.ChatType.GROUP
    )
