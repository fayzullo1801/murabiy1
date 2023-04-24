from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, bot
import logging

    

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photot(message: types.Message):
    await message.reply(message.photo[-1].file_id)
    
    
    

@dp.message_handler(text="📚 malumot")
async def malumotlar(message: types.Message):
    malumot = f"Assalomu alaykum hurmatliy ishtirokchi😊\n "
    malumot += f"🎁 Sizga aytib o`tgan kitoblarimizni yutib olishingiz uchun :\n<b>1  Boshlash</b> buyrug`ini yuborsangiz \n<b>2</b>  Sizga botimiz tominidan alohida link ajratib beriladi \n"
    malumot += f"<b>3</b>  Ushbu linkni ko`proq inlonlarga ulashing \n"
    malumot += f"<b>4</b>  Botimizga azo bo`lgan har bir ishtirokchi uchun sizga <b>1 BALL</b> dan qo`shib boriladi\n"
    malumot += f" Va anglaganingizdek <b>G`OLIBLAR</b> eng ko`p ball to`plagan ishtirokchilar bo`lishadi   shoshiling 20ta kitoblardan biri sizni kutmoqda!!! \n eslatib o`tamiz ushbu tanlov 15 -mayga qadar davom etadi"
    await message.answer(malumot) 

@dp.message_handler(text="✅ boshlash")
async def boshlash(message: types.Message):
    text = f"🎁  Eng sara 20ta kitob to`plamlari va kitoblardan birini yutib olishni istaysizmi? Unda <b>Murabbiy akademiy </b>  tashkil etgan tanlovlad qatnashib, kitoblarni yutib oling!\n\n"

    text += f"<b>📚 Shartlar juda oddiy, Sovg`alar esa manfaatli!</b>\n \n"
                
    text += f"Тanlovda ishtirok etish uchun 👇"
    text += f"https://t.me/murabbiy_akademiy_bot?start={message.from_user.id}"
    photo_id = "AgACAgIAAxkBAAIBYmRGtKQIlvl1jU69O92OypYDD1QGAALjxjEblwY4SnLC05i66RsBAQADAgADeQADLwQ"
    await message.reply_photo(photo_id, caption=text) 
