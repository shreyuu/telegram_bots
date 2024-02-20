import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# Replace with your Telegram bot token
bot_token = "6618326634:AAHBWenyLShJUYLEaWxi3u3jBYqHz4EDri0"

# Initialize the Telegram bot
bot = telegram.Bot(token=bot_token)

# Define the command handler for the /quote command
def quote(update: telegram.Update, context: CallbackContext):
    try:
        category = 'love'
        api_url = 'https://api.api-ninjas.com/v1/quotes?category=love'
        response = requests.get(api_url, headers={'X-Api-Key': 'zySNTDohuRqGSxslulcRGg==MCoHoPEVDWUeYTeo'})  # Replace 'YOUR_API_KEY' with your actual API key
        if response.status_code == requests.codes.ok:
            quote_data = response.json()
            quote_text = quote_data.get("quote", "No quote available")

            # Send the quote to the user
            update.message.reply_text(quote_text)
        else:
            update.message.reply_text("Sorry, I couldn't fetch a quote at the moment. Try again later.")

    except Exception as e:
        update.message.reply_text("Try again later.")

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
