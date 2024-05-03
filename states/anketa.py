"""Импортирует из модуля aiogram нужные методы"""
from aiogram.fsm.state import State, StatesGroup

class Anketa(StatesGroup):
    """Указывает какие объекты есть в классе"""
    name = State()
    age = State()
    gender = State()
    