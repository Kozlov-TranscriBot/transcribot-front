from typing import cast
from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    File
)
from telegram.ext import (
    ContextTypes
)

from .custom_request import AudioData


async def start_cmd_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        update.effective_chat.id, "Hello! Let's transcribe something!\nYou can send me a file or a voice message up to 20 MB"
    )

def get_langs_keyboard(file: File) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup.from_column(
        [InlineKeyboardButton(code, callback_data=AudioData(code, file)) for code in ["ru", "en"]]
    ) # TODO: Есть шанс, что callback_data создаёт брешь в безопасности из-за прямой передачи туда типа и путя, надо это проверить

async def voice_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice = await update.message.voice.get_file()
    keyboard = get_langs_keyboard(voice)
    await update.message.reply_text("Choose the language", reply_markup=keyboard)

async def audio_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.audio.get_file()
    keyboard = get_langs_keyboard(file)
    await update.message.reply_text("Choose the language", reply_markup=keyboard)

async def lang_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Processing audio...")
    data = cast(AudioData, query.data)
    user_id = update.effective_user.id

    response = await data.send(user_id)
    await query.delete_message()
    await context.bot.send_message(
        update.effective_chat.id, response
    )

async def unknown_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        update.effective_chat.id, "Sorry, I don't know this command. Try /start or /help"
    )
