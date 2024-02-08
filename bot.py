from asyncio import run
from logging import INFO, StreamHandler, getLogger
from os import environ
from sys import stdout
from telegram import Update

from telegram.constants import ParseMode
from telegram.ext import Application, ContextTypes, MessageHandler
from telegram.ext.filters import ALL

from datetime import date

# Set up logging
handler = StreamHandler(stdout)
handler.setLevel(INFO)

logger = getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(INFO)



# Get the current date
current_date = date.today()

# Format: DD/MM/YYYY
format1 = current_date.strftime("%d/%m/%Y")

# Keywords
keywords = ["dota", "дота", "дотка", "доту", "дотку", "дотан", "катку", "катка", "каточку", "каточка", "дис", "дискорд", "дискорде", "катать", "играть", "поиграть"]

# Token
token = environ["TELEGRAM_BOT_TOKEN"]

# Mentions string
# mentions = "[гей](tg://user?id=274528988), [пидор](tg://user?id=129026381), [гомик](tg://user?id=469730736), [глиномес](tg://user?id=125631977) и [дырявый](tg://user?id=89097615)"
# Strings of random
reply1 = f"Подходит [Петька](tg://user?id=274528988) к [Василиванычу](tg://user?id=129026381) и спрашивает \n    — Василиваныч, а что такое [НЮАНС](tg://user?id=469730736)? \n Василивааныч и говорит: \n    — Снимай, Петька, штаны. \n Петька снял. \n  Василиваныч достает [хуй](tg://user?id=125631977) и сует Петьке в [жопу](tg://user?id=89097615)... \n    — Вот смотри, Петька, у тебя хуй в жопе, и у меня хуй в жопе. Но есть один нюанс!"
reply2 = f"Из всех бурундуков меня больше всего возбуждает и заводит [Теодор](tg://user?id=89097615). Он такой невинный, такой пухленький, такой милашечка. Я прям представляю как глажу его пушистые [жирные сисечки](tg://user?id=274528988) и ляшечки. Так и хочется чтобы он взял [мой хуй](tg://user?id=129026381) своим нежным девственным ротиком. И чтоб когда сосал, смотрел на меня пронзительным милым взглядом кота из Шрека. А его тоненький писклявый голосочек. Я прям начинаю течь как [сука](tg://user?id=469730736), когда представляю, как натягиваю его [девственный анальчик](tg://user?id=125631977) на мой пульсирующий вставший хуй. А он пищит своим тоненьким пронзительным голоском. Мой хуй проходит через весь желудочно-кишечный тракт и выходит из его сладенького пищевода. И я начинаю дрочить им, словно специальной секс игрушкой, а он захлебывается слюной и пытается беспомощно что-то сделать, начинает молить о пощаде"
reply3 = f"Заходят как-то в таверну [гей](tg://user?id=274528988), [пидор](tg://user?id=129026381), [гомик](tg://user?id=469730736), [глиномес](tg://user?id=125631977) и [дырявый](tg://user?id=89097615). А бармен у них и спрашивает: «А мидера у вас тоже два?»"
reply4 = f"— Кидай на уклонение! — сказал [ведущий](tg://user?id=274528988) тёмному эльфу. \n — Один, — покачал головой [эльф](tg://user?id=89097615). \n — В этот раз не уклонишься от катки в доту! — радостно воскликнули [немая птица](tg://user?id=125631977), [дворф](tg://user?id=129026381) и его [обезьяна](tg://user?id=469730736)."
reply5 = f"Гороскоп на" + " " format1 + ": \n \n **♑** [Козерогов](tg://user?id=274528988) сегодня ждет удача на роли саппорта. Однако без вардов не обойтись даже в самой лоускилльной игре. \n \n **♊** [Близнецам](tg://user?id=469730736) рекомендуется стоять на миду и раз в 5 минут приходить на ганг к своим товарищам, а то их к крипам не подпускает соперник. \n \n **♋** [Раки](tg://user?id=129026381) и их [клешни](tg://user?id=125631977) сегодня узнают, почему баунти хантер не контрится на их рейтинге. Однако с хорошей поддержкой счет 1/7/20 им обеспечен. А что? Он же положительный, даже для керри. \n \n **♌** [Львам](tg://user?id=89097615) сегодня предначертано вновь быть пидорасами с личной жизнью, которые никогда не залетают с пацанами на катку. Однако любой прогноз обратим при должной силе воли."

import random
replies = [reply1, reply2, reply3, reply4, reply5]
random_string = random.choice(replies)

# Handle incoming messages
async def keyword_response(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None or update.message.text is None:
        return
    message = update.message.text.lower()  # Get the text of the incoming message in lowercase
    for keyword in keywords:
        if keyword in message:
            await update.message.reply_text(random_string, parse_mode=ParseMode.MARKDOWN)
            return


def main() -> None:
    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(ALL, keyword_response))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
