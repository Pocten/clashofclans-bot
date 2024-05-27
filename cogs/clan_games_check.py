from telegram.ext import CallbackContext
from utils.clash_api import get_clan_members

def check_clan_games(update, context: CallbackContext):
    members = get_clan_members()
    underperforming_members = []
    for member in members['items']:
        if member['clanGamesPoints'] < 1000:
            underperforming_members.append(member['name'])
    update.message.reply_text(f"Члены, которые набрали менее 1000 очков в играх кланов: {', '.join(underperforming_members)}")
