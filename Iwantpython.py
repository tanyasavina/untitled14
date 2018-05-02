
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='524090412:AAHC6mjNhViDYgjgd1fmeg1TGo_B_QYL0gE')
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hi there')
def textMessage(bot, update):
    response = 'Got your message' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)

start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()