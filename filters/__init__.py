from os import name

from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from . Guruh import Guruh



if name == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(Guruh)
