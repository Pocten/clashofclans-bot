from telegram.ext import CallbackContext
from utils.clash_api import get_clan_members

def check_donations(update, context: CallbackContext):
    members = get_clan_members()
    eligible_for_promotion = []
    for member in members['items']:
        if member['donations'] >= 700:
            eligible_for_promotion.append(member['name'])
    update.message.reply_text(f"Члены, которые могут быть повышены до Старейшины: {', '.join(eligible_for_promotion)}")
