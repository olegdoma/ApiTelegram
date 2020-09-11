from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bt_1 = InlineKeyboardButton(text="1", callback_data='1')
bt_2 = InlineKeyboardButton(text="2", callback_data="2")
bt_3 = InlineKeyboardButton(text="3", callback_data="3")
bt_4 = InlineKeyboardButton(text="4", callback_data="4")
bt_5 = InlineKeyboardButton(text="5", callback_data="5")
bt_6 = InlineKeyboardButton(text="6", callback_data="6")
bt_7 = InlineKeyboardButton(text="7", callback_data="7")
bt_8 = InlineKeyboardButton(text="8", callback_data="8")
bt_9 = InlineKeyboardButton(text="9", callback_data="9")
bt_0 = InlineKeyboardButton(text="0", callback_data="0")
bt_summ = InlineKeyboardButton(text="+", callback_data="+")
bt_equal = InlineKeyboardButton(text="=", callback_data="=")

digitals = InlineKeyboardMarkup(resize_keyboard=True).add(bt_1).add(bt_2).add(bt_3).add(bt_4).add(bt_5).\
                                 add(bt_6).add(bt_7).add(bt_8).add(bt_9).add(bt_0).add(bt_summ).add(bt_equal)

