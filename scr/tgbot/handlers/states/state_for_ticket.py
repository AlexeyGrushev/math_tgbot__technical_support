from aiogram import types, dispatcher
from aiogram.dispatcher.filters import Text

from tgbot.database.db_sqlite import DataBaseHelper
from settings.const import SUPPORT_CHAT
from tgbot.misc.ticket_format import format
from tgbot.misc.bad_words_filter import has_bad_words
from tgbot.misc.states.ticket_state import TicketForm
from tgbot.keyboards.reply import(
    cancel_keyboard,
    confirm_keyboard,
    theme_keyboard,
    main_keyboard
)

async def confirm_handler(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        try:
            keyboard = main_keyboard()
            db = DataBaseHelper()
            if has_bad_words(format(data)):
                await message.answer(
                    "Ваше обращение содержит нецензурную лексику. Создайте новое обращение исключив эти слова"
                )
                return
            data_to_save = []
            data_to_save.append(message.from_user.id)
            data_to_save.append(format(data))

            db.save_active_ticket(data_to_save)
            
            try:
                get_id = db.user_last_ticket()[0][0]
            except IndexError:
                get_id = 1
            
            await message.bot.send_message(
                int(SUPPORT_CHAT),
                f"{get_id}\n" + \
                f"{message.from_user.id}\n" + \
                "Идентификаторы обращения\n" + \
                f"{format(data)}"
            )

            await message.answer(
                f"Обращение в поддержку под номером {get_id} успешно отправлено.\nОжидайте ответа",
                reply_markup=keyboard
            )
            
        except Exception:
            await message.bot.delete_message(
                chat_id=message.chat.id,
                message_id=message.message_id
            )
        finally:
            await state.finish()

async def cancel_handler(message: types.Message, state: dispatcher.FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

    await state.finish()

    keyboard = main_keyboard()

    await message.answer(
        "Обращение в поддержку отменено, возвращение в главное меню",
        reply_markup=keyboard
    )

async def start_new_form(
        message: types.Message, state: dispatcher.FSMContext
        ) -> None:
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    
    keyboard = theme_keyboard()
    await message.answer(
        "<b>Обращение в поддержку</b>\n\n" + \
        "Возможно Вы сможете найти ответ на свой вопрос в разделе FAQ"
    )
    await message.answer(
        "Для начала обозначьте тему обращения\n" + \
        "Вы можете выбрать вариант с клавиатуры или указать свою тему, написав её текстом",
        reply_markup=keyboard
    )
    await TicketForm.first()

async def save_ticket_theme(
        message: types.Message, state: dispatcher.FSMContext
        ) -> None:
    if not message.text:
        await message.bot.send_message(
            message.from_user.id,
            "Я лучше понимаю, если мне пишут текстом😉"
        )
        return
    
    async with state.proxy() as data:
        data["theme"] = message.text
    await TicketForm.next()
    
    keyboard = cancel_keyboard()
    await message.answer(
        "Напишите кратко суть обращения",
        reply_markup=keyboard
    )

async def save_ticket_discription(
        message: types.Message, state: dispatcher.FSMContext
        ) -> None:
    if not message.text:
        await message.bot.send_message(
            message.from_user.id,
            "Я лучше понимаю, если мне пишут текстом😉"
        )
        return
    
    async with state.proxy() as data:
        data["discription"] = message.text
    await TicketForm.next()

    await message.answer(
        "Опишите Вашу проблему детально, изложив все мелочи"
    )

async def save_ticket_appeal(
        message: types.Message, state: dispatcher.FSMContext
        ) -> None:
    if not message.text:
        await message.bot.send_message(
            message.from_user.id,
            "Я лучше понимаю, если мне пишут текстом😉"
        )
        return
    async with state.proxy() as data:
        keyboard = confirm_keyboard()
        try:
            if data["appeal"] is not None:
                await message.answer(
                    "Будет лучше, если Вы укажите ответ с клавиатуры",
                    reply_markup=keyboard
                )
                return
        except Exception:
            data["appeal"] = message.text
            data["user"] = message.from_user.username

    await message.answer(
        text=format(data),
        reply_markup=keyboard
    )


def register_ticket_form(dp: dispatcher.Dispatcher):
    dp.register_message_handler(
        confirm_handler,
        Text("Отправить✅"),
        state="*"
    )
    dp.register_message_handler(
        cancel_handler,
        Text("Отменить🛑"),
        state="*"
    )
    dp.register_message_handler(
        start_new_form,
        Text("Обратиться в поддержку📨"),
        state="*"
    )
    dp.register_message_handler(
        save_ticket_theme,
        state=TicketForm.theme,
        content_types="any"
    )
    dp.register_message_handler(
        save_ticket_discription,
        state=TicketForm.discription,
        content_types="any"
    )
    dp.register_message_handler(
        save_ticket_appeal,
        state=TicketForm.appeal,
        content_types="any"
    )
