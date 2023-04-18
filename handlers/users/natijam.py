from aiogram.dispatcher.filters import Command, Text
from keyboards.default.key import menu
from aiogram.types import Message

import logging


from loader import dp,db


# Echo bot
@dp.message_handler(text="🧮 natijam")
async def menyubot(message: Message):
    
    ismi = message.from_user.full_name
    idlar = int(message.from_user.id)
    userlar = db.select_all_users()

    for user in userlar:
       
        if idlar == user[0]:
           ishkal = user[0]
           listlar = user[1]
            
           

           
    await message.answer(f"Sizning so`rovingiz bo`yicha malumotlar\n \n{ismi}  Ball:  {listlar}✅" )
