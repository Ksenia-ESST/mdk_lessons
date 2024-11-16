import asyncio
import logging
import re
import random
import telebot
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command,CommandObject, CommandStart
from aiogram.types import Message,FSInputFile, URLInputFile, BufferedInputFile, LinkPreviewOptions
from aiogram.enums import ParseMode
from typing import Union
from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram import Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters import Command
from aiogram.utils.markdown import hide_link
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.markdown import hide_link\



TOKEN = '8063764692:AAGqqTm_tfavKkgqTSd5oKM9ya0HjhqE8pE'

logging.basicConfig(level = logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

@dp.message(Command('start'))
async def cmd_hello(message: Message):
    
    await message.answer(
        f"Здравствуйте, <b>{message.from_user.full_name}</b>",
            parse_mode=ParseMode.HTML
    )
    kb = [
        [types.KeyboardButton(text="commands")],
        [types.KeyboardButton(text="help")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("Выберите 'commands' что бы просмотреть, что умеет этот бот", reply_markup=keyboard ),
    await message.answer('Выберите "help" что бы понять, как использовать команды', reply_markup=keyboard)

@dp.message(CommandStart(
    deep_link=True,
    magic=F.args.regexp(re.compile(r'book_(\d+)'))
))
async def cmd_start_book(
        message: Message,
        command: CommandObject
):
    book_number = command.args.split("_")[1]
    await message.answer(f"Sending book №{book_number}")

@dp.message(Command('images'))
async def upload_photo(message: Message):

    file_ids = []

    with open("buffer_emulation.jpeg", "rb") as image_from_buffer:
        result = await message.answer_photo(
            BufferedInputFile(
                image_from_buffer.read(),
                filename="image from buffer.jpeg"
            ),
            caption="Привет"
        )
        file_ids.append(result.photo[-1].file_id)

    image_from_pc = FSInputFile("image_from_pc.jpeg")
    result = await message.answer_photo(
        image_from_pc,
        caption="Изображение из файла на компьютере"
    )
    file_ids.append(result.photo[-1].file_id)

    image_from_url = URLInputFile("https://avatars.mds.yandex.net/get-mpic/5252557/img_id844761290857337258.jpeg/orig")
    result = await message.answer_photo(
        image_from_url,
        caption="Изображение по ссылке"
    )
    file_ids.append(result.photo[-1].file_id)
    await message.answer("Отправленные файлы:\n"+"\n".join(file_ids))

@dp.message(Command("link"))
async def cmd_links(message: Message):
    links_text = (
        "https://eyes.nasa.gov/apps/solar-system/#/home"
        "\n"
        "https://t.me/telegram"
    )
    options_3 = LinkPreviewOptions(
        url="https://eyes.nasa.gov/apps/solar-system/#/home",
        prefer_large_media=True
    )
    await message.answer(
        f"Большое превью\n{links_text}",
        link_preview_options=options_3
    )

@dp.message(F.text.lower() == "commands")
async def with_puree(message: types.Message):
    await message.answer("'на данный момент доступны команды, такие как: 'number - выбор чисел от 1 до 9', 'emoji - вывод смайлика', 'info  - информация о том, когда был запущен бот', 'link - переход по ссылке', 'random - выводится любое число от 1 - 999999999'")

@dp.message(F.text.lower() == "help")
async def without_puree(message: types.Message):
    await message.answer("все команды вводятся через '/', если команда не работает, проверьте ее написание")

@dp.message(Command("number"))
async def number(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 10):
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(3)
    await message.answer(
        "Выберите число от 1 до 9:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )
    kb = [
        [types.KeyboardButton(text="commands")],
        [types.KeyboardButton(text="help")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )

@dp.message(F.text.lower() == "1")
async def without_puree(message: types.Message):
    await message.answer("гранат")

@dp.message(F.text.lower() == "2")
async def without_puree(message: types.Message):
    await message.answer("автобус")

@dp.message(F.text.lower() == "3")
async def without_puree(message: types.Message):
    await message.answer("лемур")

@dp.message(F.text.lower() == "4")
async def without_puree(message: types.Message):
    await message.answer("кот")

@dp.message(F.text.lower() == "5")
async def without_puree(message: types.Message):
    await message.answer("кот")

@dp.message(F.text.lower() == "6")
async def without_puree(message: types.Message):
    await message.answer("канарейка")

@dp.message(F.text.lower() == "7")
async def without_puree(message: types.Message):
    await message.answer("симба")

@dp.message(F.text.lower() == "8")
async def without_puree(message: types.Message):
    await message.answer("крол")

@dp.message(F.text.lower() == "9")
async def without_puree(message: types.Message):
    await message.answer("замзамыч")


@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("простое сообщение")

@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply("сообщение с ответом на сообщение")

@dp.message(Command("random"))
async def cmd_random(message: types.Message):
    min_value = 1 
    max_value = 999999999 
    random = random.randint(min_value, max_value)
    await message.answer("Случайное число - ")

@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")

@dp.message(Command("emoji"))
def send_random_emoji(message):
    random_emoji = random.choice(emojis)
    bot.reply_to(message, random_emoji)

# bot = telebot.TeleBot(TOKEN)
emojis = [
    '😃', '😁', '😃', '😄', '😅', '😊', '😇', '🙂', '😉', '😍',
    '😘', '😗', '🤐', '😚', '😜', '😝', '🤑', '🤪', '😎', '🤓',
    '😲', '😳', '😱', '😨', '😰', '😥', '😭', '😢', '😩', '😫',
    '😬', '😡', '😠', '😤', '🤬', '🤡', '👿', '💀', '☠️', '👻',
    '👽', '🧠', '🎃', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', 
    '🧡', '💛', '💚', '💙', '🩵', '💜', '🖤', '🩶', '🤍', '🐵', 
    '🐒', '🦍', '🦧', '🐶', '🐕', '🦮', '🐕‍🦺', '🐩', '🐺', '🦊', 
    '🦝', '🐈', '🦁', '🐯', '🐅', '🐴', '🫎', '🫏', '🐎', '🦄', 
    '🦓', '🦌', '🦬', '🐮', '🐃', '🐄', '🐏', '🐐', '🐁', '🐫', 
    '🦙', '🦒', '🦒', '🐘', '🦣', '🦏', '🦔', '🐭', '🐀', '🐹', 
    '🐰', '🐇', '🐿️', '🦫', '🦇', '🐻', '🐻‍❄️', '🐼', '🦥', '🦦',
    '🦅', '🦆', '🦢', '🦷', '🦉', '🦤', '🪶', '🦩', '🦜', '🪽', 
    '🐦‍⬛', '🪿', '🐦‍🔥', '🐦', '🐸', '🐊', '🐢', '🦎', '🐍', '🐲', 
    '🦕', '🦖', '🐳', '🐋', '🐬', '🦭', '🐠', '🐠', '🦈', '🐙', 
    '🐚', '🪸', '🪼', '🐌', '🐛', '🐜', '🐝', '🐞', '🦗', '🪳', 
    '🕷️', '🕸️', '🦂', '🦟', '🪱', '🦠', '💐', '💮', '🏵️', '🌹', 
    '🥀', '🌻', '🌼', '🪻', '🌱', '🪴', '🌲', '🌳', '🌴', '🌵', 
    '🌾', '☘️', '🍁', '🍂', '🪹', '🍄', '🍇', '🥥', '🥑', '🥦', 
    '🥒', '🍄‍🟫', '🫐', '🍒', '🌽', '🍤', '🦞', '🦐', '🦑', '🍭', 
    '🍫', '🍻', '🍺', '🍸', '🍾', '🏺', '🧊', '🧉', '🎂', '🎄', 
    '🎆', '🎇', '🧨', '✨', '🎉', '🎊', '🎁', '🎟️', '⚽', '⚾', 
    '🏀', '🏐', '🏈', '🎾', '🥏', '🥎', '🏉', '🧩', '🎲', '🎱', 
    '🔮', '🪩', '♠️', '♥️', '♣️', '♣️', '🌏', '🧱', '🗻', '🌋', '🌃', 
    '🏙️', '🌄', '🌅', '🌆', '🌇', '🌉', '🌠', '🌌', '⛅', '🌝', 
    '🌞', '🌙', '⭐', '🌦️', '🌪️', '🌨️', '🌟', '🌚', '🌓', '🌀', 
    '🌂', '☄️', '🔥', '⚡', '⛱️', '💧', '🌊', '☃️', '🕶️', '🎶', 
    '🎤', '📱', '💻', '🖨️', '🎥', '📸', '💡', '🖇️', '⛓️', '🩸', 
    '💊', '🩹', '🪤', '🚪', '🧿', '🗿', '❌', '☑️', '❎'
]
# bot.polling()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, mylist=[1, 2, 3])

if __name__ == "__main__":
    asyncio.run(main())

class ChatTypeFilter(BaseFilter): 
    def __init__(self, chat_type: Union[str, list]): 
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool: 
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type

router = Router()

@router.message(
    ChatTypeFilter(chat_type=["group", "supergroup"]),
    Command(commands=["emoji"]),
)
async def cmd_emoji_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.emoji)

@router.message(
    ChatTypeFilter(chat_type=["group", "supergroup"]),
    Command(commands=["reels"]),
)

async def cmd_reels_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.reels)

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"])
)
@router.message(Command("emoji"))
async def cmd_emoji_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.emoji)

@router.message(Command("reels"))
async def cmd_reels_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.reels)