from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Сохранить ссылку", callback_data="save")]])

check = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Подтвердить", callback_data="applay")]])
