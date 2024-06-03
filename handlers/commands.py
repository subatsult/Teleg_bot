from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile, CallbackQuery


router = Router()


@router.message(CommandStart())
async def start(message:Message):
    await message.answer("Hello I'm bot ceo helper")


@router.message(Command(commands=['help']))
async def help(message:Message):
    await message.answer('For help call 911')

@router.message(Command(commands=['about']))
async def about_us(message:Message):
    await message.answer('We are awesome')

@router.message(F.text.lower() == 'hello')
async def hello(message:Message):
    await message.answer("Hello I'm bot ceo helper")