from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def language_menu():
    return ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
        KeyboardButton(text='🇺🇿 O\'zbekcha'),
        KeyboardButton(text='🇷🇺 Русский'),
        KeyboardButton(text='🇬🇧 English')
    )

def main_keyboard(lang):
    if lang == "ru":
        return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
            KeyboardButton(text='❓ Часто задаваемые вопросы'),
            KeyboardButton(text='📬 Оставить заявку')
        )
    elif lang == "uz":
        return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
            KeyboardButton(text='❓ Tez-tez so‘raladigan savollar'),
            KeyboardButton(text='📬 Ariza qoldirish')
        )
    else:
        return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
            KeyboardButton(text='❓ Frequently Asked Questions'),
            KeyboardButton(text='📬 Submit Application')
        )


def contact_keyboard(lang):
    if lang == "ru":
        return ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton(text="Отправить контакт", request_contact=True)
        )
    elif lang == "uz":
        return ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton(text="Kontaktni yuboring", request_contact=True)
        )
    else:
        return ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton(text="Send contact", request_contact=True)
        )


def generate_name(name):
        return ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton(text=f"{name}")
        )


def faq_keyboard(lang):
    if lang == 'ru':
        buttons = [

            KeyboardButton("1. Сколько времени занимает возврат активов?"),
            KeyboardButton("2. Возможно ли вернуть потерянные или украденные криптоактивы?"),
            KeyboardButton("3. Сколько вы взимаете за услуги по возврату активов?"),
            KeyboardButton("4. Какую информацию вам нужно предоставить для начала процесса возврата?"),
            KeyboardButton("5. Как вы обеспечиваете безопасность и конфиденциальность моей информации?"),
            KeyboardButton("6. Какие типы криптоактивов вы можете помочь вернуть?"),
            KeyboardButton("7. Предоставляете ли вы гарантии на возврат активов?"),
            KeyboardButton("8. Как я могу начать пользоваться вашими услугами?"),
            KeyboardButton("9. Что происходит, если мои активы не могут быть возвращены?"),
            KeyboardButton("10. Можете ли вы помочь вернуть активы, потерянные в результате мошенничества или мошеннических действий?"),
            KeyboardButton("🔙")

        ]
    else:
        buttons = [
            KeyboardButton("1. Kripto aktivlarimni qaytarish qancha vaqtni o`z ichiga oladi?"),
            KeyboardButton("2. Yo`qolgan yoki o`g`irlangan kripto aktivlarni qaytarish mumkinmi?"),
            KeyboardButton("3. Kripto aktivlarni qaytarish xizmatlari uchun qancha haq olasiz?"),
            KeyboardButton("4. Men qaytarish jarayoni boshlanishi uchun qanday ma’lumotlarni taqdim qilishim kerak?"),
            KeyboardButton("5. Mening ma'lumotlarim xavfsizligi va maxfiyligini qanday ta'minlaysiz?"),
            KeyboardButton("6. Qanday turdagi kripto aktivlarni tiklashga yordam bera olasiz?"),
            KeyboardButton("7. Siz aktivlarni qaytarish uchun qandaydir kafolatlar taklif qila olasizmi?"),
            KeyboardButton("8. Qanday qilib sizning xizmatlaringizdan foydalanishni boshlashim mumkin?"),
            KeyboardButton("9. Agar aktivlarimni qaytarish imkoniyati bo`lmasa nima bo`ladi?"),
            KeyboardButton("10. Firibgarlik natijasida yo‘qolgan aktivlarni qayta tiklashga yordam bera olasizmi?"),
            KeyboardButton("🔙")
        ]

    return ReplyKeyboardMarkup( row_width=1).add(*buttons)