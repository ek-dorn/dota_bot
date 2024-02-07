from asyncio import run
from logging import INFO, StreamHandler, getLogger
from os import environ
from sys import stdout
from telegram import Update

from telegram.constants import ParseMode
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

# Mentions string
mentions = "[гиперсодомит](tg://user?id=nkognit0), [мегагей](tg://user?id=madmaniako), [ультрапидор](tg://user?id=pseusys), [кибергомик](tg://user?id=bunnynobugs)"


# Handle incoming messages
async def keyword_response(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.lower()  # Get the text of the incoming message in lowercase
    for keyword in keywords:
        if keyword in message:
            await update.message.reply_text(f"{keyword} {mentions}", parse_mode=ParseMode.MARKDOWN)
            return


def main() -> None:
    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(ALL, keyword_response))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
