from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='6807212910:AAHlUxhVhqcAK3uxtrFiHRIB76MywAw295o')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! Im Gunther Bot, Please follow my YT channel")

@dp.message_handler(commands=['logo'])
async def logo(message: types.Message):
    await message.answer_photo('https://avatars.githubusercontent.com/u/62240649?v=4')

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
