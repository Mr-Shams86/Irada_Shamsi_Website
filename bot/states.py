from aiogram.fsm.state import StatesGroup
from aiogram.fsm.state import State


class ReviewStates(StatesGroup):
    waiting_for_language = State()
    waiting_for_rating = State()
    waiting_for_comment = State()
