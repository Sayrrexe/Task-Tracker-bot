from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from app.database.requests import get_approved_users, get_all_tasks, get_unique_required_days


phone = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Подтвердить номер телефона', request_contact=True)],
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Создать задачу'),
     KeyboardButton(text='Посмотреть Задач')],
    [KeyboardButton(text='Профиль')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

admin = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Пользователи.'),
    KeyboardButton(text='Задачи')],
    [KeyboardButton(text='в меню')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

out = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отмена')]
],
                           resize_keyboard=True,)


async def protect():
    data = await get_approved_users()
    keyboard = ReplyKeyboardBuilder()
    for brand in data:
        brand = str(brand)
        keyboard.add(KeyboardButton(text=brand))
    keyboard.add(KeyboardButton(text='Отмена'))
    return keyboard.adjust(1).as_markup(resize_keyboard=True)

info = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Дoверенные пользователи')],
    [KeyboardButton(text='Все пользователи')],
    [KeyboardButton(text='Панель')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='В меню',callback_data='menu')],
])
dz_changes = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Все задачи')],
    [KeyboardButton(text='Удалить Задачу.')],
    [KeyboardButton(text='Панель')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

Users_changes = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Информация')],
    [KeyboardButton(text='Добавить Пользователя в доверенные.'),
    KeyboardButton(text='Удалить пользователя из доверенных.')],
    [KeyboardButton(text='Панель')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

lessons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Русский Язык'),
     KeyboardButton(text='Литература'),
    ],
    [KeyboardButton(text='АнглДА'),
     KeyboardButton(text='АнглКА'),
    ],
    [KeyboardButton(text='Алгебра'),
     KeyboardButton(text='Геометрия'),
    ],
    [KeyboardButton(text='Физика'),
     KeyboardButton(text='История'),
    ],
    [KeyboardButton(text='Общество'),
     KeyboardButton(text='Химия'),
    ],
    [KeyboardButton(text='ОБЖ'),
     KeyboardButton(text='Информатика'),
    ],
    [KeyboardButton(text='Биология'),
     KeyboardButton(text='География'),
    ],
    [KeyboardButton(text='Отмена')
    ],
    
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

Mounth = ReplyKeyboardMarkup(keyboard=[
#    [KeyboardButton(text='Январь'),
#     KeyboardButton(text='Февраль'),
#    ],
#    [KeyboardButton(text='Март'),
#     KeyboardButton(text='Апрель'),
#    ],
#    [KeyboardButton(text='Май'),
#     KeyboardButton(text='Май'),
#    ],
    [KeyboardButton(text='Сентябрь'),
     KeyboardButton(text='Октябрь'),
    ],
#    [KeyboardButton(text='Ноябрь'),
#     KeyboardButton(text='Декабрь'),
#    ],
    [KeyboardButton(text='Отмена')],
   
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')

async def numbers():
    keyboard = ReplyKeyboardBuilder()
    for i in range(1, 32):
        keyboard.add(KeyboardButton(text=str(i)))
    keyboard.add(KeyboardButton(text='Отмена'))
    return keyboard.adjust(4).as_markup(resize_keyboard=True)

async def show_lesson():
    keyboard = ReplyKeyboardBuilder()
    tasks = await get_all_tasks()  # Получаем все Задачи
    for hw in tasks:
        # Добавляем ID и текст задания в кнопку
        keyboard.add(KeyboardButton(text=f"{hw.id}: Дата: {hw.due_date}, Предмет: {hw.subject}, задачу: {hw.text}"))
    keyboard.add(KeyboardButton(text='Панель'))
    return keyboard.adjust(1).as_markup(resize_keyboard=True)

admin_check_dz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Удалить задачу')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')


async def show_lesson_with_days():
    keyboard = ReplyKeyboardBuilder()
    tasks = await get_unique_required_days()  # Получаем все Задачи
    for hw in tasks:
        # Добавляем ID и текст задания в кнопку
        keyboard.add(KeyboardButton(text=hw))
    keyboard.add(KeyboardButton(text='В меню'))
    return keyboard.adjust(1).as_markup(resize_keyboard=True)