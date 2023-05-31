from aiogram.types import ReplyKeyboardMarkup,KeyboardButton




back = KeyboardButton('Backend')
front = KeyboardButton('Frontend')
uxui = KeyboardButton('UX-UI')
android = KeyboardButton('Android')
ios = KeyboardButton('Дизайн')
napr_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back,front,uxui,android,ios,KeyboardButton('cancle'))

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(KeyboardButton('да'),KeyboardButton('нет'))

cancle_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True
                                    ).add(KeyboardButton('/cancle'))
