from aiogram.dispatcher.filters.state import State, StatesGroup


class TicketForm(StatesGroup):
    theme = State()
    discription = State()
    appeal = State()
