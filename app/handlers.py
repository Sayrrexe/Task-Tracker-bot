import app.keyboard as kb
from app.database.requests import set_user
from app.States import User_reg
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

handlers_router = Router()
 
@handlers_router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(User_reg.number)
    await message.reply(f'Привет, {message.from_user.username}! \n Сейчас я помогу тебе разобраться с ботом для максимально приятного использования')
    await message.answer('Для использования бота подтвердите свой номер телефона', reply_markup=kb.phone)
@handlers_router.message(User_reg.number)
async def reg_name(message: Message, state: FSMContext):
    await set_user(message.from_user.id, message.contact.phone_number, message.from_user.username)
    await message.answer(f'Команды: \n/start Команда приветствия ( более ничем не полезна \n/help список всех доступных команд \n/new Создать задачу о Задач ( только для доверенных пользователей)\n/dz Посмотреть задачи Задач по дням \n/all Показывает весё заданное домашнее задание\n\n\n/menu команда для выхода в главное меню и навигиции при момощи кнопок', reply_markup=kb.menu)
    await state.clear()
    

@handlers_router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f'Команды: \n/start Команда приветствия ( более ничем не полезна \n/help список всех доступных команд \n/new Создать задачу о Задач ( только для доверенных пользователей)\n/dz Посмотреть задачи Задач по дням \n/all Показывает весё заданное домашнее задание\n\n\n/menu команда для выхода в главное меню и навигиции при момощи кнопок', reply_markup=kb.menu)
    
@handlers_router.message(Command('menu'))
async def cmd_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Выберите нужное действие', reply_markup=kb.menu)
    
@handlers_router.message(F.text == 'в меню')
async def but_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Выберите нужное действие', reply_markup=kb.menu)

@handlers_router.message(F.text == 'В меню')
async def but_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Выберите нужное действие', reply_markup=kb.menu)
    
@handlers_router.message(F.text =='Профиль')
async def cmd_profile(message: Message):
    await message.answer(f'Профиль пользователя: \nИмя: {message.from_user.username}\nId: `{message.from_user.id}`', reply_markup=kb.inline_main, parse_mode="MARKDOWN")
    
@handlers_router.callback_query(F.data == 'menu')
async def basket(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Выберите нужное действие', reply_markup=kb.menu)
    

