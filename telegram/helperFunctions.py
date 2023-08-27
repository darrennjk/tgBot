# Importing libraries
import requests
import os
from dotenv import load_dotenv

# Importing local files
from constants import *


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


def send_message_telegram(message: str, id: str):
    """This function is used to send a message to a Telegram chat/channel.
    
    Payload Params:
        chat_id (str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        text (str): Text of the message to be sent
        parse_mode (str): Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message
        disable_web_page_preview (bool): Disables link previews for links in this message
        disable_notification (bool): Sends the message silently. Users will receive a notification with no sound.
        reply_to_message_id (int): If the message is a reply, ID of the original message

    Args:
        message (str): the message text
        id (str): the chat ID or channel ID
    """
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": id,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": False,
        "disable_notification": False,
        "reply_to_message_id": 0
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    # For debugging purposes
    # print(response.text)
    
    
# Clement's SHIT
# send_message_telegram("i love nuts even more", DSAI_GROUP_ID)