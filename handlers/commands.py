from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile, CallbackQuery
import handlers.keyboards as KB


router = Router()


@router.message(CommandStart())
async def start(message:Message):
    await message.answer("Hello I'm bot ceo helper", reply_markup=KB.kb)


@router.message(Command(commands=['help']))
async def help(message:Message):
    await message.answer('For help call 911')


@router.message(F.text.lower() == 'hello')
async def hello(message:Message):
    await message.answer("Hello I'm bot ceo helper")


@router.message(F.text == 'Departments')
async def departments(message:Message):
    await message.answer('Choose departmnets', reply_markup=await KB.departments_kb())