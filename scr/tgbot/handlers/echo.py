from aiogram import types, Dispatcher
from tgbot.keyboards.reply import main_keyboard, group_keyboard


async def echo(message: types.Message):
    if message.chat.type == "group" or message.chat.type == "supergroup":
        keyboard = group_keyboard()
    else:
        keyboard = main_keyboard()
    if not message.text:
        await message.answer(
            "Я лучше понимаю, если мне пишут текстом😉"
        )
        return
    await message.answer(
        "Я Вас не понимаю, лучше выберите ответ с клавиатуры😉",
        reply_markup=keyboard
    )


def register_echo(dp: Dispatcher):
    dp.register_message_handler(
        echo,
        state="*",
        content_types="any"
    )
