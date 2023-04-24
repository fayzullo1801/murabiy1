#from environs import Env

# environs kutubxonasidan foydalanish
#env = Env()
#env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
#BOT_TOKEN = ["6127537918:AAHJnRnq4oub0US8AlmYuOjCEBv7enqWZ1Y"]  # Bot toekn
#ADMINS = ["351350395","1994042333"]  # adminlar ro'yxati
#IP = ["lokalhost"]  # Xosting ip manzili
import os
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
ADMINS = list(os.environ.get("ADMINS"))
IP = str(os.environ.get("ip"))
CHANNEL = ["-1001935637483"]
