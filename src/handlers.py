from telegram import Update
from telegram.ext import ContextTypes


async def start_cmd_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        update.effective_chat.id, "Hello! Let's transcribe something!"
    )


async def voice_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        update.effective_chat.id, "Voice message recieved"
    )
    voice = await update.message.voice.get_file()
    buf = await voice.download_as_bytearray()
    with open("voice", "wb") as f:
        f.write(buf)


async def audio_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        update.effective_chat.id, "File recieved"
    )
    file = await update.message.audio.get_file()
    buf = await file.download_as_bytearray()
    with open("file", "wb") as f:
        f.write(buf)


async def unknown_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        update.effective_chat.id, "Sorry, I don't know this command. Try /start or /help"
    )
