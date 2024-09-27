from aiogram.fsm.state import State, StatesGroup

class User_reg(StatesGroup):
    number = State()
   
class Add_Protect_user_fsm(StatesGroup):
    idU = State()
    
class Dell_Protect_user_fsm(StatesGroup):
    idDU = State()

class show_lessons(StatesGroup):
    show_ll = State()
    show_me_ll = State()
    
class all_spam_class(StatesGroup):
    text = State()
    
class Create_tasks_fsm(StatesGroup):
    Ritem = State()
    date = State()
    mounth = State()
    text = State()
    
class Show_tasks(StatesGroup):
    lesson = State()

  