import dotenv
import random
import asyncio
from aiogram import Bot, Dispatcher,F
from aiogram.filters import Command,CommandStart
from aiogram.types import Message, ContentType,ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton,BotCommand,InlineKeyboardButton,InlineKeyboardMarkup
import os
dotenv.load_dotenv()
qwerty:str=os.getenv("qwerty")
bot=Bot(qwerty)
dp=Dispatcher()
a=0
b=0
numbers=[]
plus=KeyboardButton(text="Сложить")
minus=KeyboardButton(text="Вычесть")
umnojit=KeyboardButton(text="Перемножить")
delit=KeyboardButton(text="Разделить")
kb3=ReplyKeyboardMarkup(keyboard=[[plus,minus,umnojit,delit]],one_time_keyboard=True)

poshol_v_jopu=InlineKeyboardButton(text="NINJAGRAM",url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
kb2=InlineKeyboardMarkup(inline_keyboard=[[poshol_v_jopu]])

async def set_menu(bot:Bot):
    commands_menu=[
        BotCommand(command="/help",description="помощь"),
        BotCommand(command="/calc",description="нерабочий калькулятор"),
        BotCommand(command="/game",description="игра"),
        BotCommand(command="/meme",description="мем"),
        BotCommand(command="/demo",description="демо"),
        BotCommand(command="/w_calc",description="рабочий калькулятор"),
        BotCommand(command="/start_meme",description="мем2"),
        BotCommand(command="/mine_efirum",description="майнить эфирум"),
        BotCommand(command="/bruteforce",description="кратко о брутофорсе"),
        BotCommand(command="/usdtorub",description="доллар сша в рублях (актуаьно на 11.07.2025)")
    ]
    await bot.set_my_commands(commands_menu)
dp.startup.register(set_menu)

async def help(message:Message):
    await message.answer(text="Позвони в 112, не знаю ¯\_(ツ)_/¯")
async def calc(message:Message):
    await message.answer(text="Win+R calc.exe ^_^")
async def game(message:Message):
    await message.answer(text="квак 3 арена запусти, не знаю =)")
async def meme(message:Message):
    await message.answer(text="👇ВНИЗУ ССЫЛКА НА НИНДЗЯГРАМ👇",reply_markup=kb2)
async def demo(message:Message):
    await message.answer(text="Привет я де***о-свинья. я умею... ну пока ничего дельного . пожалуйста попользуйтесь этим ботом :3")
async def usd_to_rub(message:Message):
    await message.answer(text="1 USD = 77,80 RUB (11.07.2025)")
async def working_calc1(message:Message):
    await message.answer(text="Введи числа для действий через пробел:")
async def working_calc2(message:Message):
    global a
    global c
    global b
    numbers=message.text.split(" ")
    for i in numbers:
        if not i.isdigit():
            

        global a
        global c
        global b
        a=int(numbers[0])
        b=int(numbers[1])
        await message.answer(text="Обработка...")
        await message.answer(text="Выбери действие👇",reply_markup=kb3)
    if message.text=="Сложить":
        await message.answer(text="Плюсую...")
        c=a+b
        await message.answer(text=f"Готово! Ответ: {c}")
    if message.text=="Вычесть":
        await message.answer(text="Вычитаю...")
        c=a-b
        await message.answer(text=f"Готово! Ответ: {c}")
    if message.text=="Перемножить":
        await message.answer(text="Умножаю...")
        c=a*b
        await message.answer(text=f"Готово! Ответ: {c}")
    if message.text=="Разделить":
        await message.answer(text="Делю...")
        c=a/b
        await message.answer(text=f"Готово! Ответ: {c}")

dp.message.register(usd_to_rub,Command(commands=["usdtorub"]))
dp.message.register(help,Command(commands=["help"]))
dp.message.register(calc,Command(commands=["calc"]))
dp.message.register(game,Command(commands=["game"]))
dp.message.register(meme,Command(commands=["meme"]))
dp.message.register(demo,Command(commands=["demo"]))
dp.message.register(working_calc1,Command(commands=["w_calc"]))
dp.message.register(working_calc2,F.text)


obosratsa=KeyboardButton(text="Обосрался")
kb=ReplyKeyboardMarkup(keyboard=[[obosratsa]],one_time_keyboard=True)
@dp.message(Command(commands=["start_meme"]))
async def start_obosratsa(message:Message):
    await message.answer(text="Бу!")
    await message.answer(text="Испгался?",reply_markup=kb)
@dp.message(F.text=="Обосрался")
async def procces_button(message:Message):
    await message.answer(text="Трус)",reply_markup=ReplyKeyboardRemove())

@dp.message(Command(commands=["bruteforce"]))
async def bruteforce_start(message:Message):
    await message.answer(text="Полный перебор (или метод «грубой силы», англ. brute force) — метод решения математических задач. Относится к классу методов поиска решения исчерпыванием всевозможных вариантов[англ.]. Сложность полного перебора зависит от количества всех возможных решений задачи. Если пространство решений очень велико, то полный перебор может не дать результатов в течение нескольких лет или даже столетий.")

@dp.message(Command(commands=["mine_efirum"]))
async def mine_start(message:Message):
    await message.answer(text="Майню эфирум...")

user={
    "random_number":None,
    "attempts":None,
    "total_games":0,
    "in_game":None,
    "win":0
    }

async def proccess_start(message:Message):
    await message.answer("Привет, я бот shit_pig. Я умею загадывать числа. Хочешь попробовать ?")

def get_random():
    return random.randint(1,100)

async def chek_pos(message:Message):
    if not user["in_game"]:
        user["in_game"]=True
        user["random_number"]=get_random()
        user["attempts"]=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        await message.answer("Короч кент всё ок готово")
    elif user["in_game"]:
        await message.answer("малолетний дэбил уже в игре")
async def check_neg(message:Message):
    if not user["in_game"]:
        await message.answer("(")
        exit()
    else:
        await message.answer("малолетний дэбил уже в игре")

async def procces_answer(message:Message):
    if user["in_game"]:
        if int(message.text) == user["random_number"]:
            user["in_game"]=False
            user["total_games"] += 1
            user["win"] += 1
            await message.answer("ура мололетний дебил победил")
        elif int(message.text)>user["random_number"]:
            await message.answer("меньше")
        elif int(message.text)<user["random_number"]:
            await message.answer("больше")
        if user["attempts"]==0:
            user["in_game"]=False
            user["total_games"]+=1
            await message.answer("неа проиграл")
    else:
        exit()



dp.message.register(proccess_start,Command(commands=["start_game"]))
dp.message.register(chek_pos,F.text.lower().in_(["да","конешна","кншн","конечно","конешно","ок","хочу","нет"]))
dp.message.register(check_neg,F.text.lower().in_(["неа"]))
dp.message.register(procces_answer, lambda x: x.text and x.text.isdigit()  and 1<= int(x.text) <= 100)

async def proccess_start(message:Message):
    await message.answer("прывт я дерьмо-свинья")

async def echo(message:Message):
    await message.answer(text=message.text)

async def echo_image(message:Message):
    await message.reply_photo(message.photo[0].file_id)

async def echo_sticker(message:Message):
    await message.answer_sticker(message.sticker.file_id)

async def echo_document(message:Message):
    await message.answer_document(message.document.file_id)

dp.message.register(echo_document,F.conten_type == ContentType.DOCUMENT)
dp.message.register(echo_sticker,F.sticker)
dp.message.register(echo_image,F.content_type == ContentType.PHOTO)
dp.message.register(proccess_start,Command(commands=["start"]))
#dp.message.register(echo)


async def main():
    print("bot_started")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)





if __name__ == "__main__":
    asyncio.run(main())