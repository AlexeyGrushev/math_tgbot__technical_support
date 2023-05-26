from aiogram import types


def main_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True, input_field_placeholder="Главное меню"
    )
    keyboard.add(
        types.KeyboardButton(text="Профиль👤"),
        types.KeyboardButton(text="FAQ🛟")
    )
    keyboard.row(
        types.KeyboardButton(text="Обратиться в поддержку📨")
    )

    return keyboard

def theme_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True, input_field_placeholder="Обращение в поддержку"
    )
    keyboard.add(
        types.KeyboardButton(text="Уравнения🟰"),
        types.KeyboardButton(text="Графики📈"),
        types.KeyboardButton(text="Обучение🎓"),
        types.KeyboardButton(text="Статистика📊")
    )
    keyboard.row(
        types.KeyboardButton(text="Отменить🛑")
        )
    return keyboard

def cancel_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True, input_field_placeholder="Обращение в поддержку"
    )
    keyboard.add(
        types.KeyboardButton(text="Отменить🛑")
    )

    return keyboard

def confirm_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        input_field_placeholder="Обращение в поддержку",
        row_width=1
    )
    keyboard.add(
        types.KeyboardButton(text="Отправить✅"),
    )
    keyboard.row(
        types.KeyboardButton(text="Отменить🛑")
    )

    return keyboard

def group_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        input_field_placeholder="Решение вопросов пользователей"
    )
    keyboard.add(
        types.KeyboardButton(text="Показать активные🔃")
    )
    return keyboard
