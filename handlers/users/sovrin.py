from aiogram.dispatcher.filters import Command, Text
from keyboards.default.key import menu
from aiogram.types import Message

import logging


from loader import dp,db


# Echo bot
@dp.message_handler(text="🏆 sovrinlar")
async def menyubot(message: Message):
    
    text = f" 1-o`rin  G`OLIBIMIZGA :🥇 Tafsiri hilol, Muallif: Shayx Muhammad Sodiq Muhammad Yusuf \n"
    text += f" 2-o`rin:🥈 Saodat Asri, Muallif: Ahmad Lutfiy Qozonchi\n"        
    text += f" 3-o`rin:🥉 Ruhiy tarbiya, Muallif: Shayx Muhammad Sodiq Muhammad Yusuf\n"
    text += f" 4-o`rin:📓 Kifoya, Muallif: Shayx Muhammad Sodiq Muhammad Yusuf\n"
    text += f" 5-o`rin:📔 Shamoili Muhammadiy, Muallif: Imom Abu Iso Muhammad Termiziy\n"
    text += f" 6-o`rin:📘 Ikki olam sarvari, Muallif: Sayyid Muhammad Xasaniy\n"
    text += f" 7-o`rin:📖 Alloh bilan ko`ngil suhbati Namoz, Muallif: Mehmed Yildiz\n"
    text += f" 8-o`rin:📕 Men Robiya, Muallif: Sadiya Erol Aykach\n"
    text += f" 9-o`rin:✅ Mo`yna kiygan Maddonna, Muallif: Sabahiddin Ali\n"
    text += f" 10-o`rin: Oilamani yaxshi ko`raman, Muallif: Abdulaziz Kiranshal\n"
    text += f" 11-o`rin: Atirgul o`g`risi, Muallif: Alvarov Yunkey\n"
    text += f" 12-o`rin: Ulamolar nazlida vaqtning qadri, Muallif: Abdulfattoh Abu G`udda\n"
    text += f" 13-o`rin: Erbaqon, Muallif: Najmiddin Erbaqon\n"
    text += f" 14-o`rin: Muso Fir`avn o`ldirolmagan Payg`ambar, Muallif: Hakimo`g`li Ismoil\n"
    text += f" 15-o`rin: Savdogarlar ustozi, Muallif: Ahadquli Xolmuhammad o`g`li\n"
    text += f" 16-o`rin: Mening ismim Sano, Muallif: Juliya San Yaman o`g`li\n"
    text += f" 17-o`rin: Mukammal kun, Muallif: Oyshagul Aqoqush Oqgun\n"
    text += f" 18-o`rin: Talabaning odobi, Muallif: Muhammadsodiq Muhammad Ismoil\n"
    text += f" 19-o`rin: Bir olimning kundaligi, Muallif: Abul Faraj Abdurrahmon Ibn Javziy\n"
    text += f" 20-o`rin: O`limga kulib boqqan odam, Muallif: Saydulloh Oydin\n"

    









                
    await message.answer( f"{text}")
