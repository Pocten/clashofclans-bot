# Используйте базовый образ Python
FROM python:3.10-slim

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы requirements.txt в рабочую директорию
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте весь код проекта в рабочую директорию
COPY . .

# Укажите команду для запуска приложения
CMD ["python", "bot.py"]
