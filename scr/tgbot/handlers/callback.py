from aiogram import types, dispatcher

from tgbot.keyboards.inline import help_pages_keyboard, profile_keyboard
from tgbot.misc.help_data import FAQ_INFO, addiction_page, return_page, subtraction_page


async def page_back(callback: types.CallbackQuery):
    keyboard = help_pages_keyboard()

    if return_page() <= 0:
        return

    else:
        subtraction_page()
        info = str(FAQ_INFO[return_page()])
        await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
        await callback.message.answer(
            text=info,
            reply_markup=keyboard,
        )


async def page_forward(callback: types.CallbackQuery):
    keyboard = help_pages_keyboard()

    if return_page() >= len(FAQ_INFO) - 1:
        return

    else:
        addiction_page()
        info = str(FAQ_INFO[return_page()])
        await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
        await callback.message.answer(
            text=info,
            reply_markup=keyboard
        )

async def active_ticket(callback: types.CallbackQuery):
    keyboard = profile_keyboard()
    await callback.bot.send_message(chat_id=callback.chat.id, text="Привет!", reply_markup=keyboard, from_user=callback.user_id)

def register_all_callback(dp: dispatcher.Dispatcher):
    dp.register_callback_query_handler(
        page_back,
        lambda callback: "back" in callback.data,
        state="*"
    )
    dp.register_callback_query_handler(
        page_forward,
        lambda callback: "forward" in callback.data,
        state="*"
    )
    dp.register_callback_query_handler(
        active_ticket,
        lambda callback: "active_tickets" in callback.data,
        state="*"
    )