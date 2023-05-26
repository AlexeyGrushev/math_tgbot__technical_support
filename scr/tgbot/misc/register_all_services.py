from aiogram import Dispatcher

from tgbot.misc.set_bot_commands import set_default_commands
from tgbot.handlers.user import register_user
from tgbot.handlers.support import register_support_handlers
from tgbot.handlers.states.state_for_ticket import register_ticket_form
from tgbot.handlers.message import register_message
from tgbot.handlers.echo import register_echo
from tgbot.handlers.callback import register_all_callback


def register_all_handlers(dp: Dispatcher):
    register_user(dp)
    register_ticket_form(dp)
    register_message(dp)
    register_support_handlers(dp)
    register_echo(dp)

def register_all_callbacks(dp: Dispatcher):
    register_all_callback(dp)

async def register_all_services(dp: Dispatcher):
    register_all_handlers(dp)
    register_all_callbacks(dp)
    await set_default_commands(dp)
