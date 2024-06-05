from aiogram.types import(ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from database.request import *

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Departments')],
        [KeyboardButton(text='Rabs')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Choose action'
)

async def departments_kb():
    departments = await get_departments()
    kb = InlineKeyboardBuilder()
    for depp in departments:
        kb.add(InlineKeyboardButton(text= depp.name, callback_data=f'department_{depp.id}'))

    return kb.adjust(2).as_markup()


