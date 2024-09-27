import app.keyboard as kb

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

from app.States import Create_Dz_fsm, Show_Dz
from app.database.requests import get_approved_users, create_new_task, get_task_by_date
from config import MONTH_DICT


User_router = Router()


@User_router.message(F.text =='Создать задачу')
async def add_dz(message: Message, state: FSMContext):
    Users_list = await get_approved_users()
    for users in Users_list:
        if users == message.from_user.id:
            await state.set_state(Create_Dz_fsm.Ritem)
            await message.answer('Выберите ветку, на которую задана задача', reply_markup=kb.lessons)
            return
    await message.answer("У вас нет доступа к созданию задач.", reply_markup=kb.menu)
    await state.clear()
    
@User_router.message(Create_Dz_fsm.Ritem)
async def add_date(message: Message, state: FSMContext):
    if message.text == 'Отмена' or message.text == '/menu':
        await message.answer('Выберите пункт меню', reply_markup=kb.menu)
        await state.clear()
        return
    await state.update_data(Ritem = message.text)
    await state.set_state(Create_Dz_fsm.date)
    await message.answer('Напишите Число (1-31)', reply_markup= await kb.numbers())

@User_router.message(Create_Dz_fsm.date)
async def Create_Dz_fsm_name(message: Message, state: FSMContext):
    if message.text == 'Отмена' or message.text == '/menu':
        await message.answer('Выберите пункт меню', reply_markup=kb.menu)
        await state.clear()
        return
    await state.update_data(date=message.text)
    await state.set_state(Create_Dz_fsm.mounth)
    await message.answer('Выберите месяц', reply_markup=kb.Mounth)
    
@User_router.message(Create_Dz_fsm.mounth)
async def Create_Dz_name(message: Message, state: FSMContext):
    if message.text == 'Отмена' or message.text == '/menu':
        await message.answer('Выберите пункт меню', reply_markup=kb.menu)
        await state.clear()
        return
    await state.update_data(mounth=message.text)
    await state.set_state(Create_Dz_fsm.text)
    await message.answer('Напишите Домашнее задание')
    
@User_router.message(Create_Dz_fsm.text)
async def Create_Dz_name(message: Message, state: FSMContext):
    if message.text == 'Отмена' or message.text == '/menu':
        await message.answer('Выберите пункт меню', reply_markup=kb.menu)
        await state.clear()
        return
    if len(message.text) >= 100:
        await message.answer('Задание превышает 100 символов, пожалуйста сократите его')
        return
    await state.update_data(text=message.text)
    data = await state.get_data()
    Ritem = data['Ritem']
    date = data['date']
    month = data['mounth']
    month = MONTH_DICT[month]
    text = data['text']
    
    await create_new_task(Ritem, date, month, text, message.from_user.id)
    await message.answer(f"Информация о добавленном Задач: \n{date} {month}:\n{Ritem} - {text}", reply_markup=kb.menu)
    
    await state.clear()
   

@User_router.message(F.text =='Посмотреть Задач')
async def show_dz(message: Message, state: FSMContext):
    await state.set_state(Show_Dz.lesson)
    await message.answer('выберите нужный день: ', reply_markup=await kb.show_lesson_with_days())

@User_router.message(Show_Dz.lesson)
async def show_dz_dz(message: Message, state: FSMContext):
    if message.text == 'В меню' or message.text == '/menu':
        await message.answer('Выберите пункт меню', reply_markup=kb.menu)
        await state.clear()
        return
    task = await get_task_by_date(message.text)
    task_text = "\n".join(task)
    await message.answer(f'Домашнее задание на {message.text}:\n\n`{task_text}`', parse_mode=ParseMode.MARKDOWN)
    