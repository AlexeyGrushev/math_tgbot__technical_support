from aiogram import types, Dispatcher

from tgbot.database.db_sqlite import DataBaseHelper
from tgbot.keyboards.reply import main_keyboard, group_keyboard
from aiogram.dispatcher import FSMContext
from settings.const import SUPPORT_CHAT


async def start_message(message: types.Message, state: FSMContext):
    await state.finish()
    if message.chat.type == "group" or message.chat.type == "supergroup":
        if str(message.chat.id) != SUPPORT_CHAT:
            await message.answer(
                "Невалидная группа❌.\nЕсли Вы считаете, что это не так, обратитесь к администратору.\n" + \
                f"ID этого чата: <b>{message.chat.id}</b>"
            )
            return
        keyboard = group_keyboard()
        await message.answer(
            "Валидация прошла успешно✅.\nПоступающие сообщения будут отображаться в этом чате",
            reply_markup=keyboard
        )
        return
    db = DataBaseHelper()
    data = [
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name,
        message.from_user.last_name
    ]
    db.register_user_in_db(data)
    keyboard = main_keyboard()
    await message.answer(
                f"<b>Здравствуйте, {message.from_user.first_name}</b>\n\n" + \
                "Я бот технической поддержки приложения Math\n\n" + \
                "<u>Выберите нужное действие с клавиатуры</u>",
                reply_markup=keyboard
        )

def register_user(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=["start"], state="*")
