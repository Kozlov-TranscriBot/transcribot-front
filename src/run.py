import sys
import logging

import telegram
from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)

from .handlers import (
    start_cmd_handler, 
    voice_message_handler, 
    audio_message_handler,
    lang_selected,
    unknown_message_handler
)


def get_token() -> str:
    with open("./token.txt") as token_file:
        return token_file.readline()


def start():
    app = ApplicationBuilder()\
        .arbitrary_callback_data(True)\
        .token(get_token()).build()

    app.add_handlers([
        CommandHandler('start', start_cmd_handler),
        CommandHandler('help', start_cmd_handler),
        MessageHandler(filters.VOICE, voice_message_handler),
        MessageHandler(filters.AUDIO, audio_message_handler),
        MessageHandler(filters.COMMAND, unknown_message_handler),
        MessageHandler(filters.TEXT, unknown_message_handler),
        CallbackQueryHandler(lang_selected) # TODO: Добавить защиту от устаревших запросов
    ])

    # requests logging
    logging.basicConfig(filename='log/api.log', level=logging.DEBUG,
                        format=' %(asctime)s - %(levelname)s - %(message)s')
    # bot logging
    sys.stdout = open('./log/bot_main.log', 'w')
    sys.stderr = open('./log/bot_error.log', 'w')
    if '--debug' in sys.argv:
        telegram.logger.setLevel('DEBUG')

    app.run_polling()