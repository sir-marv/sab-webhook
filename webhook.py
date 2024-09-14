import sys
import requests
import json


def send_notification(notification_type, notification_title, notification_text):
    webhook_url = "WEBHOOK"
    payload = {
        "text": "[" + notification_type + "] " + notification_title + " - " + notification_text,
        "format": "plain",
        "displayName": "SABnzbd",
        "avatar_url": "https://raw.githubusercontent.com/sabnzbd/sabnzbd.github.io/master/images/icons/android-192x192.png"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Request to webhook returned an error {
                         response.status_code}, the response is:\n{response.text}")


if __name__ == "__main__":
    try:
        scriptname, notification_type, notification_title, notification_text = sys.argv
    except ValueError:
        print("No commandline parameters found")
        # sys.exit(1)

    send_notification(notification_type, notification_title, notification_text)
    sys.exit(0)
