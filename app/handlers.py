from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb
from aiogram.fsm.state import StatesGroup, State 
from aiogram.fsm.context import FSMContext
import json
import shutil
import subprocess


json_file = "data.json"
backup_file = "data_backup.json"
info = {}



router = Router()

class Reg(StatesGroup):
    notion_token = State()
    data_id = State()

class GetInfo(StatesGroup):
    link = State()
    title = State()
    user_name = State()
    user_id = State()
    chanal_id = State()

@router.message(CommandStart())
async def cmb_start(message: Message, state: FSMContext):
    shutil.copy(backup_file, json_file)
    await state.set_state(Reg.notion_token)
    await message.answer("Type your Ntion Tocen:")

@router.message(Reg.notion_token)
async def notion_tok(message: Message, state: FSMContext):
    await state.update_data(notion_token = message.text)
    await state.set_state(Reg.data_id)
    await message.answer("Type your Database ID: ")

@router.message(Reg.data_id)
async def notion_tok(message: Message, state: FSMContext):
    await state.update_data(data_id = message.text)
    data = await state.get_data()
    info.update(data)
    print(info)
    await message.answer(f"Your Notion Token: {data['notion_token']}\nYour Database ID: {data['data_id']} ", reply_markup=kb.main)
    
    await state.clear()

@router.callback_query(F.data == "save")
async def detect_link(callback: CallbackQuery, state: FSMContext):
    await state.set_state(GetInfo.link)
    await callback.answer("Link or URL")
    await callback.message.answer("Type your link or url")
    

@router.message(GetInfo.link)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(link = message.text)
    await state.set_state(GetInfo.title)
    await message.answer("Type title for a link")

@router.message(GetInfo.title)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(title = message.text)
    await state.update_data(user_name = message.from_user.full_name)
    await state.update_data(user_id = message.from_user.id)
    await state.update_data(user_id = message.bot.id)
    data = await state.get_data()
    await message.answer(f"Your link {data["link"]} \nLink Title {"title"} \nSave?", reply_markup=kb.check)
    info.update(data)
    await state.clear()




@router.callback_query(F.data == "applay")
async def detect_link(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    with open('data.json', 'w') as json_file:
        json.dump(info, json_file, indent=4)
    subprocess.run(["python", "main.py"])
    await callback.message.answer("Your link saved", reply_markup=kb.main)

# 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
# 14adc5ba8a82800b9a98f44cf72c9fcd

