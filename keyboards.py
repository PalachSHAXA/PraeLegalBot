from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


# def generate_register():
#    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#    btn_register = KeyboardButton(text='Пройти регистрацию 📋')
#    markup.add(btn_register)
#    return markup
#


def generate_language_menu():
    return ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(*
                                                                       [
                                                                           KeyboardButton(text='Русский 🇷🇺'),
                                                                           KeyboardButton(text='Özbekcha 🇺🇿'),
                                                                           KeyboardButton(text='English 🇬🇧')
                                                                       ])


#ef generate_send_contact():
#   markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#   send_contact = KeyboardButton(text='Отправить контакт 👤', request_contact=True)
#   markup.add(send_contact)
#   return markup


# def generate_main_menu():
#     markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     btn_location = KeyboardButton(text='Геолокация📍')
#     btn_websites = KeyboardButton(text='Социальные сети 📱')
#     btn_get_office = KeyboardButton(text='Поднятся в офис 🏢')
#     btn_office = KeyboardButton(text='🏢 Офис 360')
#     btn_call = KeyboardButton(text='☎ Позвонить 📞')
#     btn_lang = KeyboardButton(text=' ⚖ О компнании 📑')
#     markup.add(btn_location, btn_websites, btn_get_office, btn_office, btn_call, btn_lang)
#     return markup


def generate_categories(categories):
    markup = KeyboardButton(row_width=2)
    buttons = []
    for category_id, category_name in categories:
        btn = KeyboardButton(text=category_name, callback_data=f'category_{category_id}')
        buttons.append(btn)
        markup.add(*buttons)
        return markup


def generate_websites_menu(lang):
    if lang == "Russian 🇷🇺":
        return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(*
        [
            KeyboardButton(text='Instagram 🇷🇺'),
            KeyboardButton(text='Website 🇷🇺'),
            KeyboardButton(text='Facebook 🇷🇺'),
            KeyboardButton(text='Linkedin 🇷🇺')
        ])
    elif lang == 'Uzbek 🇺🇿':
        return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(*
          [
              KeyboardButton(text='Instagram 🇺🇿'),
              KeyboardButton(text='Website 🇺🇿'),
              KeyboardButton(text='Facebook 🇺🇿'),
              KeyboardButton(text='Linkedin 🇺🇿')
          ])
    elif lang == 'English 🇬🇧':
        return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(*
          [
              KeyboardButton(text='Instagram 🇬🇧'),
              KeyboardButton(text='Website 🇬🇧'),
              KeyboardButton(text='Facebook 🇬🇧'),
              KeyboardButton(text='Linkedin 🇬🇧'),
          ])
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn_instagram = KeyboardButton(text='Instagram')
    btn_website = KeyboardButton(text='Website')
    btn_facebook = KeyboardButton(text='Facebook')
    btn_linkedin = KeyboardButton(text='Linkedin')
    #btn_back = KeyboardButton(text='🔙')
    markup.add(btn_instagram, btn_website, btn_facebook, btn_linkedin)
    return markup

def generate_main_menu(lang):
    if lang == "Russian 🇷🇺":
        return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(*
        [
            KeyboardButton(text='Локация📍'),
            KeyboardButton(text='📲 Социальные сети  🌍 '),
            KeyboardButton(text='⤴ Вход в офис 🏛️'),
            KeyboardButton(text=' 🏢 Тур офиса 360’  🧭'),
            KeyboardButton(text='☎ Позвонить 📞'),
            KeyboardButton(text='⚖ Профайл 📚')
        ])
    elif lang == 'Uzbek 🇺🇿':
        return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(*
          [
              KeyboardButton(
                  text='Geolokatsiya📍'),
              KeyboardButton(
                  text='📲  Ijtimoiy tarmoqlar  🌍'),
              KeyboardButton(text='⤴ Ofisga kirish 🏛️'),
              KeyboardButton(text='🏢 Ofisga sayr 360’  🧭'),
              KeyboardButton(
                  text='☎ Telefon qilish📞'),
              KeyboardButton(text='⚖ Profayl 📚')
          ])
    elif lang == 'English 🇬🇧':
        return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(*
          [
              KeyboardButton(
                  text='Location📍'),
              KeyboardButton(text='📲  Social media  🌍'),
              KeyboardButton(
                  text='⤴ Entering the office 🏛️'),
              KeyboardButton(text=' 🏢 Office tour 360’  🧭'),
              KeyboardButton(text='☎   Call   📞'),
              KeyboardButton(text='⚖ Profile 📚')

          ])