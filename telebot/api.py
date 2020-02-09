import telebot
from telebot import apihelper

bot = telebot.TeleBot('1060336857:AAHnYKNYKRUbk2MBJDr5PsjAY-pD9bKzFsU')

apihelper.proxy = {'https': 'https://163.172.146.119:8811'}


# Приветсвие бота после старта
@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Помощь', callback_data='help')
    )
    # keyboard.add(
    #     telebot.types.InlineKeyboardButton(
    #         'Получить свои деньги', url='@webtraderBot/cash')
    # )
    bot.send_message(
        message.chat.id,
        'Привет!\nЯ бот по имени "Кэш"!\n'
        'Если хочешь срубить бабла по-быстрому, я тебе помогу;)\n'
        'Пользуйся кнопками ниже для получения информации',
        reply_markup=keyboard)


# обработчик help-а
@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Сообщение разработчику', url='telegram.me/s1lv3rr')
    )
    bot.send_message(
        message.chat.id,
        '1) Чтобы купить карт с балансом - нажимай /cash.\n',
        reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "help":
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")


# обработчик /cash
@bot.message_handler(commands=['cash'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Давай уже карт', url='https://webtrader.store')
    )
    bot.send_message(
        message.chat.id,
        '1) Есть карты на любой вкус и цвет с балансом от 50к до 300к рублей.\n',
        reply_markup=keyboard)


# обработка текста
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
