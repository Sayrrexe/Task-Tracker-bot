from app.database.models import async_session
from app.database.models import User, TasksTable
from sqlalchemy import select, delete
from sqlalchemy.future import select

async def set_user(tg_id, phone_number, username): # Создание нового юзера в таблице
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            session.add(User(tg_id=tg_id, phone = phone_number, user_name = username ))
            await session.commit()

async def get_approved_users(): # получаем всех Подтверждённых пользователей
    async with async_session() as session:
        stmt = select(User.tg_id).where(User.Approved == 1)
        
        # Выполняем запрос и получаем результаты
        result = await session.execute(stmt)
        tg_ids = result.scalars().all()
        
        return tg_ids
     
async def approve_user(tg_id): # Подтверждение пользователя ( выдача прав администратора )
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user.Approved == 1:
            session.commit()
            return
        user.Approved = 1
        await session.commit()

async def disapprove_user(tg_id): # Разжалование Доверенного пользователя ( администратора )
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user.Approved == 0:
            session.commit()
            return
        user.Approved = 0
        await session.commit()

async def all_user_info(): # получение информации о всех пользователях которые когда-либо заходили
    async with async_session() as session:
        stmt = select(User.phone, User.user_name, User.tg_id, User.Approved)
        
        # Выполняем запрос и получаем результаты
        result = await session.execute(stmt)
        users = result.fetchall()  # Получаем все задачи
        
        # Форматируем информацию о пользователях
        user_info_list = []
        for phone, username, tgid, approved in users:
            user_info_list.append(f'Пользователь {phone}:{username}:{tgid}:{approved}')
        
        # Объединяем все строки в одну
        return '\n'.join(user_info_list)
    
async def get_all_users_tg_id(): # создание списка TG_ID всех пользователей
    async with async_session() as session:
        stmt = select(User.tg_id)
        result = await session.execute(stmt)
        
        # Извлекаем tg_id и создаем список
        user_tgid_list = [tg_id[0] for tg_id in result.fetchall()]
        
        return user_tgid_list
    
async def delete_task(task_id: int): # Создание нового задания
    async with async_session() as session:
        await session.execute(delete(TasksTable).where(TasksTable.id == task_id))
        await session.commit()
        return

async def get_unique_required_days(): # Получить все уникальные даты ( на которые есть задача )
    async with async_session() as session:
        stmt = select(TasksTable.due_date).distinct()  # Используем distinct, чтобы получить уникальные даты
        result = await session.execute(stmt)
        due_dates = result.scalars().all()
        
        # Преобразуем строки в формат 'MM-DD' и убираем дубликаты
        unique_due_dates = list(set(due_dates))  # Убираем дубликаты
        return unique_due_dates

async def get_all_tasks():
    async with async_session() as session:
        stmt = select(TasksTable)
        result = await session.execute(stmt)
        tasks = result.scalars().all()  # Получаем все объекты task
    
    return tasks

# Создание новой задачи
async def create_new_task(subject: str, date: int, month: str, text: str, user_id: int):
    async with async_session() as session:
        due_date=str(f"{date} {month}")
        new_task = TasksTable(
            subject=subject,
            text=text,
            due_date = due_date,
            user=user_id
        )
        session.add(new_task)
        await session.commit()
        
        
async def get_task_by_date(due_date: str): # получить все даты ( на которые есть задача )
    async with async_session() as session:
        try:
            stmt = select(TasksTable).where(TasksTable.due_date == due_date)
            results = await session.execute(stmt)
            task_list = results.scalars().all()  # Получаем все результаты

            # Формируем список результатов в нужном формате
            result_list = [f"{task.subject} - {task.text}" for task in task_list]
            return result_list
        except Exception as e:
            print(f"An error occurred: {e}")
            return []  # Возвращаем пустой список в случае ошибки