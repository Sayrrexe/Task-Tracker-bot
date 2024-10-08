# Task-Tracker-bot

## Инструмент для создания и отслеживания задач группой лиц, интегрированный в удобный Telegram-бот

Этот бот позволяет пользователям создавать, просматривать и управлять задачами (например, домашними заданиями или проектами), а также предоставляет администраторам расширенные функции для управления пользователями и заданиями.

## Как начать?

1. Скачайте репозиторий:
    ```bash
    git clone https://github.com/Sayrrexe/Task-Tracker-bot.git
    ```

2. Создайте виртуальное окружение и установите необходимые библиотеки:
    ```bash
    # Windows
    python -m venv .venv
    .venv/Scripts/activate
    pip install -r requirements.txt
    ```

    ```bash
    # Linux
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    ```

3. Настройте файл `config.py`:
    - Добавьте в файл API-токен вашего Telegram-бота.
    - Добавьте Telegram ID пользователей, которые будут администраторами.

4. Запустите бота:
    ```bash
    python run.py
    ```

5. С аккаунта администратора зайдите в `/apanel` и добавьте аккаунты администраторов (тех, кто сможет создавать задачи).

---

## Команды

| Команда           | Описание                                                                                 |
|-------------------|------------------------------------------------------------------------------------------|
| **/start**        | Приветствие пользователя и запрос подтверждения номера телефона.                          |
| **/help**         | Показать список всех доступных команд.                                                    |
| **/new**          | Создать новую задачу (только для доверенных пользователей).                               |
| **/tasks**           | Посмотреть задачи по дням.                                                               |
| **/all**          | Показать все заданные задачи.                                                             |
| **/menu**         | Возврат в главное меню.                                                                  |
| **'в меню'**      | Возвращение в главное меню через текстовую команду.                                       |
| **'Профиль'**     | Показать профиль пользователя с его именем и ID в Telegram.                               |

### Административные команды (только для администраторов)

| Команда                  | Описание                                                                                                   |
|--------------------------|------------------------------------------------------------------------------------------------------------|
| **/apanel**               | Открыть панель администратора с дополнительными опциями управления пользователями и задачами.               |
| **'Панель'**              | Открыть панель администратора через текстовую команду.                                                     |
| **'Пользователи.'**       | Перейти в меню управления пользователями (добавление/удаление доверенных пользователей).                    |
| **'Добавить Пользователя в доверенные.'** | Добавить пользователя в доверенные (требуется ввести ID пользователя).                              |
| **'Удалить пользователя из доверенных.'** | Удалить пользователя из доверенных.                                                              |
| **'Информация'**          | Показать информацию о пользователях.                                                                      |
| **'Все пользователи'**    | Показать информацию о всех пользователях (имя, ID, уровень доступа).                                       |
| **'Доверенные пользователи'** | Показать список доверенных пользователей.                                                           |
| **'Задачи'**              | Доступ к управлению задачами.                                                                             |
| **'Удалить Задачу.'**     | Удалить выбранную задачу.                                                                                 |
| **'Все задачи'**          | Показать все задачи.                                                                                      |
| **/allspam**              | Запустить массовую рассылку сообщений всем пользователям.                                                 |

---

## Лицензия

Этот проект распространяется по лицензии MIT. Подробности можно найти в файле `LICENSE`.

