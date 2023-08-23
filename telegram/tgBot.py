# Importing libraries
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import requests
import json
import random
import os
from dotenv import load_dotenv

# Importing local files
from helperFunctions import *
from constants import *

BOT_USERNAME = '@ShrekEnjoyers_bot'

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

with open('quotes.json', encoding='utf-8') as f:
    data = json.load(f)



# Clement's SHIT
# send_message_telegram("penis hehe, deez nuts", CLEM_USER_ID)
# send_message_telegram("penis hehe, deez nuts", DARR_USER_ID)
# send_message_telegram("penis hehe, deez nuts", DENZ_USER_ID)



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello waddup B-)")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Don't know what I do?")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Custom command!")


async def compliment_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://complimentr.com/api")
    if response.status_code == 200:
        compliment = response.json()['compliment']
        await update.message.reply_text(compliment)

    else:
        await update.message.reply_text("Sorry can't think of any right now :)")


async def insult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    if response.status_code == 200:
        insult = response.json()['insult']
        await update.message.reply_text(insult)

    else:
        await update.message.reply_text("Sorry can't think of any right now :)")


async def uselessFacts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    if response.status_code == 200:
        uselessFacts = response.json()['text']
        await update.message.reply_text(uselessFacts)

    else:
        await update.message.reply_text("Sorry can't think of any right now :)")


async def motivation_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    x = random.randint(0, len(data))
    motivation = data[x]['quoteText']
    await update.message.reply_text(motivation)


def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return "Hey there"

    if 'how are you' in processed:
        return 'I am good'

    return "i don't understand"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)

        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    # app.add_handler(CommandHandler('start', start_command))
    # app.add_handler(CommandHandler('help', help_command))    # app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('compliment', compliment_command))
    app.add_handler(CommandHandler('insult', insult_command))
    app.add_handler(CommandHandler('facts', uselessFacts_command))
    app.add_handler(CommandHandler('motivate', motivation_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
    
