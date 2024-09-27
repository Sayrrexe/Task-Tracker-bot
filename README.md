# Task-Tracker-bot
 
## Инструмент для создания и отслеживания задач группой лиц интегрированный в удобный телеграм бот

### Как начать?
1. Скачать репозиторий 
	```
	git clone https://github.com/Sayrrexe/Task-Tracker-bot.git
	```
2. Создать Виртуальное окружение и скачать нужные библиотеки
		```	
		# Windows
		python -m venv .venv
		.venv/Scripts/activate
		pip install -r requirements.txt
		

		# Linux
		python3 -m venv .venv
		source .venv/bin/activate
		pip3 install -r requirements.txt
		```
3. Настроить файл Config.py
	добавьте в файл telegram-bot-api вашего бота
	добавьте в файл tg-id пользователей
4. Запустите 
	```
	python run.py
	```
5. С аккаунта администратора зайдите в /apanel и добавьте аккаунты администраторов ( тех кто сможет создавать задачи )
