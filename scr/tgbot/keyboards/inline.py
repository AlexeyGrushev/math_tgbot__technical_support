from aiogram import types


def help_pages_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
            types.InlineKeyboardButton(text="<<<", callback_data="back"),
            types.InlineKeyboardButton(text=">>>", callback_data="forward")
    )

    return keyboard

def profile_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(text="Активные обращения", callback_data="active_tickets")
    )
    keyboard.row(
        types.InlineKeyboardButton(text="История обращений", callback_data="history_tickets")
    )
    
    return keyboard
