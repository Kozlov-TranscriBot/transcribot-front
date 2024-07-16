from telegram import Update
from telegram.ext import ContextTypes

from .custom_request import send_bytearray


async def start_cmd_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        update.effective_chat.id, "Hello! Let's transcribe something!"
    )


async def voice_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice = await update.message.voice.get_file()
    response = send_bytearray(
        update.effective_user.id, 
        await voice.download_as_bytearray()
    )
    await context.bot.send_message(
        update.effective_chat.id, response
    )


async def audio_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.audio.get_file()
    response = send_bytearray(
        update.effective_user.id, 
        await file.download_as_bytearray()
    )
    await context.bot.send_message(
        update.effective_chat.id, response
    )


async def unknown_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        update.effective_chat.id, "Sorry, I don't know this command. Try /start or /help"
    )
