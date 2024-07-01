from telegram import Update
from telegram.ext import ContextTypes


async def start_cmd_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        update.effective_chat.id, "Hello! Let's transcribe something!"
    )