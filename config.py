import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env файла

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
COC_API_TOKEN = os.getenv('COC_API_TOKEN')
CLAN_TAG = '#28GCQ0LU8'
