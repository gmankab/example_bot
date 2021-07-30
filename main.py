from callback import *
from commands import *
from message_reply import *
from aiogram import executor


fuck_pycharm_import_warnings_callback()
fuck_pycharm_import_warning_commands()


if __name__ == '__main__':
    while True:
        executor.start_polling(dp)
        # loop = asyncio.get_event_loop()
