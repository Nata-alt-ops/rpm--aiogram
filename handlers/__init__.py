"""Импорт из модуля aiogram нужных методов"""
from aiogram import Dispatcher
from handlers import anketa, start

def include_routers(dp:Dispatcher):
    """Объединяет все роутеры"""
    dp.include_router(
        start.router,
        anketa.router
    )