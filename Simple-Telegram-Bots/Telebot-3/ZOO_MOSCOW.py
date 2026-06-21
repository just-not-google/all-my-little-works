from FILES import *
import telebot
from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    text = "Здравствуйте, вас приветствует бот\n<a href='{}'>Московского зоопарка</a>!\n\nЧем я могу вам помочь?\n/test - Узнать какое ты животное\n/contacts - Контакты для связи\n/feedback - Оставить отзыв\n/website - Сайт зоопарка".format(url)
    item1 = types.KeyboardButton("/test")
    item2 = types.KeyboardButton("/contacts")
    item3 = types.KeyboardButton("/feedback")
    item4 = types.KeyboardButton("/website")
    markup.add(item1, item2, item3, item4)
    bot.send_photo(message.chat.id, photo, caption=text, parse_mode="HTML", reply_markup=markup)


@bot.message_handler(commands=['website'])
def website(message):
    text = "Официальный сайт:\n<a href='{}'>Ссылка 1</a>\n<a href='{}'>Ссылка 2</a>\n\nОфициальный телеграм-канал:\n<a href='{}'>Ссылка 3</a>".format(url1, url2, url3)
    bot.send_photo(message.chat.id, photo1, caption=text, parse_mode="HTML",)

@bot.message_handler(commands=['contacts'])
def contacts(message):
    text = "Контакты для связи:\n\nТелефон по покупке билетов\n+7 (499) 252-29-51\n\nЦентр воспроизводства\n+7 (962) 971-32-45\ninfo@moscowzoo.center\n\nАдминистрация\nzoopark@culture.mos.ru\n\nПресс-служба\nSaralievBS@culture.mos.ru\n\nОтдел гуманитарных и творческих программ\n+7 (499) 255-57-63\n\nДетский лагерь «ЗооМастерские»\n+7 (499) 255-57-63\n\nОпекунство\n+7 (962) 971-38-75\nzoofriends@moscowzoo.ru\n\nЗаказ экскурсий\n+7 (499) 255-53-75\neducation@moscowzoo.ru\n\nВолонтерам\nVolonterZoo@culture.mos.ru\n\nДежурно-диспетчерская служба\npcn@culture.mos.ru\n\nКлуб Друзей Московского зоопарка\nzoofriends@moscowzoo.ru\n\nАрт-Зебра\n+7 (906) 084-48-41\nArtzebraZoo@culture.mos.ru"
    bot.send_photo(message.chat.id, photo2, caption=text, parse_mode="HTML")


@bot.message_handler(commands=['feedback'])
def request_feedback(message):
    markup = types.ReplyKeyboardRemove()
    msg = bot.reply_to(message, "Пожалуйста, напишите ваше сообщение для обратной связи:", reply_markup = markup)
    bot.register_next_step_handler(msg, process_feedback)


def process_feedback(message):
    try:
        if len(message.text) < 10 or len(message.text) > 200:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/test")
            item2 = types.KeyboardButton("/contacts")
            item3 = types.KeyboardButton("/feedback")
            item4 = types.KeyboardButton("/website")
            markup.add(item1, item2, item3, item4)
            bot.reply_to(message, "Отзыв должен содержать больше 10 символов и меньше 200 символов!", reply_markup=markup)
            return
        markup12 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/test")
        item2 = types.KeyboardButton("/contacts")
        item3 = types.KeyboardButton("/feedback")
        item4 = types.KeyboardButton("/website")
        markup12.add(item1, item2, item3, item4)
        bot.send_message(ADMIN_ID,f"Новое сообщение от пользователя {message.from_user.username} (ID: {message.from_user.id}):\n\n{message.text}")
        bot.send_message(message.chat.id, "Спасибо за ваше сообщение! Мы рассмотрим его в ближайшее время.", reply_markup=markup12)
    except Exception as e:
        bot.reply_to(message, "Произошла ошибка при отправке сообщения. Пожалуйста, попробуйте позже.")

user_data = {}

@bot.message_handler(commands=['test'])
def start_test(message):
    for animal in animals:
        animals[animal][2] = 0

    user_data[message.chat.id] = {
        'question': 1,
        'answers': []
    }
    send_question(message.chat.id)


