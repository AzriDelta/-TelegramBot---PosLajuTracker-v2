import telegram
from dbhelper import DBHelper
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from telegram import ForceReply
import logging

#Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)



#for logging error error
def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

text_intro = "Hello and welcome to Pos Laju tracking bot. Below are the commands for your usage.\n 1. /add\n 2. /track\n 3. /delete"

#send a message when the command /intro is issued
def intro(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=text_intro)

#send a message when the command /start is issued
def start(bot, update):
    update.message.reply_text('Hi!')

#receive a message when the command /add is issued
def add(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Send me a tracking number")
    #for user reply
    tracking_number = update.message.text #get user reply
    bot.send_message(chat_id=update.message.chat_id, text=tracking_number)


#main
#start bot
def main():
    ## Create the EventHandler and pass it your bot's token.
    updater = Updater(token='471824003:AAH2AsNzhTtciPYtG6PL_NWxxyYzxCwL09A')

    ## Get the dispatcher to register handlers
    dp = updater.dispatcher

    #start_handler = CommandHandler('start', start)
    #dispatcher.add_handler(start_handler)
    #shortform way would be below

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('add', add))

    # on noncommand i.e message - put intro
    dp.add_handler(MessageHandler(Filters.text, intro))

    # log all errors
    dp.add_error_handler(error)

    #start the bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()