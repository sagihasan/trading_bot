import os
import requests
from dotenv import load_dotenv

load_dotenv()

public_webhook = os.getenv("DISCORD_PUBLIC_WEBHOOK")
private_webhook = os.getenv("DISCORD_PRIVATE_WEBHOOK")


def send_discord_message(webhook_url, message):
    data = {'content': message}
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print(f"ההודעה נשלחה בהצלחה ל־Webhook: {webhook_url}")
    else:
        print(
            f"שגיאה בשליחה ל־Webhook: {webhook_url} - קוד {response.status_code}"
        )


send_discord_message(public_webhook, "בדיקת איתות ידנית מהבוט")

print("בדיקת Webhook ציבורי...")
send_discord_message(public_webhook, "זהו רק טסט ציבורי.")

print("בדיקת Webhook פרטי...")
send_discord_message(private_webhook, "זהו רק טסט פרטי.")
