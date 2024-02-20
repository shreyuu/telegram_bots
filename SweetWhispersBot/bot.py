import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import creds
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

bot = telegram.Bot(token=creds.TELEGRAM_API_TOKEN)

# Define the command handler for the /quote command
def quote(update: telegram.Update, context: CallbackContext):
    try:
        category = 'love'
        api_url = 'https://api.api-ninjas.com/v1/quotes?category=love'
        response = requests.get(api_url, headers={'X-Api-Key':  creds.NINJA_API_KEY})
        if response.status_code == requests.codes.ok:
            quote_data = response.json()[0]
            quote_text = quote_data.get("quote", "No quote available")

            # Send the quote to the user
            update.message.reply_text(quote_text)
        else:
            update.message.reply_text("Sorry, I couldn't fetch a quote at the moment. Try again later.")

    except Exception as e:
        update.message.reply_text("Try again later.")

def main():
    # Create an Updater for the bot
    updater = Updater(token=creds.TELEGRAM_API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add a command handler for the /quote command
    dispatcher.add_handler(CommandHandler("quote", quote))
    print("heyy")
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
