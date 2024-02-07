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
keywords = ["dota", "дота", "дотка", "доту", "дотку", "дотан", "катку", "катка", "каточку", "каточка", "дис", "дискорд", "дискорде", "катать", "играть", "поиграть"]

# Token
token = environ["TELEGRAM_BOT_TOKEN"]

# Mentions string
mentions = "[гей](tg://user?id=274528988), [пидор](tg://user?id=129026381), [гомик](tg://user?id=469730736), [глиномес](tg://user?id=125631977) и [дырявый](tg://user?id=89097615)"


# Handle incoming messages
async def keyword_response(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None or update.message.text is None:
        return
    message = update.message.text.lower()  # Get the text of the incoming message in lowercase
    for keyword in keywords:
        if keyword in message:
            await update.message.reply_text(f"Заходят однажды в таверну {mentions}. А бармен у них и спрашивает: «А мидера у вас тоже два?»", parse_mode=ParseMode.MARKDOWN_V2)
            return


def main() -> None:
    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(ALL, keyword_response))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
