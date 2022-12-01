
from aiogram import Bot, Dispatcher, executor
import os
from dotenv import load_dotenv
from aiogram.types import Message, CallbackQuery, LabeledPrice, InputFile
from work import *
from settings import TOKEN
from keyboards import *
import sqlite3
from aiogram.types import ReplyKeyboardRemove
from geopy.geocoders import Nominatim


load_dotenv()


bot = Bot(TOKEN, parse_mode='HTML')

dp = Dispatcher(bot)

user_data = {}


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, 'Выберите язык|Tilni talang|Choose a language', reply_markup=generate_language_menu())


@dp.message_handler(regexp='Русский 🇷🇺|Özbekcha 🇺🇿|English 🇬🇧')
async def set_language(message: Message):
    chat_id = message.from_user.id
    if message.text == 'Русский 🇷🇺':
        await bot.send_message(chat_id, 'Здравствуйте, вас приветсвует бот PraeLegal Uzbekistan, выберите раздел:', reply_markup=generate_main_menu('Russian 🇷🇺'))
    elif message.text == 'Özbekcha 🇺🇿':
        await bot.send_message(chat_id, 'As salomu aleykum sizni Praelegal Uzbekistan boti kutib oldi, bo’limlardan birini tanlang:', reply_markup=generate_main_menu('Uzbek 🇺🇿'))
    elif message.text == 'English 🇬🇧':
        await bot.send_message(chat_id, 'Hello, welcome to PraeLegal Uzbekistan bot, please choose a section:', reply_markup=generate_main_menu('English 🇬🇧'))


@dp.message_handler(regexp='Локация📍|Geolokatsiya📍|Location📍')
async def geolocation(message: Message):
    chat_id = message.chat.id
    loc_latitude = str(41.2710255)
    loc_longitude = str(69.2606875)
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(loc_latitude + "," + loc_longitude)
    await bot.send_location(chat_id,
                            41.2710255,
                            69.2606875)
    await bot.send_message(chat_id, location)


#dp.message_handler(regexp='Пройти регистрацию 📋')
#sync def ask_full_name(message: Message):
#   global user_data
#   chat_id = message.chat.i
#   user_data['telegram_id'] = chat_id
#   await bot.send_message(chat_id, f"Для начало напишите имя и фамилию: ",
#                          reply_markup=ReplyKeyboardRemove())




@dp.message_handler(regexp='🏢 Тур офиса 360’  🧭|🏢 Ofisga sayr 360’  🧭|🏢 Office tour 360’  🧭')
async def get_to_office(message: Message):
    if message.text == '🏢 Тур офиса 360’  🧭':
        await message.answer('https://uzbekistan360.uz/ru/location/praelegal-uzbekistanKfI', reply_markup=generate_main_menu('Russian 🇷🇺'))
    elif message.text == '🏢 Ofisga sayr 360’  🧭':
        await message.answer('https://uzbekistan360.uz/ru/location/praelegal-uzbekistanKfI', reply_markup=generate_main_menu('Uzbek 🇺🇿'))
    elif message.text == '🏢 Office tour 360’  🧭':
        await message.answer('https://uzbekistan360.uz/ru/location/praelegal-uzbekistanKfI', reply_markup=generate_main_menu('English 🇬🇧'))


@dp.message_handler(regexp='📲 Социальные сети  🌍|📲  Ijtimoiy tarmoqlar  🌍|📲  Social media  🌍')
async def websites(message: Message):
    if message.text == '📲 Социальные сети  🌍':
        await message.answer('Здесь вы найдете наши сотть сети на разных платформах', reply_markup=generate_websites_menu('Russian 🇷🇺'))
    elif message.text == '📲  Ijtimoiy tarmoqlar  🌍':
        await message.answer('Bu yerda bizning ijtimoiy tarmoqlarimiz ',
                             reply_markup=generate_websites_menu('Uzbek 🇺🇿'))
    elif message.text == '📲  Social media  🌍':
        await message.answer('There you can find our social media',
                             reply_markup=generate_websites_menu('English 🇬🇧'))


@dp.message_handler(regexp='Instagram 🇷🇺|Instagram 🇺🇿|Instagram 🇬🇧')
async def instagram(message: Message):
    if message.text == 'Instagram 🇷🇺':
        await message.answer('Это нашa страница в инстаграме: https://www.instagram.com/praelegaluz/', reply_markup=generate_main_menu('Russian 🇷🇺'))
    elif message.text == 'Instagram 🇺🇿':
        await message.answer('Bu bizning instagramdagi akauntimiza: https://www.instagram.com/praelegaluz/',reply_markup=generate_main_menu('Uzbek 🇺🇿'))
    elif message.text == 'Instagram 🇬🇧':
        await message.answer('It our page on instagram: https://www.instagram.com/praelegaluz/', reply_markup=generate_main_menu('English 🇬🇧'))


