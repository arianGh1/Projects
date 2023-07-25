from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    update.message.reply_text(f'Hi {user.first_name}, the current time is {current_time}!')

def main() -> None:
    """Start the bot."""
    bot = Bot(token='6626586321:AAEnTg08uDV5oUTtGaXYJL0rLBe9rNx5nZ8')
    updater = Updater(bot=bot, update_queue = updater.update_queue)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
