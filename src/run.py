import logging
from telegram.ext import ApplicationBuilder, CommandHandler
import sys

import telegram.ext

from .handlers import start_cmd_handler


def get_token() -> str:
    with open("./src/token.txt") as token_file:
        return token_file.readline()


def start():
    app = ApplicationBuilder().token(get_token()).build()

    app.add_handler(
        CommandHandler('start', start_cmd_handler)
    )

    # requests logging
    logging.basicConfig(filename='log/api.log', level=logging.DEBUG,
                        format=' %(asctime)s - %(levelname)s - %(message)s')
    # bot logging
    sys.stdout = open('./log/bot_main.log', 'w')
    sys.stderr = open('./log/bot_error.log', 'w')
    if '--debug' in sys.argv:
        telegram.logger.setLevel('DEBUG')

    app.run_polling()