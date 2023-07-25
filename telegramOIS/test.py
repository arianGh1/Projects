from telegram import Bot
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello, I am your Telegram bot!')

def main():
    updater = Updater(token='6626586321:AAEnTg08uDV5oUTtGaXYJL0rLBe9rNx5nZ8', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
