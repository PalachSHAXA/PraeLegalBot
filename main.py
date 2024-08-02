# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.utils import executor
# from aiogram.dispatcher.filters import Text
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
# from keyboards import *
# from settings import BOT_TOKEN, ADMIN_GROUP_ID
# from work import *
# import random
# from reportlab.lib.utils import ImageReader
# import aiohttp
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# import tempfile
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.units import inch
# from reportlab.pdfgen import canvas
# from reportlab.lib import utils
# import tempfile
# import io
# import aiohttp
# from PIL import Image
#
# logging.basicConfig(level=logging.INFO)
# bot = Bot(token=BOT_TOKEN)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
#
#
# class Registration(StatesGroup):
#     name = State()
#     phone = State()
#     city = State()
#     scammer_name = State()
#     theft_amount = State()
#     fraud_method = State()
#     exchange_name = State()
#     conversation_screenshots = State()
#     scam_wallet_address = State()
#
#
# # List of code words
# code_words = [
#     "Солнце", "Луна", "Звезда", "Комета", "Метеор", "Астероид", "Галактика", "Космос", "Вселенная",
#     "МлечныйПуть", "Планета", "Орбита", "Спутник", "Туманность", "Квазары", "Пульсар", "ЧернаяДыра",
#     "Супернова", "Небо", "Созвездие", "Горизонт", "Атмосфера", "Гравитация", "Свет", "Темнота",
#     "Пространство", "Излучение", "Вакуум", "ОзоновыйСлой", "Климат", "Экватор", "Полюс", "Меридиан",
#     "Затмение", "Фазаземли", "ПолярнаяЗвезда", "СеверноеСияние", "ЮжноеСияние", "МагнитноеПоле",
#     "Альбедо", "Радиотелескоп", "Спектр", "ЦентрМассы", "Апогей", "Перигей", "АльфаЦентавра",
#     "Протон", "Электрон", "Нейтрон", "Ион", "Плазма", "Патрон", "Гравитон", "Фотон", "Квант", "Физика",
#     "Астрономия", "Климатология", "Картография", "Биология", "Химия", "Антропология", "Социология",
#     "Психология", "Энтомология", "Экология", "Этнография", "Биофизика", "Геология", "Гидрология",
#     "Метеорология", "Зоология", "Орнитология", "Палеонтология", "Систематика", "Таксономия",
#     "Физиология", "Эволюция", "Генетика", "Микробиология", "Ботаника", "Биохимия", "Цитология",
#     "Иммунология", "МолекулярнаяБиология", "География", "Океанология", "Лимнология", "Экосистема",
#     "Биом", "Фауноведение", "Флора", "Геоботаника", "Орнитофауна"
# ]
#
#
# def generate_unique_case_identifier():
#     serial_number = random.randint(1000, 9999)
#     code_word = random.choice(code_words)
#     return f"{serial_number}-{code_word}"
#
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     user_id = message.from_user.id
#     user = get_user(user_id)
#     if not user:
#         await message.answer("Выберите язык / Choose your language / Tilni tanlang", reply_markup=language_menu())
#     else:
#         await message.answer('Меню', reply_markup=main_keyboard('ru'))
#
# @dp.message_handler(commands=['id'])
# async def start(message: types.Message):
#     chat_id = message.chat.id
#     await message.answer(f"{chat_id}")
#
# @dp.message_handler(Text(equals=['🇺🇿 O\'zbekcha', '🇷🇺 Русский', '🇬🇧 English']))
# async def set_language_and_register(message: types.Message, state: FSMContext):
#     if message.text == '🇺🇿 O\'zbekcha':
#         lang = 'uz'
#     elif message.text == '🇷🇺 Русский':
#         lang = 'ru'
#     else:
#         lang = 'en'
#
#     await state.update_data(language=lang)
#     await start_registration(message, state)
#
# async def start_registration(message: types.Message, state: FSMContext):
#     user_data = await state.get_data()
#     name = message.from_user.full_name
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Введите ваше имя:",
#         'uz': "Ismingizni kiriting:",
#         'en': "Enter your name:"
#     }
#
#     await message.answer(prompts[lang], reply_markup=generate_name(name))
#     await Registration.name.set()
#
# @dp.message_handler(state=Registration.name)
# async def process_name(message: types.Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     contact_keyb = contact_keyboard(lang)
#
#     prompts = {
#         'ru': "Отправьте ваш номер телефона:",
#         'uz': "Telefon raqamingizni yuboring:",
#         'en': "Send your phone number:"
#     }
#
#     await message.answer(prompts[lang], reply_markup=contact_keyb)
#     await Registration.phone.set()
#
#
# @dp.message_handler(content_types=types.ContentType.CONTACT, state=Registration.phone)
# async def process_phone(message: types.Message, state: FSMContext):
#     contact = message.contact
#     if contact is None:
#         await message.answer("Пожалуйста, используйте кнопку для отправки номера телефона.")
#         return
#
#     await state.update_data(phone=contact.phone_number)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Введите ваш город:",
#         'uz': "Shaharingizni kiriting:",
#         'en': "Enter your city:"
#     }
#
#     await message.answer(prompts[lang], reply_markup=ReplyKeyboardRemove())
#     await Registration.city.set()
#
# FAQS = {
#     'ru': {
#         "1. Сколько времени занимает возврат активов?": "Время возврата активов может варьироваться в зависимости от специфики случая. В среднем, процесс обычно занимает от 5 до 6 месяцев. Однако некоторые случаи могут быть решены быстрее или дольше, в зависимости от сложности и необходимых ресурсов.",
#         "2. Возможно ли вернуть потерянные или украденные криптоактивы?": "Да, возможно вернуть потерянные или украденные криптоактивы. Наш успех зависит от различных факторов, таких как тип актива, характер потери и скорость принятия мер. Хотя мы стремимся максимально увеличить шансы на возврат, каждый случай уникален и результаты могут варьироваться.",
#         "3. Сколько вы взимаете за услуги по возврату активов?": "Наши гонорары зависят от специфики каждого случая. Обычно мы взимаем авансовый платеж для покрытия первоначальных расходов и комиссию за возврат в процентах от возвращенной суммы. Этот процент может варьироваться от 10% до 50%, в зависимости от сложности возврата и суммы.",
#         "4. Какую информацию вам нужно предоставить для начала процесса возврата?": "Для начала процесса возврата нам требуется подробная информация о происшествии, включая детали транзакций, адреса кошельков, записи переписки и любую другую релевантную документацию. Чем больше информации вы предоставите, тем лучше мы сможем помочь вам в возврате активов.",
#         "5. Как вы обеспечиваете безопасность и конфиденциальность моей информации?": "Мы придаем большое значение безопасности и конфиденциальности вашей информации. Наша команда использует строгие протоколы безопасности и меры защиты данных, чтобы обеспечить надлежащее обращение с вашей конфиденциальной информацией.",
#         "6. Какие типы криптоактивов вы можете помочь вернуть?": "Мы специализируемся на возврате широкого спектра криптоактивов, включая, но не ограничиваясь, Биткойном, Эфириумом и различными альткойнами. Если вы не уверены, можем ли мы помочь с вашим конкретным активом, пожалуйста, свяжитесь с нами для консультации.",
#         "7. Предоставляете ли вы гарантии на возврат активов?": "Хотя мы стремимся сделать все возможное для возврата ваших активов, мы не можем гарантировать возврат в каждом случае из-за сложностей и неопределенностей. Однако мы предоставим вам тщательную оценку вашей ситуации и обозначим возможный процент успеха перед началом работы.",
#         "8. Как я могу начать пользоваться вашими услугами?": "Чтобы начать, пожалуйста, отправьте всю необходимую информацию о вашем случае через наш сайт или бот. Мы оценим случай и свяжемся с вами с нашими выводами и дальнейшими шагами.",
#         "9. Что происходит, если мои активы не могут быть возвращены?": "Если после тщательного расследования и усилий мы определим, что ваши активы не могут быть возвращены, мы сообщим вам об этом. Обратите внимание, что мы не предоставляем возвраты авансовых платежей, так как они покрывают первоначальные расходы на наше расследование и усилия.",
#         "10. Можете ли вы помочь вернуть активы, потерянные в результате мошенничества или мошеннических действий?": "Да, у нас есть опыт работы с случаями, связанными с мошенничеством и мошенническими действиями. Наша команда будет усердно работать над отслеживанием активов и определением возможных путей возврата. Однако процент успеха варьируется в зависимости от специфики мошенничества и своевременности принятых мер."
#     },
#     'uz': {
#         "1. Kripto aktivlarimni qaytarish qancha vaqtni o`z ichiga oladi?": "Aktivlarni qaytarib olish uchun ketadigan vaqt ishning o'ziga xos xususiyatlariga qarab farq qilishi mumkin. O'rtacha hisobda, bu jarayon odatda 5-6 oy davom etadi. Biroq, ba'zi ishlar murakkabligi va talab etiladigan resurslariga qarab tezroq hal bo'lishi yoki uzoqroq vaqt olishi mumkin.",
#         "2. Yo`qolgan yoki o`g`irlangan kripto aktivlarni qaytarish mumkinmi?": "Ha, yo'qolgan yoki o'g'irlangan kripto aktivlarni qaytarib olish mumkin. Bizning muvaffaqiyatimiz aktiv turi, yo'qotish tabiati va harakat tezligi kabi turli omillarga bog'liq. Biz aktivlarni qaytarib olish imkoniyatlarini maksimal darajada oshirishga harakat qilsak-da, har bir holat o'ziga xos va natijalar ham turlicha bo'lishi mumkin.",
#         "3. Kripto aktivlarni qaytarish xizmatlari uchun qancha haq olasiz?": "Bizning xizmat haqlarimiz har bir holatning o'ziga xos xususiyatlariga bog'liq. Biz odatda dastlabki xarajatlarni qoplash uchun avans to‘lovini va undirilgan summaning foiziga qarab qayta tiklash to‘lovini olamiz. Bu foiz qaytarish qiyinchiligi va jalb qilingan summa kabi omillarga qarab 10% dan 50% gacha bo'lishi mumkin.",
#         "4. Men qaytarish jarayoni boshlanishi uchun qanday ma’lumotlarni taqdim qilishim kerak?": "Qaytarish jarayonini boshlash uchun biz hodisa haqida batafsil ma'lumotni talab qilamiz, jumladan tranzaksiya tafsilotlari, hamyon manzillari, aloqa yozuvlari va boshqa tegishli hujjatlar kabi. Siz qanchalik ko'p ma'lumot taqdim eta olsangiz, biz sizning aktivlaringizni qaytarib olishda shunchalik yaxshi yordam bera olamiz.",
#         "5. Mening ma'lumotlarim xavfsizligi va maxfiyligini qanday ta'minlaysiz?": "Biz sizning ma'lumotlaringiz xavfsizligi va maxfiyligini birinchi o`ringa qo`yamiz. Bizning jamoamiz sizning shaxsiy ma'lumotlaringiz eng yuqori darajadagi e'tibor va maxfiylik bilan ta’minlanishi uchun qat’iy xavfsizlik protokollaridan va ma’lumotlarni himoya qilish chora-tadbirlaridan foydalanadi.",
#         "6. Qanday turdagi kripto aktivlarni tiklashga yordam bera olasiz?": "Biz turli xil kripto aktivlarni qaytarib olishga ixtisoslashganmiz, jumladan, lekin cheklanmagan holda, Bitcoin, Ethereum va turli altcoinlar. Agar siz bizning aniq aktiv bilan yordam bera olishimizdan shubhalansangiz, iltimos, maslahat uchun biz bilan bog’laning.",
#         "7. Siz aktivlarni qaytarish uchun qandaydir kafolatlar taklif qila olasizmi?": "Biz aktivlaringizni qaytarish uchun barcha imkoniyatlarni amalga oshirishga harakat qilsak-da, har bir holatda 100% kafolat bera olmaymiz. Biroq, biz sizning holatingizni batafsil baholaymiz va ishni boshlashdan oldin mumkin bo’lgan muvaffaqiyat darajasini belgilaymiz.",
#         "8. Qanday qilib sizning xizmatlaringizdan foydalanishni boshlashim mumkin?": "Boshlash uchun, iltimos, saytimiz yoki bot orqali sizning holatingiz haqida barcha kerakli ma’lumotlarni yuboring. Biz holatni baholaymiz va sizga keyingi qadamlar va natijalar bilan bog’lanamiz.",
#         "9. Agar aktivlarimni qaytarish imkoniyati bolmasa nima boladi?": "Agar bizning batafsil tekshiruv va harakatlardan so’ng aktivlaringizni qaytarib olish imkoniyati bo’lmasa, biz sizga bu haqda xabar beramiz. E’tibor bering, dastlabki to’lovlarni qaytarib berish yo’q, chunki ular bizning tadqiqot va harakatlarimiz uchun dastlabki xarajatlarni qoplashni o’z ichiga oladi.",
#         "10. Firibgarlik natijasida yo‘qolgan aktivlarni qayta tiklashga yordam bera olasizmi?": "Ha, biz firibgarlik va soxtalashtirish bilan bog’liq holatlar bilan ishlash tajribasiga egamiz. Bizning jamoamiz aktivlarni aniqlash va qaytarish uchun barcha sa’y-harakatlarni amalga oshiradi. Biroq, firibgarlikning xususiyati va tezkorlikka qarab muvaffaqiyat darajasi turlicha bo’lishi mumkin."
#     }
# }
#
#
# @dp.message_handler(lambda message: message.text in ['❓ Часто задаваемые вопросы', '❓ Tez-tez so‘raladigan savollar'])
# async def faq_menu(message: types.Message):
#     lang = 'ru' if message.text == '❓ Часто задаваемые вопросы' else 'uz'
#     markup = faq_keyboard(lang)
#     await message.answer("Выберите вопрос:", reply_markup=markup)
#
# @dp.message_handler(lambda message: message.text in FAQS['ru'] or message.text in FAQS['uz'])
# async def faq_answer(message: types.Message):
#     lang = 'ru' if message.text in FAQS['ru'] else 'uz'
#     answer = FAQS[lang].get(message.text, "Вопрос не найден.")
#     await message.answer(answer)
#
#
# @dp.message_handler(regexp="🔙")
# async def back(message: types.Message):
#     user_id = message.from_user.id
#     lang = get_lang(user_id)
#     if lang == ('ru',):
#         await message.answer('👈🏻', reply_markup=main_keyboard('ru'))
#     elif lang == ('uz',):
#         await message.answer('👈🏻', reply_markup=main_keyboard('uz'))
#
# @dp.message_handler(state=Registration.city)
# async def process_city(message: types.Message, state: FSMContext):
#     await state.update_data(city=message.text)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Введите имя мошенника:",
#         'uz': "Moshennik ismini kiriting:",
#         'en': "Enter the scammer's name:"
#     }
#
#     await message.answer(prompts[lang])
#     await Registration.scammer_name.set()
#
# @dp.message_handler(state=Registration.scammer_name)
# async def process_scammer_name(message: types.Message, state: FSMContext):
#     await state.update_data(scammer_name=message.text)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Введите сумму кражи:",
#         'uz': "O'g'irlik summasini kiriting:",
#         'en': "Enter the theft amount:"
#     }
#
#     await message.answer(prompts[lang])
#     await Registration.theft_amount.set()
#
# @dp.message_handler(state=Registration.theft_amount)
# async def process_theft_amount(message: types.Message, state: FSMContext):
#     await state.update_data(theft_amount=message.text)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Опишите, какая схема мошенничества использовалась:",
#         'uz': "Qanday firibgarlik sxemasi ishlatilganligini tavsiflang:",
#         'en': "Describe the fraud method used:"
#     }
#
#     await message.answer(prompts[lang])
#     await Registration.fraud_method.set()
#
# @dp.message_handler(state=Registration.fraud_method)
# async def process_fraud_method(message: types.Message, state: FSMContext):
#     await state.update_data(fraud_method=message.text)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Введите название биржи мошенника:",
#         'uz': "Moshennikning birjasini kiriting:",
#         'en': "Enter the scammer's exchange name:"
#     }
#
#     await message.answer(prompts[lang])
#     await Registration.exchange_name.set()
#
#
#
# def create_case_pdf(user_data, media_files, pdf_path):
#     c = canvas.Canvas(pdf_path, pagesize=letter)
#     width, height = letter
#
#     # Добавление текста
#     c.drawString(100, height - 50, f"Новая заявка от {user_data['name']}:")
#     c.drawString(100, height - 70, f"Телефон: {user_data['phone']}")
#     c.drawString(100, height - 90, f"Юзернейм: @{user_data['username']}")
#     c.drawString(100, height - 110, f"ID: {user_data['user_id']}")
#     c.drawString(100, height - 130, f"Город: {user_data['city']}")
#     c.drawString(100, height - 150, f"Имя мошенника: {user_data['scammer_name']}")
#     c.drawString(100, height - 170, f"Сумма кражи: {user_data['theft_amount']}")
#     c.drawString(100, height - 190, f"Схема мошенничества: {user_data['fraud_method']}")
#     c.drawString(100, height - 210, f"Биржа мошенника: {user_data['exchange_name']}")
#     c.drawString(100, height - 230, f"Адрес криптокошелька мошенника: {user_data['scam_wallet_address']}")
#     c.drawString(100, height - 250, f"Серийный номер: №{user_data['serial_number']}")
#     c.drawString(100, height - 270, f"Кодовое слово: #{user_data['code_word']}")
#     c.drawString(100, height - 290, f"Описание: {user_data.get('description', 'Нет описания')}")
#
#     # Добавление изображений
#     y_position = height - 320
#     for media in media_files:
#         image = ImageReader(media)
#         c.drawImage(image, 100, y_position, width=400, preserveAspectRatio=True, mask='auto')
#         y_position -= 220
#         if y_position < 100:
#             c.showPage()
#             y_position = height - 50
#
#     c.save()
#
#
# @dp.message_handler(content_types=types.ContentType.PHOTO, state=Registration.conversation_screenshots)
# async def process_conversation_screenshots(message: types.Message, state: FSMContext):
#     photos = message.photo
#     await state.update_data(conversation_screenshots=[photo.file_id for photo in photos])
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#  #todo Media secwtion edit fix bug
#     prompts = {
#         'ru': "Введите адрес криптокошелька мошенника:",
#         'uz': "Firibgarning kriptovalyuta manzilini kiriting:",
#         'en': "Enter the scammer's crypto wallet address:"
#     }
#
#     await message.answer(prompts[lang])
#     await Registration.scam_wallet_address.set()
#
# @dp.message_handler(state=Registration.exchange_name)
# async def process_exchange_name(message: types.Message, state: FSMContext):
#     await state.update_data(exchange_name=message.text)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Прикрепите скриншоты переписки:",
#         'uz': "Suhbatning skrinshotlarini biriktiring:",
#         'en': "Attach screenshots of the conversation:"
#     }
#
#     await message.answer(prompts[lang])
#     await Registration.conversation_screenshots.set()
#
#
#
# def create_case_pdf(user_data, media_files, pdf_file_path):
#     c = canvas.Canvas(pdf_file_path, pagesize=letter)
#     width, height = letter
#
#     # Добавляем информацию о деле
#     c.setFont("Helvetica-Bold", 14)
#     c.drawString(1 * inch, height - 1 * inch, "Новая заявка")
#     c.setFont("Helvetica", 12)
#     c.drawString(1 * inch, height - 1.5 * inch, f"Имя: {user_data['name']}")
#     c.drawString(1 * inch, height - 1.75 * inch, f"Телефон: {user_data['phone']}")
#     c.drawString(1 * inch, height - 2 * inch, f"Юзернейм: @{user_data['username']}")
#     c.drawString(1 * inch, height - 2.25 * inch, f"ID: {user_data['user_id']}")
#     c.drawString(1 * inch, height - 2.5 * inch, f"Город: {user_data['city']}")
#     c.drawString(1 * inch, height - 2.75 * inch, f"Имя мошенника: {user_data['scammer_name']}")
#     c.drawString(1 * inch, height - 3 * inch, f"Сумма кражи: {user_data['theft_amount']}")
#     c.drawString(1 * inch, height - 3.25 * inch, f"Схема мошенничества: {user_data['fraud_method']}")
#     c.drawString(1 * inch, height - 3.5 * inch, f"Биржа мошенника: {user_data['exchange_name']}")
#     c.drawString(1 * inch, height - 3.75 * inch, f"Адрес криптокошелька мошенника: {user_data['scam_wallet_address']}")
#     c.drawString(1 * inch, height - 4 * inch, f"Серийный номер: №{user_data['serial_number']}")
#     c.drawString(1 * inch, height - 4.25 * inch, f"Кодовое слово: #{user_data['code_word']}")
#     c.drawString(1 * inch, height - 4.5 * inch, f"Описание: {user_data.get('description', 'Нет описания')}")
#
#     # Добавляем изображения
#     y_position = height - 5 * inch
#     for img_data in media_files:
#         img = Image.open(io.BytesIO(img_data))
#         img_width, img_height = utils.ImageReader(img).getSize()
#         aspect = img_height / float(img_width)
#         img_width_inch = 6 * inch
#         img_height_inch = img_width_inch * aspect
#
#         if y_position - img_height_inch < 0:
#             c.showPage()
#             y_position = height - 1 * inch
#
#         c.drawImage(utils.ImageReader(img), 1 * inch, y_position - img_height_inch, width=img_width_inch, height=img_height_inch)
#         y_position -= img_height_inch + 0.5 * inch
#
#     c.save()
#
# @dp.message_handler(state=Registration.scam_wallet_address)
# async def process_scam_wallet_address(message: types.Message, state: FSMContext):
#     await state.update_data(scam_wallet_address=message.text)
#
#     user_data = await state.get_data()
#     user_id = message.from_user.id
#     user_data['user_id'] = user_id
#     user_data['username'] = message.from_user.username
#     lang = user_data.get('lang', 'ru')
#     case_id = generate_unique_case_identifier()
#     serial_number, code_word = case_id.split('-')
#
#     user_data['serial_number'] = serial_number
#     user_data['code_word'] = code_word
#
#     save_case(user_id, user_data['name'], user_data['phone'], user_data['city'], user_data['scammer_name'],
#               user_data['theft_amount'], user_data['fraud_method'], user_data['exchange_name'], user_data['scam_wallet_address'],
#               case_id, serial_number, code_word)
#
#     prompts = {
#         'ru': f"Ваше дело успешно сохранено с идентификатором: {case_id}",
#         'uz': f"Sizning ishingiz muvaffaqiyatli saqlandi: {case_id}",
#         'en': f"Your case has been successfully saved with ID: {case_id}"
#     }
#
#     await message.answer(prompts[lang], reply_markup=main_keyboard(lang))
#     await state.finish()
#
#     # Загрузка изображений
#     media_files = []
#     for file_id in user_data.get('conversation_screenshots', []):
#         try:
#             file_info = await bot.get_file(file_id)
#             file_path = file_info.file_path
#             file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"
#             async with aiohttp.ClientSession() as session:
#                 async with session.get(file_url) as response:
#                     if response.status == 200:
#                         media_files.append(await response.read())
#                     else:
#                         print(f"Failed to download file {file_id}, status: {response.status}")
#         except Exception as e:
#             print(f"Error downloading file {file_id}: {e}")
#
#     # Создание PDF
#     with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as temp_file:
#         create_case_pdf(user_data, media_files, temp_file.name)
#         temp_file_path = temp_file.name
#
#     # Отправка PDF в группу
#     caption = f"Кодовое слово: #{code_word}\nОписание: {user_data.get('description', 'Нет описания')}"
#     await bot.send_document(ADMIN_GROUP_ID, open(temp_file_path, 'rb'), caption=caption)
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from keyboards import *
from settings import BOT_TOKEN, ADMIN_GROUP_ID
from work import *
# from aiogram.types import InputMediaPhoto, InputMediaVideo, InputMediaAudio
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from aiogram.types import MediaGroup
from reportlab.lib.utils import ImageReader
# import io
# import tempfile


logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Registration(StatesGroup):
    name = State()
    phone = State()
    city = State()
    scammer_name = State()
    theft_amount = State()
    fraud_method = State()
    exchange_name = State()
    conversation_screenshots = State()
    scam_wallet_address = State()


# List of code words
code_words = [
    "Солнце", "Луна", "Звезда", "Комета", "Метеор", "Астероид", "Галактика", "Космос", "Вселенная",
    "МлечныйПуть", "Планета", "Орбита", "Спутник", "Туманность", "Квазары", "Пульсар", "ЧернаяДыра",
    "Супернова", "Небо", "Созвездие", "Горизонт", "Атмосфера", "Гравитация", "Свет", "Темнота",
    "Пространство", "Излучение", "Вакуум", "ОзоновыйСлой", "Климат", "Экватор", "Полюс", "Меридиан",
    "Затмение", "Фазаземли", "ПолярнаяЗвезда", "СеверноеСияние", "ЮжноеСияние", "МагнитноеПоле",
    "Альбедо", "Радиотелескоп", "Спектр", "ЦентрМассы", "Апогей", "Перигей", "АльфаЦентавра",
    "Протон", "Электрон", "Нейтрон", "Ион", "Плазма", "Патрон", "Гравитон", "Фотон", "Квант", "Физика",
    "Астрономия", "Климатология", "Картография", "Биология", "Химия", "Антропология", "Социология",
    "Психология", "Энтомология", "Экология", "Этнография", "Биофизика", "Геология", "Гидрология",
    "Метеорология", "Зоология", "Орнитология", "Палеонтология", "Систематика", "Таксономия",
    "Физиология", "Эволюция", "Генетика", "Микробиология", "Ботаника", "Биохимия", "Цитология",
    "Иммунология", "МолекулярнаяБиология", "География", "Океанология", "Лимнология", "Экосистема",
    "Биом", "Фауноведение", "Флора", "Геоботаника", "Орнитофауна"
]


