from telegram.ext import CallbackContext
from utils.clash_api import get_clan_members

def check_war_league(update, context: CallbackContext):
    # Добавьте логику для проверки участия в лиге войны кланов
    update.message.reply_text("Логика проверки участия в лиге войны кланов пока не реализована.")

