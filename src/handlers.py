from telegram import Update
from telegram.ext import ContextTypes

from .custom_request import send_file
from .misc import get_file_path


async def start_cmd_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        update.effective_chat.id, "Hello! Let's transcribe something!"
    )


async def voice_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice = await update.message.voice.get_file()
    user_id = update.effective_user.id
    response = send_file(
        user_id,
        await voice.download_to_drive(get_file_path(user_id))
    )
    await context.bot.send_message(
        update.effective_chat.id, response
    )


async def audio_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.audio.get_file()
    user_id = update.effective_user.id
    response = send_file(
        user_id,
        await file.download_to_drive(get_file_path(user_id))
    )
    await context.bot.send_message(
        update.effective_chat.id, response
    )


async def unknown_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        update.effective_chat.id, "Sorry, I don't know this command. Try /start or /help"
    )
