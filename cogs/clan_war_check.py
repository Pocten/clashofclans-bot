from telegram import Update
from telegram.ext import CallbackContext

async def check_clan_war(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Логика проверки участия в обычных войнах кланов пока не реализована.")
