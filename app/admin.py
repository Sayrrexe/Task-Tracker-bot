from aiogram import Router, F
from aiogram.filters import Command
from aiogram.filters.base import Filter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.database.requests import ( get_approved_users, approve_user, disapprove_user,      all_user_info, delete_task, get_all_users_tg_id, get_all_tasks )
from config import ADMINS_ID
import app.keyboard as kb
from app.States import Add_Protect_user_fsm, Dell_Protect_user_fsm, show_lessons, all_spam_class


admin_router = Router()

class AdminProtect(Filter):
    def __init__(self):
        self.admins = ADMINS_ID

    async def __call__(self, message: Message):
        return message.from_user.id in self.admins

   
@admin_router.message(AdminProtect(), Command('apanel'))
async def apanel_cmd(message: Message):
    await message.answer('Это панель администратора', reply_markup=kb.admin)
    
@admin_router.message(AdminProtect(), F.text == 'Панель')
async def apanel_text_cmd(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Это панель администратора', reply_markup=kb.admin)
    
@admin_router.message(AdminProtect(), F.text == 'Пользователи.')
async def ad_pol(message: Message, state: FSMContext):
    await message.answer('выберите действие', reply_markup=kb.Users_changes)
   
@admin_router.message(AdminProtect(), F.text == 'Добавить Пользователя в доверенные.')
async def ad_pol(message: Message, state: FSMContext):
    await state.set_state(Add_Protect_user_fsm.idU)
    await message.answer('ВВедите ID пользователя для добавление в доверенные. Для отмены напишите "Отмена"', reply_markup=kb.out)
    
@admin_router.message(Add_Protect_user_fsm.idU)
async def add_user(message: Message, state: FSMContext):
    if message.text == 'Отмена':
        await message.answer('Действие отменено', reply_markup=kb.admin)
        await state.clear()
        return
    await approve_user(message.from_user.id)
    await message.answer('Пользователь добавлен в доверенные', reply_markup=kb.admin)
    await state.clear()
    
@admin_router.message(AdminProtect(), F.text =='Удалить пользователя из доверенных.')
async def del_pol(message: Message, state: FSMContext):
    await state.set_state(Dell_Protect_user_fsm.idDU)
    await message.answer('Выберите ID пользователя', reply_markup= await kb.protect())  
     
@admin_router.message(Dell_Protect_user_fsm.idDU)
async def del_us(message: Message, state: FSMContext):
    if message.text == 'Отмена':
        await message.answer('Действие отменено', reply_markup=kb.admin)
        await state.clear()
        return
    await disapprove_user(message.text)
    await message.answer('Пользователь удалён из доверенных', reply_markup=kb.admin)
    await state.clear()
    
@admin_router.message(AdminProtect(), F.text == 'Информация')
async def ad_pol(message: Message):
    await message.answer('Выберите опцию', reply_markup=kb.info)
    
@admin_router.message(AdminProtect(), F.text =='Все пользователи')
async def def_pol(message: Message):
    try:
        await message.answer(f'Информация о пользователях:\nФормат: Номер:юзернейм:юзид:доступ\n\n{await all_user_info()}')
    except Exception as e:
        await message.reply(f"Произошла ошибка: {e}")
        
@admin_router.message(AdminProtect(), F.text =='Дoверенные пользователи')
async def def_pol(message: Message):
    try:
        await message.answer(str(await get_approved_users()))
    except Exception as e:
        error_message = str(e)
        await message.reply(f"Произошла ошибка: {error_message[:4000]}")
        
@admin_router.message(AdminProtect(), F.text == 'Задачи')
async def dz_changes_def(message: Message):
    await message.answer('Выберите задачу', reply_markup=kb.dz_changes)
        
@admin_router.message(AdminProtect(), F.text == 'Удалить Задачу.')
async def def_check_dz_admin(message: Message, state: FSMContext):
    await message.answer('Выберите нужную задачу', reply_markup=await kb.show_lesson())
    await state.set_state(show_lessons.show_ll)
    
@admin_router.message(show_lessons.show_ll)
async def cmd_show_lesson(message: Message, state: FSMContext):
    try:
        id = message.text.split(':')[0]
        await delete_task(id)
        await message.answer('задачу удалена, выберите другую или нажмите панель для возвращения в главное меню', reply_markup= await kb.show_lesson())
    except Exception as e:
        await message.reply(f"Произошла ошибка: {e}")
        await state.clear()
        
@admin_router.message(AdminProtect(), F.text == 'Все задачи')
async def all_dz_cmd_for_admin(message: Message):
    list = await get_all_tasks()
    tasks = []
    for hw in list:
        tasks.append(f"{hw.id}: Дата: {hw.due_date},{hw.subject} - {hw.text}, Создал {hw.user}")
    task_text = "\n".join(tasks)
    await message.answer(f'Все задачи домашних заданий: \n{task_text}')
    
@admin_router.message(AdminProtect(), Command('allspam'))
async def all_spam_cmd(message: Message, state: FSMContext):
    await message.answer("Запускаем массовую рассылку, введите нужный текст:")
    await state.set_state(all_spam_class.text)
    
@admin_router.message(all_spam_class.text)
async def all_spam_cmd_text(message: Message, state: FSMContext):
    text = message.text
    await state.clear()
    file_content = await get_all_users_tg_id()
    (file_content)
    for user in file_content:
        if user:  # Проверяем, что строка не пустая
            try:
                find_user = int(user)
                await message.bot.send_message(chat_id=find_user, text=text)
            except Exception as e:
                # Обрабатываем случай, когда строку нельзя преобразовать в число
                print(f"Неправильное значение: {user}")
                await message.answer(f'Возникла ошибка {e}')
    await message.answer('Рассылка успешно завершена')
    