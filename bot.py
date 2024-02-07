from asyncio import run
from logging import INFO, StreamHandler, getLogger
from os import environ
from sys import stdout
from telegram import Update

from telegram.ext import Application, ContextTypes, MessageHandler
from telegram.ext.filters import ALL


# Set up logging
handler = StreamHandler(stdout)
handler.setLevel(INFO)

logger = getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(INFO)

# Keywords
keywords = ["dota", "дота", "дотка", "доту", "дотку"]

# Token
token = environ["TELEGRAM_BOT_TOKEN"]


# Handle incoming messages
async def keyword_response(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.lower()  # Get the text of the incoming message in lowercase
    for keyword in keywords:
        if keyword in message:
            await update.message.reply_text(f"<a href="dolbaeb.com">гиперсодомит</a> <a href="dolbaeb.com">мегагей</a> <a href="dolbaeb.com">ультрапидор</a> <a href="dolbaeb.com">кибергомик</a>")
            return


def main():
    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(ALL, keyword_response))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
