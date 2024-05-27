from telegram import Update
from telegram.ext import CallbackContext
from utils.clash_api import get_clan_members

print("Импорт функции check_inactive_members выполнен")

async def check_inactive_members(update: Update, context: CallbackContext) -> None:
    print("Функция check_inactive_members вызвана")
    members = get_clan_members()
    print("Полученные данные от API:", members)
    member_info = []
    for member in members['items']:
        info = f"Имя: {member['name']}, Уровень TH: {member['townHallLevel']}, Опыт: {member['expLevel']}, Пожертвования: {member['donations']}"
        member_info.append(info)
    await update.message.reply_text(f"Информация об участниках:\n" + "\n".join(member_info))