def generate_unique_case_identifier():
    serial_number = random.randint(1000, 9999)
    code_word = random.choice(code_words)
    return f"{serial_number}-{code_word}"


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    user = get_user(user_id)
    if not user:
        await message.answer("Выберите язык / Choose your language / Tilni tanlang", reply_markup=language_menu())
    else:
        await message.answer('Меню', reply_markup=main_keyboard('ru'))


@dp.message_handler(commands=['id'])
async def start(message: types.Message):
    chat_id = message.chat.id
    await message.answer(f"{chat_id}")


@dp.message_handler(Text(equals=['🇺🇿 O\'zbekcha', '🇷🇺 Русский', '🇬🇧 English']))
async def set_language_and_register(message: types.Message, state: FSMContext):
    if message.text == '🇺🇿 O\'zbekcha':
        lang = 'uz'
    elif message.text == '🇷🇺 Русский':
        lang = 'ru'
    else:
        lang = 'en'

    await state.update_data(language=lang)
    await start_registration(message, state)

async def start_registration(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    name = message.from_user.full_name
    lang = user_data.get('language', 'en')

    prompts = {
        'ru': "Введите ваше имя:",
        'uz': "Ismingizni kiriting:",
        'en': "Enter your name:"
    }

    await message.answer(prompts[lang], reply_markup=generate_name(name))
    await Registration.name.set()

@dp.message_handler(state=Registration.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    user_data = await state.get_data()
    lang = user_data.get('language', 'en')

    contact_keyb = contact_keyboard(lang)

    prompts = {
        'ru': "Отправьте ваш номер телефона:",
        'uz': "Telefon raqamingizni yuboring:",
        'en': "Send your phone number:"
    }

    await message.answer(prompts[lang], reply_markup=contact_keyb)
    await Registration.phone.set()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=Registration.phone)
async def process_phone(message: types.Message, state: FSMContext):
    contact = message.contact
    if contact is None:
        await message.answer("Пожалуйста, используйте кнопку для отправки номера телефона.")
        return

    await state.update_data(phone=contact.phone_number)
    user_data = await state.get_data()
    lang = user_data.get('language', 'en')

    prompts = {
        'ru': "Введите ваш город:",
        'uz': "Shaharingizni kiriting:",
        'en': "Enter your city:"
    }

    await message.answer(prompts[lang], reply_markup=ReplyKeyboardRemove())
    await Registration.city.set()

FAQS = {
    'ru': {
        "1. Сколько времени занимает возврат активов?": "Время возврата активов может варьироваться в зависимости от специфики случая. В среднем, процесс обычно занимает от 5 до 6 месяцев. Однако некоторые случаи могут быть решены быстрее или дольше, в зависимости от сложности и необходимых ресурсов.",
        "2. Возможно ли вернуть потерянные или украденные криптоактивы?": "Да, возможно вернуть потерянные или украденные криптоактивы. Наш успех зависит от различных факторов, таких как тип актива, характер потери и скорость принятия мер. Хотя мы стремимся максимально увеличить шансы на возврат, каждый случай уникален и результаты могут варьироваться.",
        "3. Сколько вы взимаете за услуги по возврату активов?": "Наши гонорары зависят от специфики каждого случая. Обычно мы взимаем авансовый платеж для покрытия первоначальных расходов и комиссию за возврат в процентах от возвращенной суммы. Этот процент может варьироваться от 10% до 50%, в зависимости от сложности возврата и суммы.",
        "4. Какую информацию вам нужно предоставить для начала процесса возврата?": "Для начала процесса возврата нам требуется подробная информация о происшествии, включая детали транзакций, адреса кошельков, записи переписки и любую другую релевантную документацию. Чем больше информации вы предоставите, тем лучше мы сможем помочь вам в возврате активов.",
        "5. Как вы обеспечиваете безопасность и конфиденциальность моей информации?": "Мы придаем большое значение безопасности и конфиденциальности вашей информации. Наша команда использует строгие протоколы безопасности и меры защиты данных, чтобы обеспечить надлежащее обращение с вашей конфиденциальной информацией.",
        "6. Какие типы криптоактивов вы можете помочь вернуть?": "Мы специализируемся на возврате широкого спектра криптоактивов, включая, но не ограничиваясь, Биткойном, Эфириумом и различными альткойнами. Если вы не уверены, можем ли мы помочь с вашим конкретным активом, пожалуйста, свяжитесь с нами для консультации.",
        "7. Предоставляете ли вы гарантии на возврат активов?": "Хотя мы стремимся сделать все возможное для возврата ваших активов, мы не можем гарантировать возврат в каждом случае из-за сложностей и неопределенностей. Однако мы предоставим вам тщательную оценку вашей ситуации и обозначим возможный процент успеха перед началом работы.",
        "8. Как я могу начать пользоваться вашими услугами?": "Чтобы начать, пожалуйста, отправьте всю необходимую информацию о вашем случае через наш сайт или бот. Мы оценим случай и свяжемся с вами с нашими выводами и дальнейшими шагами.",
        "9. Что происходит, если мои активы не могут быть возвращены?": "Если после тщательного расследования и усилий мы определим, что ваши активы не могут быть возвращены, мы сообщим вам об этом. Обратите внимание, что мы не предоставляем возвраты авансовых платежей, так как они покрывают первоначальные расходы на наше расследование и усилия.",
        "10. Можете ли вы помочь вернуть активы, потерянные в результате мошенничества или мошеннических действий?": "Да, у нас есть опыт работы с случаями, связанными с мошенничеством и мошенническими действиями. Наша команда будет усердно работать над отслеживанием активов и определением возможных путей возврата. Однако процент успеха варьируется в зависимости от специфики мошенничества и своевременности принятых мер."
    },
    'uz': {
        "1. Kripto aktivlarimni qaytarish qancha vaqtni o`z ichiga oladi?": "Aktivlarni qaytarib olish uchun ketadigan vaqt ishning o'ziga xos xususiyatlariga qarab farq qilishi mumkin. O'rtacha hisobda, bu jarayon odatda 5-6 oy davom etadi. Biroq, ba'zi ishlar murakkabligi va talab etiladigan resurslariga qarab tezroq hal bo'lishi yoki uzoqroq vaqt olishi mumkin.",
        "2. Yo`qolgan yoki o`g`irlangan kripto aktivlarni qaytarish mumkinmi?": "Ha, yo'qolgan yoki o'g'irlangan kripto aktivlarni qaytarib olish mumkin. Bizning muvaffaqiyatimiz aktiv turi, yo'qotish tabiati va harakat tezligi kabi turli omillarga bog'liq. Biz aktivlarni qaytarib olish imkoniyatlarini maksimal darajada oshirishga harakat qilsak-da, har bir holat o'ziga xos va natijalar ham turlicha bo'lishi mumkin.",
        "3. Kripto aktivlarni qaytarish xizmatlari uchun qancha haq olasiz?": "Bizning xizmat haqlarimiz har bir holatning o'ziga xos xususiyatlariga bog'liq. Biz odatda dastlabki xarajatlarni qoplash uchun avans to‘lovini va undirilgan summaning foiziga qarab qayta tiklash to‘lovini olamiz. Bu foiz qaytarish qiyinchiligi va jalb qilingan summa kabi omillarga qarab 10% dan 50% gacha bo'lishi mumkin.",
        "4. Men qaytarish jarayoni boshlanishi uchun qanday ma’lumotlarni taqdim qilishim kerak?": "Qaytarish jarayonini boshlash uchun biz hodisa haqida batafsil ma'lumotni talab qilamiz, jumladan tranzaksiya tafsilotlari, hamyon manzillari, aloqa yozuvlari va boshqa tegishli hujjatlar kabi. Siz qanchalik ko'p ma'lumot taqdim eta olsangiz, biz sizning aktivlaringizni qaytarib olishda shunchalik yaxshi yordam bera olamiz.",
        "5. Mening ma'lumotlarim xavfsizligi va maxfiyligini qanday ta'minlaysiz?": "Biz sizning ma'lumotlaringiz xavfsizligi va maxfiyligini birinchi o`ringa qo`yamiz. Bizning jamoamiz sizning shaxsiy ma'lumotlaringiz eng yuqori darajadagi e'tibor va maxfiylik bilan ta’minlanishi uchun qat’iy xavfsizlik protokollaridan va ma’lumotlarni himoya qilish chora-tadbirlaridan foydalanadi.",
        "6. Qanday turdagi kripto aktivlarni tiklashga yordam bera olasiz?": "Biz turli xil kripto aktivlarni qaytarib olishga ixtisoslashganmiz, jumladan, lekin cheklanmagan holda, Bitcoin, Ethereum va turli altcoinlar. Agar siz bizning aniq aktiv bilan yordam bera olishimizdan shubhalansangiz, iltimos, maslahat uchun biz bilan bog’laning.",
        "7. Siz aktivlarni qaytarish uchun qandaydir kafolatlar taklif qila olasizmi?": "Biz aktivlaringizni qaytarish uchun barcha imkoniyatlarni amalga oshirishga harakat qilsak-da, har bir holatda 100% kafolat bera olmaymiz. Biroq, biz sizning holatingizni batafsil baholaymiz va ishni boshlashdan oldin mumkin bo’lgan muvaffaqiyat darajasini belgilaymiz.",
        "8. Qanday qilib sizning xizmatlaringizdan foydalanishni boshlashim mumkin?": "Boshlash uchun, iltimos, saytimiz yoki bot orqali sizning holatingiz haqida barcha kerakli ma’lumotlarni yuboring. Biz holatni baholaymiz va sizga keyingi qadamlar va natijalar bilan bog’lanamiz.",
        "9. Agar aktivlarimni qaytarish imkoniyati bolmasa nima boladi?": "Agar bizning batafsil tekshiruv va harakatlardan so’ng aktivlaringizni qaytarib olish imkoniyati bo’lmasa, biz sizga bu haqda xabar beramiz. E’tibor bering, dastlabki to’lovlarni qaytarib berish yo’q, chunki ular bizning tadqiqot va harakatlarimiz uchun dastlabki xarajatlarni qoplashni o’z ichiga oladi.",
        "10. Firibgarlik natijasida yo‘qolgan aktivlarni qayta tiklashga yordam bera olasizmi?": "Ha, biz firibgarlik va soxtalashtirish bilan bog’liq holatlar bilan ishlash tajribasiga egamiz. Bizning jamoamiz aktivlarni aniqlash va qaytarish uchun barcha sa’y-harakatlarni amalga oshiradi. Biroq, firibgarlikning xususiyati va tezkorlikka qarab muvaffaqiyat darajasi turlicha bo’lishi mumkin."
    }
}


@dp.message_handler(lambda message: message.text in ['❓ Часто задаваемые вопросы', '❓ Tez-tez so‘raladigan savollar'])
async def faq_menu(message: types.Message):
    lang = 'ru' if message.text == '❓ Часто задаваемые вопросы' else 'uz'
    markup = faq_keyboard(lang)
    await message.answer("Выберите вопрос:", reply_markup=markup)

@dp.message_handler(lambda message: message.text in FAQS['ru'] or message.text in FAQS['uz'])
async def faq_answer(message: types.Message):
    lang = 'ru' if message.text in FAQS['ru'] else 'uz'
    answer = FAQS[lang].get(message.text, "Вопрос не найден.")
    await message.answer(answer)


@dp.message_handler(regexp="🔙")
async def back(message: types.Message):
    user_id = message.from_user.id
    lang = get_lang(user_id)
    if lang == ('ru',):
        await message.answer('👈🏻', reply_markup=main_keyboard('ru'))
    elif lang == ('uz',):
        await message.answer('👈🏻', reply_markup=main_keyboard('uz'))

@dp.message_handler(state=Registration.city)
async def process_city(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    user_data = await state.get_data()
    lang = user_data.get('language', 'en')

    prompts = {
        'ru': "Введите имя мошенника:",
        'uz': "Moshennik ismini kiriting:",
        'en': "Enter the scammer's name:"
    }

    await message.answer(prompts[lang])
    await Registration.scammer_name.set()

@dp.message_handler(state=Registration.scammer_name)
async def process_scammer_name(message: types.Message, state: FSMContext):
    await state.update_data(scammer_name=message.text)
    user_data = await state.get_data()
    lang = user_data.get('language', 'en')

    prompts = {
        'ru': "Введите сумму кражи:",
        'uz': "O'g'irlik summasini kiriting:",
        'en': "Enter the theft amount:"
    }

    await message.answer(prompts[lang])
    await Registration.theft_amount.set()

@dp.message_handler(state=Registration.theft_amount)
async def process_theft_amount(message: types.Message, state: FSMContext):
    await state.update_data(theft_amount=message.text)
    user_data = await state.get_data()
    lang = user_data.get('language', 'en')

    prompts = {
        'ru': "Опишите, какая схема мошенничества использовалась:",
        'uz': "Qanday firibgarlik sxemasi ishlatilganligini tavsiflang:",
        'en': "Describe the fraud method used:"
    }

    await message.answer(prompts[lang])
    await Registration.fraud_method.set()

@dp.message_handler(state=Registration.fraud_method)
async def process_fraud_method(message: types.Message, state: FSMContext):
    await state.update_data(fraud_method=message.text)
    user_data = await state.get_data()
    lang = user_data.get('language', 'en')

    prompts = {
        'ru': "Введите название биржи мошенника:",
        'uz': "Moshennikning birjasini kiriting:",
        'en': "Enter the scammer's exchange name:"
    }

    await message.answer(prompts[lang])
    await Registration.exchange_name.set()



def create_case_pdf(user_data, media_files, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # Добавление текста
    c.drawString(100, height - 50, f"Новая заявка от {user_data['name']}:")
    c.drawString(100, height - 70, f"Телефон: {user_data['phone']}")
    c.drawString(100, height - 90, f"Юзернейм: @{user_data['username']}")
    c.drawString(100, height - 110, f"ID: {user_data['user_id']}")
    c.drawString(100, height - 130, f"Город: {user_data['city']}")
    c.drawString(100, height - 150, f"Имя мошенника: {user_data['scammer_name']}")
    c.drawString(100, height - 170, f"Сумма кражи: {user_data['theft_amount']}")
    c.drawString(100, height - 190, f"Схема мошенничества: {user_data['fraud_method']}")
    c.drawString(100, height - 210, f"Биржа мошенника: {user_data['exchange_name']}")
    c.drawString(100, height - 230, f"Адрес криптокошелька мошенника: {user_data['scam_wallet_address']}")
    c.drawString(100, height - 250, f"Серийный номер: №{user_data['serial_number']}")
    c.drawString(100, height - 270, f"Кодовое слово: #{user_data['code_word']}")
    c.drawString(100, height - 290, f"Описание: {user_data.get('description', 'Нет описания')}")

    # Добавление изображений
    y_position = height - 320
    for media in media_files:
        image = ImageReader(media)
        c.drawImage(image, 100, y_position, width=400, preserveAspectRatio=True, mask='auto')
        y_position -= 220
        if y_position < 100:
            c.showPage()
            y_position = height - 50

    c.save()


@dp.message_handler(content_types=[types.ContentType.PHOTO, types.ContentType.VIDEO],
                    state=Registration.conversation_screenshots)
async def process_conversation_screenshots(message: types.Message, state: FSMContext):
    data = await state.get_data()
    conversation_screenshots = data.get('conversation_screenshots', [])
    media = MediaGroup()

    if message.photo:
        for photo in message.photo:
            conversation_screenshots.append(photo.file_id)
            media.attach_photo(photo.file_id, caption='')  # Empty caption, can be customized
    if message.video:
        for video in message.video:
            conversation_screenshots.append(video.file_id)
            media.attach_video(video.file_id, caption='')  # Empty caption, can be customized

    await state.update_data(conversation_screenshots=conversation_screenshots)

    user_data = await state.get_data()
    lang = user_data.get('language', 'en')

    prompts = {
        'ru': "Введите адрес криптокошелька мошенника:",
        'uz': "Firibgarning kriptovalyuta manzilini kiriting:",
        'en': "Enter the scammer's crypto wallet address:"
    }

    await message.answer_media_group(media)
    await message.answer(prompts[lang])
    await Registration.scam_wallet_address.set()


@dp.message_handler(state=Registration.exchange_name)
async def process_exchange_name(message: types.Message, state: FSMContext):
    await state.update_data(exchange_name=message.text)
    user_data = await state.get_data()
    lang = user_data.get('language', 'en')

    prompts = {
        'ru': "Прикрепите скриншоты переписки:",
        'uz': "Suhbatning skrinshotlarini biriktiring:",
        'en': "Attach screenshots of the conversation:"
    }

    await message.answer(prompts[lang])
    await Registration.conversation_screenshots.set()

@dp.message_handler(state=Registration.scam_wallet_address)
async def process_scam_wallet_address(message: types.Message, state: FSMContext):
    await state.update_data(scam_wallet_address=message.text)

    user_data = await state.get_data()
    user_id = message.from_user.id
    name = user_data['name']
    phone = user_data['phone']
    city = user_data['city']
    scammer_name = user_data['scammer_name']
    theft_amount = user_data['theft_amount']
    fraud_method = user_data['fraud_method']
    exchange_name = user_data['exchange_name']
    scam_wallet_address = user_data['scam_wallet_address']
    lang = user_data.get('lang', 'ru')
    case_id = generate_unique_case_identifier()
    serial_number, code_word = case_id.split('-')

    save_case(user_id, name, phone, city, scammer_name, theft_amount, fraud_method, exchange_name, scam_wallet_address, case_id, serial_number, code_word)

    prompts = {
        'ru': f"Ваше дело успешно сохранено с идентификатором: {case_id}",
        'uz': f"Sizning ishingiz muvaffaqiyatli saqlandi: {case_id}",
        'en': f"Your case has been successfully saved with ID: {case_id}"
    }

    await message.answer(prompts[lang], reply_markup=main_keyboard(lang))
    await state.finish()

    caption = (f"Новая заявка от {name}:\n"
               f"Телефон: {phone}\n"
               f"Юзернейм: @{message.from_user.username}\n"
               f"ID: {user_id}\n"
               f"Город: {city}\n"
               f"Имя мошенника: {scammer_name}\n"
               f"Сумма кражи: {theft_amount}\n"
               f"Схема мошенничества: {fraud_method}\n"
               f"Биржа мошенника: {exchange_name}\n"
               f"Адрес криптокошелька мошенника: {scam_wallet_address}\n"
               f"Серийный номер: №{serial_number}\n"
               f"Кодовое слово: #{code_word}\n"
               f"Описание: {user_data.get('description', 'Нет описания')}")

    media_files = []

    # Handle conversation screenshots if provided
    for screenshot in user_data.get('conversation_screenshots', []):
        media_files.append(types.InputMediaPhoto(media=screenshot))

    # Send media as an album if multiple files are present
    if media_files:
        if len(media_files) > 1:
            await bot.send_media_group(ADMIN_GROUP_ID, media_files)
            await bot.send_message(ADMIN_GROUP_ID, caption)
        else:
            await bot.send_photo(ADMIN_GROUP_ID, media_files[0].media, caption=caption)
    else:
        await bot.send_message(ADMIN_GROUP_ID, caption)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)





#
# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.utils import executor
# from aiogram.dispatcher.filters import Text
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
# from keyboards import *
# from settings import BOT_TOKEN, ADMIN_GROUP_ID
# from work import *
# from aiogram.types import InputMediaPhoto, InputMediaVideo, InputMediaAudio
#
# logging.basicConfig(level=logging.INFO)
# bot = Bot(token=BOT_TOKEN)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
#
#
# class Registration(StatesGroup):
#     name = State()
#     phone = State()
#     city = State()
#     scammer_name = State()
#     theft_amount = State()
#     fraud_method = State()
#     exchange_name = State()
#     conversation_screenshots = State()
#     scam_wallet_address = State()
#
#
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     user_id = message.from_user.id
#     user = get_user(user_id)
#     if not user:
#         await message.answer("Выберите язык / Choose your language / Tilni tanlang", reply_markup=language_menu())
#     else:
#         await message.answer('Меню', reply_markup=main_keyboard('ru'))
#
#
# @dp.message_handler(commands=['id'])
# async def start(message: types.Message):
#     chat_id = message.chat.id
#     await message.answer(f"{chat_id}")
#
#
# @dp.message_handler(Text(equals=['🇺🇿 O\'zbekcha', '🇷🇺 Русский', '🇬🇧 English']))
# async def set_language_and_register(message: types.Message, state: FSMContext):
#     if message.text == '🇺🇿 O\'zbekcha':
#         lang = 'uz'
#     elif message.text == '🇷🇺 Русский':
#         lang = 'ru'
#     else:
#         lang = 'en'
#
#     await state.update_data(language=lang)
#     await start_registration(message, state)
#
#
# async def start_registration(message: types.Message, state: FSMContext):
#     user_data = await state.get_data()
#     name = message.from_user.full_name
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Введите ваше имя:",
#         'uz': "Ismingizni kiriting:",
#         'en': "Enter your name:"
#     }
#
#     await message.answer(prompts[lang], reply_markup=generate_name(name))
#     await Registration.name.set()
#
#
# @dp.message_handler(state=Registration.name)
# async def process_name(message: types.Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     contact_keyb = contact_keyboard(lang)
#
#     prompts = {
#         'ru': "Отправьте ваш номер телефона:",
#         'uz': "Telefon raqamingizni yuboring:",
#         'en': "Send your phone number:"
#     }
#
#     await message.answer(prompts[lang], reply_markup=contact_keyb)
#     await Registration.phone.set()
#
#
# @dp.message_handler(content_types=types.ContentType.CONTACT, state=Registration.phone)
# async def process_phone(message: types.Message, state: FSMContext):
#     contact = message.contact
#     if contact is None:
#         await message.answer("Пожалуйста, используйте кнопку для отправки номера телефона.")
#         return
#
#     await state.update_data(phone=contact.phone_number)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Введите ваш город:",
#         'uz': "Shaharingizni kiriting:",
#         'en': "Enter your city:"
#     }
#
#     await message.answer(prompts[lang], reply_markup=ReplyKeyboardRemove())
#     await Registration.city.set()
#
#
# @dp.message_handler(state=Registration.city)
# async def process_city(message: types.Message, state: FSMContext):
#     await state.update_data(city=message.text)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Введите имя мошенника:",
#         'uz': "Moshennik ismini kiriting:",
#         'en': "Enter the scammer's name:"
#     }
#
#     await message.answer(prompts[lang])
#     await Registration.scammer_name.set()
#
#
# @dp.message_handler(state=Registration.scammer_name)
# async def process_scammer_name(message: types.Message, state: FSMContext):
#     await state.update_data(scammer_name=message.text)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Введите сумму кражи:",
#         'uz': "O'g'irlik summasini kiriting:",
#         'en': "Enter the theft amount:"
#     }
#
#     await message.answer(prompts[lang])
#     await Registration.theft_amount.set()
#
#
# @dp.message_handler(state=Registration.theft_amount)
# async def process_theft_amount(message: types.Message, state: FSMContext):
#     await state.update_data(theft_amount=message.text)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Опишите, какая схема мошенничества использовалась:",
#         'uz': "Qanday firibgarlik sxemasi ishlatilganligini tavsiflang:",
#         'en': "Describe the fraud method used:"
#     }
#
#     await message.answer(prompts[lang])
#     await Registration.fraud_method.set()
#
#
# @dp.message_handler(state=Registration.fraud_method)
# async def process_fraud_method(message: types.Message, state: FSMContext):
#     await state.update_data(fraud_method=message.text)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Введите название биржи мошенника:",
#         'uz': "Moshennikning birjasini kiriting:",
#         'en': "Enter the scammer's exchange name:"
#     }
#
#     await message.answer(prompts[lang])
#     await Registration.exchange_name.set()
#
#
# @dp.message_handler(state=Registration.exchange_name)
# async def process_exchange_name(message: types.Message, state: FSMContext):
#     await state.update_data(exchange_name=message.text)
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Прикрепите скриншоты переписки:",
#         'uz': "Suhbatning skrinshotlarini biriktiring:",
#         'en': "Attach screenshots of the conversation:"
#     }
#
#     await message.answer(prompts[lang])
#     await Registration.conversation_screenshots.set()
#
#
# @dp.message_handler(state=Registration.scam_wallet_address)
# async def process_scam_wallet_address(message: types.Message, state: FSMContext):
#     await state.update_data(scam_wallet_address=message.text)
#     user_data = await state.get_data()
#
#     user_id = message.from_user.id
#     username = message.from_user.username
#     full_name = message.from_user.full_name
#     phone = user_data['phone']
#     lang = user_data['language']
#     city = user_data['city']
#     scammer_name = user_data['scammer_name']
#     theft_amount = user_data['theft_amount']
#     fraud_method = user_data['fraud_method']
#     exchange_name = user_data['exchange_name']
#     conversation_screenshots = user_data['conversation_screenshots']
#     scam_wallet_address = user_data['scam_wallet_address']
#
#     # Добавление пользователя в базу данных
#     add_user(lang, full_name, phone, username, user_id, city)
#
#     prompts = {
#         'ru': "Вы успешно зарегистрированы!",
#         'uz': "Siz muvaffaqiyatli ro‘yxatdan o‘tdingiz!",
#         'en': "You have successfully registered!"
#     }
#
#     await message.answer(prompts[lang], reply_markup=main_keyboard(lang))
#     await state.finish()
#
#     # Подготовка заявки для админов
#     caption = (f"Новая заявка от {full_name}:\n"
#                f"Телефон: {phone}\n"
#                f"Юзернейм: @{username}\n"
#                f"ID: {user_id}\n"
#                f"Город: {city}\n"
#                f"Имя мошенника: {scammer_name}\n"
#                f"Сумма кражи: {theft_amount}\n"
#                f"Схема мошенничества: {fraud_method}\n"
#                f"Биржа мошенника: {exchange_name}\n"
#                f"Адрес криптокошелька мошенника: {scam_wallet_address}\n"
#                f"Описание: {user_data.get('description', 'Нет описания')}")
#
#     media_files = []
#
#     # Handle conversation screenshots if provided
#     for screenshot in conversation_screenshots:
#         media_files.append(types.InputMediaPhoto(media=screenshot))
#
#     # Send media as an album if multiple files are present
#     if media_files:
#         if len(media_files) > 1:
#             await bot.send_media_group(ADMIN_GROUP_ID, media_files)
#             await bot.send_message(ADMIN_GROUP_ID, caption)
#         else:
#             await bot.send_photo(ADMIN_GROUP_ID, media_files[0].media, caption=caption)
#     else:
#         await bot.send_message(ADMIN_GROUP_ID, caption)
#
#     await message.answer(
#         "Ваша заявка отправлена!" if lang == 'ru' else "Arizangiz yuborildi!" if lang == 'uz' else "Your application has been sent!", reply_markup=main_keyboard(lang))
#
#
# async def on_startup(dispatcher):
#     # Если необходимо, добавьте код инициализации базы данных здесь
#     # await init_db()
#     pass
#
# FAQS = {
#     'ru': {
#         "1. Сколько времени занимает возврат активов?": "Время возврата активов может варьироваться в зависимости от специфики случая. В среднем, процесс обычно занимает от 5 до 6 месяцев. Однако некоторые случаи могут быть решены быстрее или дольше, в зависимости от сложности и необходимых ресурсов.",
#         "2. Возможно ли вернуть потерянные или украденные криптоактивы?": "Да, возможно вернуть потерянные или украденные криптоактивы. Наш успех зависит от различных факторов, таких как тип актива, характер потери и скорость принятия мер. Хотя мы стремимся максимально увеличить шансы на возврат, каждый случай уникален и результаты могут варьироваться.",
#         "3. Сколько вы взимаете за услуги по возврату активов?": "Наши гонорары зависят от специфики каждого случая. Обычно мы взимаем авансовый платеж для покрытия первоначальных расходов и комиссию за возврат в процентах от возвращенной суммы. Этот процент может варьироваться от 10% до 50%, в зависимости от сложности возврата и суммы.",
#         "4. Какую информацию вам нужно предоставить для начала процесса возврата?": "Для начала процесса возврата нам требуется подробная информация о происшествии, включая детали транзакций, адреса кошельков, записи переписки и любую другую релевантную документацию. Чем больше информации вы предоставите, тем лучше мы сможем помочь вам в возврате активов.",
#         "5. Как вы обеспечиваете безопасность и конфиденциальность моей информации?": "Мы придаем большое значение безопасности и конфиденциальности вашей информации. Наша команда использует строгие протоколы безопасности и меры защиты данных, чтобы обеспечить надлежащее обращение с вашей конфиденциальной информацией.",
#         "6. Какие типы криптоактивов вы можете помочь вернуть?": "Мы специализируемся на возврате широкого спектра криптоактивов, включая, но не ограничиваясь, Биткойном, Эфириумом и различными альткойнами. Если вы не уверены, можем ли мы помочь с вашим конкретным активом, пожалуйста, свяжитесь с нами для консультации.",
#         "7. Предоставляете ли вы гарантии на возврат активов?": "Хотя мы стремимся сделать все возможное для возврата ваших активов, мы не можем гарантировать возврат в каждом случае из-за сложностей и неопределенностей. Однако мы предоставим вам тщательную оценку вашей ситуации и обозначим возможный процент успеха перед началом работы.",
#         "8. Как я могу начать пользоваться вашими услугами?": "Чтобы начать, пожалуйста, отправьте всю необходимую информацию о вашем случае через наш сайт или бот. Мы оценим случай и свяжемся с вами с нашими выводами и дальнейшими шагами.",
#         "9. Что происходит, если мои активы не могут быть возвращены?": "Если после тщательного расследования и усилий мы определим, что ваши активы не могут быть возвращены, мы сообщим вам об этом. Обратите внимание, что мы не предоставляем возвраты авансовых платежей, так как они покрывают первоначальные расходы на наше расследование и усилия.",
#         "10. Можете ли вы помочь вернуть активы, потерянные в результате мошенничества или мошеннических действий?": "Да, у нас есть опыт работы с случаями, связанными с мошенничеством и мошенническими действиями. Наша команда будет усердно работать над отслеживанием активов и определением возможных путей возврата. Однако процент успеха варьируется в зависимости от специфики мошенничества и своевременности принятых мер."
#     },
#     'uz': {
#         "1. Kripto aktivlarimni qaytarish qancha vaqtni o`z ichiga oladi?": "Aktivlarni qaytarib olish uchun ketadigan vaqt ishning o'ziga xos xususiyatlariga qarab farq qilishi mumkin. O'rtacha hisobda, bu jarayon odatda 5-6 oy davom etadi. Biroq, ba'zi ishlar murakkabligi va talab etiladigan resurslariga qarab tezroq hal bo'lishi yoki uzoqroq vaqt olishi mumkin.",
#         "2. Yo`qolgan yoki o`g`irlangan kripto aktivlarni qaytarish mumkinmi?": "Ha, yo'qolgan yoki o'g'irlangan kripto aktivlarni qaytarib olish mumkin. Bizning muvaffaqiyatimiz aktiv turi, yo'qotish tabiati va harakat tezligi kabi turli omillarga bog'liq. Biz aktivlarni qaytarib olish imkoniyatlarini maksimal darajada oshirishga harakat qilsak-da, har bir holat o'ziga xos va natijalar ham turlicha bo'lishi mumkin.",
#         "3. Kripto aktivlarni qaytarish xizmatlari uchun qancha haq olasiz?": "Bizning xizmat haqlarimiz har bir holatning o'ziga xos xususiyatlariga bog'liq. Biz odatda dastlabki xarajatlarni qoplash uchun avans to‘lovini va undirilgan summaning foiziga qarab qayta tiklash to‘lovini olamiz. Bu foiz qaytarish qiyinchiligi va jalb qilingan summa kabi omillarga qarab 10% dan 50% gacha bo'lishi mumkin.",
#         "4. Men qaytarish jarayoni boshlanishi uchun qanday ma’lumotlarni taqdim qilishim kerak?": "Qaytarish jarayonini boshlash uchun biz hodisa haqida batafsil ma'lumotni talab qilamiz, jumladan tranzaksiya tafsilotlari, hamyon manzillari, aloqa yozuvlari va boshqa tegishli hujjatlar kabi. Siz qanchalik ko'p ma'lumot taqdim eta olsangiz, biz sizning aktivlaringizni qaytarib olishda shunchalik yaxshi yordam bera olamiz.",
#         "5. Mening ma'lumotlarim xavfsizligi va maxfiyligini qanday ta'minlaysiz?": "Biz sizning ma'lumotlaringiz xavfsizligi va maxfiyligini birinchi o`ringa qo`yamiz. Bizning jamoamiz sizning shaxsiy ma'lumotlaringiz eng yuqori darajadagi e'tibor va maxfiylik bilan ta’minlanishi uchun qat’iy xavfsizlik protokollaridan va ma’lumotlarni himoya qilish chora-tadbirlaridan foydalanadi.",
#         "6. Qanday turdagi kripto aktivlarni tiklashga yordam bera olasiz?": "Biz turli xil kripto aktivlarni qaytarib olishga ixtisoslashganmiz, jumladan, lekin cheklanmagan holda, Bitcoin, Ethereum va turli altcoinlar. Agar siz bizning aniq aktiv bilan yordam bera olishimizdan shubhalansangiz, iltimos, maslahat uchun biz bilan bog’laning.",
#         "7. Siz aktivlarni qaytarish uchun qandaydir kafolatlar taklif qila olasizmi?": "Biz aktivlaringizni qaytarish uchun barcha imkoniyatlarni amalga oshirishga harakat qilsak-da, har bir holatda 100% kafolat bera olmaymiz. Biroq, biz sizning holatingizni batafsil baholaymiz va ishni boshlashdan oldin mumkin bo’lgan muvaffaqiyat darajasini belgilaymiz.",
#         "8. Qanday qilib sizning xizmatlaringizdan foydalanishni boshlashim mumkin?": "Boshlash uchun, iltimos, saytimiz yoki bot orqali sizning holatingiz haqida barcha kerakli ma’lumotlarni yuboring. Biz holatni baholaymiz va sizga keyingi qadamlar va natijalar bilan bog’lanamiz.",
#         "9. Agar aktivlarimni qaytarish imkoniyati bolmasa nima boladi?": "Agar bizning batafsil tekshiruv va harakatlardan so’ng aktivlaringizni qaytarib olish imkoniyati bo’lmasa, biz sizga bu haqda xabar beramiz. E’tibor bering, dastlabki to’lovlarni qaytarib berish yo’q, chunki ular bizning tadqiqot va harakatlarimiz uchun dastlabki xarajatlarni qoplashni o’z ichiga oladi.",
#         "10. Firibgarlik natijasida yo‘qolgan aktivlarni qayta tiklashga yordam bera olasizmi?": "Ha, biz firibgarlik va soxtalashtirish bilan bog’liq holatlar bilan ishlash tajribasiga egamiz. Bizning jamoamiz aktivlarni aniqlash va qaytarish uchun barcha sa’y-harakatlarni amalga oshiradi. Biroq, firibgarlikning xususiyati va tezkorlikka qarab muvaffaqiyat darajasi turlicha bo’lishi mumkin."
#     }
# }
#
#
# @dp.message_handler(lambda message: message.text in ['❓ Часто задаваемые вопросы', '❓ Tez-tez so‘raladigan savollar'])
# async def faq_menu(message: types.Message):
#     lang = 'ru' if message.text == '❓ Часто задаваемые вопросы' else 'uz'
#     markup = faq_keyboard(lang)
#     await message.answer("Выберите вопрос:", reply_markup=markup)
#
# @dp.message_handler(lambda message: message.text in FAQS['ru'] or message.text in FAQS['uz'])
# async def faq_answer(message: types.Message):
#     lang = 'ru' if message.text in FAQS['ru'] else 'uz'
#     answer = FAQS[lang].get(message.text, "Вопрос не найден.")
#     await message.answer(answer)
#
#
# @dp.message_handler(regexp="🔙")
# async def back(message: types.Message):
#     user_id = message.from_user.id
#     lang = get_lang(user_id)
#     if lang == ('ru',):
#         await message.answer('👈🏻', reply_markup=main_keyboard('ru'))
#     elif lang == ('uz',):
#         await message.answer('👈🏻', reply_markup=main_keyboard('uz'))
#
#
# @dp.message_handler(content_types=types.ContentType.PHOTO, state=Registration.conversation_screenshots)
# async def process_conversation_screenshots(message: types.Message, state: FSMContext):
#     photos = message.photo
#     await state.update_data(conversation_screenshots=[photo.file_id for photo in photos])
#     user_data = await state.get_data()
#     lang = user_data.get('language', 'en')
#
#     prompts = {
#         'ru': "Введите адрес криптокошелька мошенника:",
#         'uz': "Firibgarning kriptovalyuta manzilini kiriting:",
#         'en': "Enter the scammer's crypto wallet address:"
#     }
#
#     await message.answer(prompts[lang])
#     await Registration.scam_wallet_address.set()
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, on_startup=on_startup)


