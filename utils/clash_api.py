import requests
from config import COC_API_TOKEN, CLAN_TAG

def get_clan_members():
    url = f'https://api.clashofclans.com/v1/clans/{CLAN_TAG.replace("#", "%23")}/members'
    headers = {'Authorization': f'Bearer {COC_API_TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_player_info(player_tag):
    url = f'https://api.clashofclans.com/v1/players/{player_tag.replace("#", "%23")}'
    headers = {'Authorization': f'Bearer {COC_API_TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json()
