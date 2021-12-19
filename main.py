import os
import Responses as R

from telegram.ext import *
from Logger import write_log

BOT_API_KEY = os.getenv('BOT_API_KEY')
print('Bot iniciado...')


def start_command(update, context):
    update.message.reply_text(R.welcome_message(update.message.from_user.first_name))
    write_log("start", update.message.from_user)


def help_command(update, context):
    update.message.reply_text(R.welcome_message(update.message.from_user.first_name))
    update.message.reply_text(
        'Hecho con ❤️por @Nachichuri\. Podés [ver el código acá](https://github.com/Nachichuri/tarjeta-regalo-bot) 🤓\.',
        parse_mode='MarkdownV2')
    write_log("help", update.message.from_user)


def handle_message(update, context):
    update.message.reply_text('Dame un toque... ⏳')

    text = str(update.message.text)
    response = R.main_answers(text)
    update.message.reply_text(response)

    write_log("query", update.message.from_user)


def error(update, context):
    print(f'Update {update} caused error {context.error}')


def main():
    updater = Updater(BOT_API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