def send_question(chat_id):
    question_num = user_data[chat_id]['question']
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if question_num == 1:
        bot.send_message(chat_id, "1. Как ты проводишь свободное время?")
        markup.add("Активно — бегаю, прыгаю, исследую мир")
        markup.add("Общаюсь с друзьями или семьёй")
        markup.add("Отдыхаю в одиночестве, наслаждаясь тишиной")
        markup.add("Планирую, анализирую или что-то создаю")

    elif question_num == 2:
        bot.send_message(chat_id, "2. Твоя реакция на опасность?")
        markup.add("Быстро атакую или убегаю")
        markup.add("Прячусь или стараюсь замаскироваться")
        markup.add("Ищу поддержку у других")
        markup.add("Анализирую ситуацию и действую хитро")

    elif question_num == 3:
        bot.send_message(chat_id, "3. Как ты относишься к незнакомцам?")
        markup.add("С любопытством, но настороженно")
        markup.add("Дружелюбно, если они не угрожают")
        markup.add("Нейтрально, пока не узнаю их лучше")
        markup.add("Скептически, пока не пойму их намерения")

    elif question_num == 4:
        bot.send_message(chat_id, "4. Твой стиль общения?")
        markup.add("Энергичный и прямолинейный")
        markup.add("Мягкий и дипломатичный")
        markup.add("Тихий, но выразительный")
        markup.add("Расчётливый и немного загадочный")

    elif question_num == 5:
        bot.send_message(chat_id, "5. Что важнее всего в жизни?")
        markup.add("Свобода и приключения")
        markup.add("Семья и близкие")
        markup.add("Комфорт и безопасность")
        markup.add("Власть и контроль")

    elif question_num == 6:
        bot.send_message(chat_id, "6. Как ты решаешь проблемы?")
        markup.add("Действую быстро и решительно")
        markup.add("Ищу компромисс")
        markup.add("Выжидаю удобный момент")
        markup.add("Разрабатываю сложный план")

    elif question_num == 7:
        bot.send_message(chat_id, "7. Твоя среда обитания?")
        markup.add("Открытые пространства (горы, леса, поля)")
        markup.add("Уютные и тёплые места")
        markup.add("Водная стихия или укромные уголки")
        markup.add("Территория, которую я контролирую")

    elif question_num == 8:
        bot.send_message(chat_id, "8. Как ты относишься к одиночеству?")
        markup.add("Нормально, но быстро начинаю скучать")
        markup.add("Предпочитаю компанию")
        markup.add("Люблю, это мой комфорт")
        markup.add("Использую его для своих планов")

    elif question_num == 9:
        bot.send_message(chat_id, "9. Твоя репутация среди других?")
        markup.add("Смелый и энергичный")
        markup.add("Добрый и заботливый")
        markup.add("Спокойный и мудрый")
        markup.add("Хитрый и влиятельный")

    elif question_num == 10:
        bot.send_message(chat_id, "10. Какое качество тебе ближе?")
        markup.add("Агрессивность (но не злость)")
        markup.add("Преданность")
        markup.add("Гибкость и адаптивность")
        markup.add("Интеллект и стратегическое мышление")

    else:
        show_result(chat_id)
        return

    bot.send_message(chat_id, "Выбери вариант ответа:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    chat_id = message.chat.id
    if chat_id not in user_data:
        return

    question_num = user_data[chat_id]['question']
    answer = message.text
    user_data[chat_id]['answers'].append(answer)

    if question_num == 1:
        if answer == "Активно — бегаю, прыгаю, исследую мир":
            animals["Amur Tiger"][2] += 1
            animals["Gray Wolf"][2] += 1
            animals["Meerkat"][2] += 1
        elif answer == "Общаюсь с друзьями или семьёй":
            animals["Giant Panda"][2] += 1
            animals["Flamingo"][2] += 1
        elif answer == "Отдыхаю в одиночестве, наслаждаясь тишиной":
            animals["Pallas's Cat"][2] += 1
            animals["Snow Leopard"][2] += 1
            animals["Orangutan"][2] += 1
        elif answer == "Планирую, анализирую или что-то создаю":
            animals["Polar Bear"][2] += 1
            animals["Giraffe"][2] += 1

    elif question_num == 2:
        if answer == "Быстро атакую или убегаю":
            animals["Amur Tiger"][2] += 1
            animals["Gray Wolf"][2] += 1
        elif answer == "Прячусь или стараюсь замаскироваться":
            animals["Pallas's Cat"][2] += 1
            animals["Snow Leopard"][2] += 1
        elif answer == "Ищу поддержку у других":
            animals["Giant Panda"][2] += 1
            animals["Orangutan"][2] += 1
        elif answer == "Анализирую ситуацию и действую хитро":
            animals["Flamingo"][2] += 1
            animals["Meerkat"][2] += 1

    elif question_num == 3:
        if answer == "С любопытством, но настороженно":
            animals["Meerkat"][2] += 1
            animals["Gray Wolf"][2] += 1
        elif answer == "Дружелюбно, если они не угрожают":
            animals["Giant Panda"][2] += 1
            animals["Flamingo"][2] += 1
        elif answer == "Нейтрально, пока не узнаю их лучше":
            animals["Orangutan"][2] += 1
            animals["Giraffe"][2] += 1
        elif answer == "Скептически, пока не пойму их намерения":
            animals["Amur Tiger"][2] += 1
            animals["Snow Leopard"][2] += 1

    elif question_num == 4:
        if answer == "Энергичный и прямолинейный":
            animals["Amur Tiger"][2] += 1
            animals["Meerkat"][2] += 1
        elif answer == "Мягкий и дипломатичный":
            animals["Giant Panda"][2] += 1
            animals["Giraffe"][2] += 1
        elif answer == "Тихий, но выразительный":
            animals["Pallas's Cat"][2] += 1
            animals["Orangutan"][2] += 1
        elif answer == "Расчётливый и немного загадочный":
            animals["Snow Leopard"][2] += 1
            animals["Flamingo"][2] += 1

    elif question_num == 5:
        if answer == "Свобода и приключения":
            animals["Gray Wolf"][2] += 1
            animals["Snow Leopard"][2] += 1
        elif answer == "Семья и близкие":
            animals["Giant Panda"][2] += 1
            animals["Orangutan"][2] += 1
        elif answer == "Комфорт и безопасность":
            animals["Pallas's Cat"][2] += 1
            animals["Polar Bear"][2] += 1
        elif answer == "Власть и контроль":
            animals["Amur Tiger"][2] += 1
            animals["Flamingo"][2] += 1

    elif question_num == 6:
        if answer == "Действую быстро и решительно":
            animals["Amur Tiger"][2] += 1
            animals["Gray Wolf"][2] += 1
        elif answer == "Ищу компромисс":
            animals["Giraffe"][2] += 1
            animals["Flamingo"][2] += 1
        elif answer == "Выжидаю удобный момент":
            animals["Pallas's Cat"][2] += 1
            animals["Snow Leopard"][2] += 1
        elif answer == "Разрабатываю сложный план":
            animals["Orangutan"][2] += 1
            animals["Meerkat"][2] += 1

    elif question_num == 7:
        if answer == "Открытые пространства (горы, леса, поля)":
            animals["Gray Wolf"][2] += 1
            animals["Snow Leopard"][2] += 1
        elif answer == "Уютные и тёплые места":
            animals["Giant Panda"][2] += 1
            animals["Orangutan"][2] += 1
        elif answer == "Водная стихия или укромные уголки":
            animals["Polar Bear"][2] += 1
            animals["Pallas's Cat"][2] += 1
        elif answer == "Территория, которую я контролирую":
            animals["Amur Tiger"][2] += 1
            animals["Flamingo"][2] += 1

    elif question_num == 8:
        if answer == "Нормально, но быстро начинаю скучать":
            animals["Meerkat"][2] += 1
            animals["Gray Wolf"][2] += 1
        elif answer == "Предпочитаю компанию":
            animals["Flamingo"][2] += 1
            animals["Giant Panda"][2] += 1
        elif answer == "Люблю, это мой комфорт":
            animals["Pallas's Cat"][2] += 1
            animals["Snow Leopard"][2] += 1
        elif answer == "Использую его для своих планов":
            animals["Orangutan"][2] += 1
            animals["Amur Tiger"][2] += 1

    elif question_num == 9:
        if answer == "Смелый и энергичный":
            animals["Amur Tiger"][2] += 1
            animals["Gray Wolf"][2] += 1
        elif answer == "Добрый и заботливый":
            animals["Giant Panda"][2] += 1
            animals["Giraffe"][2] += 1
        elif answer == "Спокойный и мудрый":
            animals["Orangutan"][2] += 1
            animals["Polar Bear"][2] += 1
        elif answer == "Хитрый и влиятельный":
            animals["Snow Leopard"][2] += 1
            animals["Flamingo"][2] += 1

    elif question_num == 10:
        if answer == "Агрессивность (но не злость)":
            animals["Amur Tiger"][2] += 1
            animals["Gray Wolf"][2] += 1
        elif answer == "Преданность":
            animals["Giant Panda"][2] += 1
            animals["Orangutan"][2] += 1
        elif answer == "Гибкость и адаптивность":
            animals["Pallas's Cat"][2] += 1
            animals["Meerkat"][2] += 1
        elif answer == "Интеллект и стратегическое мышление":
            animals["Snow Leopard"][2] += 1
            animals["Flamingo"][2] += 1



    user_data[chat_id]['question'] += 1
    send_question(chat_id)


def show_result(chat_id):
    max_score = 0
    result_animal = None

    for animal, data in animals.items():
        if data[2] > max_score:
            max_score = data[2]
            result_animal = animal

    if result_animal:
        text123 = "А также ты можешь поддержать своё\nлюбимое животное благодаря проекту:\n<a href='{}'>Возьми животное под опеку</a>".format(url5)
        photo_url = animals[result_animal][0]
        description = animals[result_animal][1]
        markup11 = types.ReplyKeyboardRemove()
        bot.send_photo(chat_id, photo_url)
        bot.send_message(chat_id, f"Твой результат: {result_animal}\n\n{description}\n\n{text123}", reply_markup=markup11, parse_mode="HTML" )
        markup114 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item12 = types.KeyboardButton("/test")
        item22 = types.KeyboardButton("/start")
        markup114.add(item12, item22)
        bot.send_message(chat_id, "Попробовать ещё раз?", reply_markup=markup114)

    if chat_id in user_data:
        del user_data[chat_id]

bot.polling(none_stop=True)