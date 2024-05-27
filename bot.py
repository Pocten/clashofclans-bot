import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from config import TELEGRAM_TOKEN
from cogs.activity_check import check_inactive_members
from cogs.donation_check import check_donations
from cogs.clan_games_check import check_clan_games
from cogs.war_league_check import check_war_league
from cogs.clan_war_check import check_clan_war

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext) -> None:
    """Отправляет сообщение при вызове команды /start."""
    await update.message.reply_text('Привет! Я бот EliteGnomeBot для управления кланом Гномы.')

async def help_command(update: Update, context: CallbackContext) -> None:
    """Отправляет сообщение при вызове команды /help."""
    await update.message.reply_text('Команды:\n/check_inactive - Проверить неактивных участников\n/check_donations - Проверить пожертвования\n/check_clan_games - Проверить участие в клановых играх\n/check_war_league - Проверить участие в лиге войны кланов\n/check_clan_war - Проверить участие в обычных войнах кланов')

def main() -> None:
    """Запуск бота."""
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Команды бота
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("check_inactive", check_inactive_members))
    application.add_handler(CommandHandler("check_donations", check_donations))
    application.add_handler(CommandHandler("check_clan_games", check_clan_games))
    application.add_handler(CommandHandler("check_war_league", check_war_league))
    application.add_handler(CommandHandler("check_clan_war", check_clan_war))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