@dp.message_handler(regexp='Facebook 🇷🇺|Facebook 🇺🇿|Facebook 🇬🇧')
async def facebook(message: Message):
    if message.text == 'Facebook 🇷🇺':
        await message.answer('Это нашa страница в фейсбуке: https://m.facebook.com/PraeLegalUzbekistan/', reply_markup=generate_main_menu('Russian 🇷🇺'))
    elif message.text == 'Facebook 🇺🇿':
        await message.answer('Bu bizning feysbukdegi akauntimiz: https://m.facebook.com/PraeLegalUzbekistan/',
                             reply_markup=generate_main_menu('Uzbek 🇺🇿'))
    elif message.text == 'Facebook 🇬🇧':
        await message.answer('It our page on facebook: https://m.facebook.com/PraeLegalUzbekistan/', reply_markup=generate_main_menu('English 🇬🇧'))


@dp.message_handler(regexp='Linkedin 🇷🇺|Linkedin 🇺🇿|Linkedin 🇬🇧')
async def linkedin(message: Message):
    if message.text == 'Linkedin 🇷🇺':
        await message.answer('Это нашa страница в Linkedin: https://ru.linkedin.com/company/praelegal-uzbekistan', reply_markup=generate_main_menu('Russian 🇷🇺'))
    elif message.text == 'Linkedin 🇺🇿':
        await message.answer('Bu bizning Linkedindegi akauntimiz: https://ru.linkedin.com/company/praelegal-uzbekistan',
                             reply_markup=generate_main_menu('Uzbek 🇺🇿'))
    elif message.text == 'Linkedin 🇬🇧':
        await message.answer('It is our page on Linkedin: https://ru.linkedin.com/company/praelegal-uzbekistan', reply_markup=generate_main_menu('English 🇬🇧'))


@dp.message_handler(regexp='Website 🇷🇺|Website 🇺🇿|Website 🇬🇧')
async def website(message: Message):
    if message.text == 'Website 🇷🇺':
        await message.answer('Это наш сайт: https://praelegal.uz/', reply_markup=generate_main_menu('Russian 🇷🇺'))
    elif message.text == 'Website 🇺🇿':
        await message.answer('Bu bizning saytimiz: https://praelegal.uz/', reply_markup=generate_main_menu('Uzbek 🇺🇿'))
    elif message.text == 'Website 🇬🇧':
        await message.answer('It is out website: https://praelegal.uz/', reply_markup=generate_main_menu('English 🇬🇧'))


@dp.message_handler(regexp='☎ Позвонить 📞|☎ Telefon qilish📞|☎   Call   📞')
async def call(message: Message):
    await message.answer_contact(first_name='PraeLegal', last_name='Office', phone_number='+998 95 198 21 12')


@dp.message_handler(regexp='⤴ Вход в офис 🏛️|⤴ Ofisga kirish 🏛️|⤴ Entering the office 🏛️')
async def send_video(message: Message):
   chat_id = message.from_user.id

   video_bytes = InputFile(path_or_bytesio='media/0.MP4')

   if message.text == '⤴ Вход в офис 🏛️':
       await message.answer(' Идет загрузка, подождите 2-3 минуты ')
       await bot.send_video(chat_id=chat_id, video=video_bytes)
       await message.answer('Следуя по видео поднимитесь в офис')
   elif message.text == '⤴ Ofisga kirish 🏛️':
       await message.answer(' Yuklanmoqda, 2-3 daqiqa kutib turing ')
       await bot.send_video(chat_id=chat_id, video=video_bytes)
       await message.answer('Video boyicha ofisga chiqing')
   elif message.text == '⤴ Entering the office 🏛️':
       await message.answer(' Loading in progress, wait 2-3 minute ')
       await bot.send_video(chat_id=chat_id, video=video_bytes)
       await message.answer('Go up to the video following the video')


@dp.message_handler(regexp='⚖ Профайл 📚|⚖ Profayl 📚|⚖ Profile 📚')
async def send_file(message: Message):
    chat_id = message.from_user.id

    if message.text == '⚖ Профайл 📚':
        await message.answer('Идет загрузка, подождите 2-3 минуты')
        await message.answer_document(InputFile('media/Firm Profile.pdf'))
        await message.answer('Прочтите содержимое файла')
    elif message.text == '⚖ Profayl 📚':
        await message.answer('Fayl yuklanmoqda, 2-3 daqiqa kutibturing')
        await message.answer_document(InputFile('media/Firm Profile.pdf'))
        await message.answer('Fayl mazmunini oqib chiqing')
    elif message.text == '⚖ Profile 📚':
        await message.answer('Loading in progress, wait 2-3 minute')
        await message.answer_document(InputFile('media/Firm Profile.pdf'))
        await message.answer('Read the contents of file')


executor.start_polling(dp)
