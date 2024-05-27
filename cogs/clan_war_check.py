from telegram.ext import CallbackContext
from utils.clash_api import get_clan_members

def check_clan_war(update, context: CallbackContext):
    # Добавьте логику для проверки участия в обычных войнах кланов
    update.message.reply_text("Логика проверки участия в обычных войнах кланов пока не реализована.")
