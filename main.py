import os
import random
import requests
import time
import json

def clear_messages(channel_id, before, token):
    base_url = f"https://discord.com/api/channels/{channel_id}/messages"
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    min = 0.582276123
    max = 0.872718292

    clock = 0
    interval = random.uniform(min, max)
    
    while True:
        response = requests.get(f"{base_url}?before={before}&limit=100", headers=headers)
        messages = response.json()
        if not messages:
            break

        for message in messages:
            before = message['id']
            time.sleep(interval)
            response = requests.delete(f"{base_url}/{before}", headers=headers)
            if response.status_code == 204:
                print(f"[+] Message supprimé : {before}")

if __name__ == "__main__":
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    token = config["token"]
    channel_id = config["channel_id"]
    last_message_id = config["last_message_id"]
    
    clear_messages(channel_id, last_message_id, token)
