from telegram import Update
from telegram.ext import CallbackContext
from utils.clash_api import get_clan_members

async def check_clan_games(update: Update, context: CallbackContext) -> None:
    members = get_clan_members()
    underperforming_members = []
    for member in members['items']:
        if member['clanGamesPoints'] < 1000:
            underperforming_members.append(member['name'])
    await update.message.reply_text(f"Члены, которые набрали менее 1000 очков в играх кланов: {', '.join(underperforming_members)}")
