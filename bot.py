import logging
from telegram.ext import Updater, CommandHandler
from config import TELEGRAM_TOKEN

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    """Отправляет сообщение при вызове команды /start."""
    update.message.reply_text('Привет! Я бот для управления кланом Гномы.')

def main():
    """Запуск бота."""
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dp = updater.dispatcher

    # Команды бота
    dp.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
