import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler
import requests

# Replace with your Telegram bot token
bot_token = "6618326634:AAHBWenyLShJUYLEaWxi3u3jBYqHz4EDri0"

# Initialize the Telegram bot
bot = telegram.Bot(token=bot_token)

# Define the command handler for the /quote command
def quote(update, context):
    try:
        # Fetch a random romantic quote from the quotes.rest API
        response = requests.get("https://quotes.rest/qod?category=love")
        data = response.json()
        quote_text = data["contents"]["quotes"][0]["quote"]

        # Send the quote to the user
        update.message.reply_text(quote_text)

    except Exception as e:
        update.message.reply_text("Sorry, I couldn't fetch a quote at the moment. Try again later.")

def main():
    # Create an Updater for the bot
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Add a command handler for the /quote command
    dispatcher.add_handler(CommandHandler("quote", quote))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
