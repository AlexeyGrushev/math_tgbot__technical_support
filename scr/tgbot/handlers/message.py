from aiogram import types, dispatcher

from aiogram.dispatcher.filters import Text
from tgbot.database.db_sqlite import DataBaseHelper
from tgbot.misc.help_data import FAQ_INFO, default_page
from tgbot.keyboards.inline import help_pages_keyboard, profile_keyboard


async def profile(message: types.Message):
    db = DataBaseHelper()
    # keyboard = profile_keyboard()
    reg_date = db.user_get_register_date(str(message.from_user.id))[0][0]
    await message.answer(
        "<b>Профиль</b>\n\n" + \
        f"{message.from_user.first_name} {message.from_user.last_name}\n" + \
        f"@{message.from_user.username}\n\n" + \
        f"Вы с нами с <u>{reg_date[0:10]}</u>\n\n"
    )

async def faq(message: types.Message):
    keyboard = help_pages_keyboard()
    default_page()
    await message.answer(
        f"{FAQ_INFO[0]}",
        reply_markup=keyboard
    )

def register_message(dp: dispatcher.Dispatcher):
    dp.register_message_handler(
        profile,
        Text("Профиль👤"),
        state = "*"
    )
    dp.register_message_handler(
        faq,
        Text("FAQ🛟"),
        state = "*"
    )
