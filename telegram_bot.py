import telebot
from telebot import types

bot = telebot.TeleBot('7063169730:AAFByWs8LY-judRFN-u5s4MiObFyVdxkLRY')

def vibor_cs_go (message):
    bot.send_message(message.chat.id, """ Секция Counter Strike.<br> <br> Одна из самых популярных секций в CYBER RNM.
Имеется несколько составов разного уровня игры. <br> <br>
RNIMU-1 8-10 уровень FAICET,подходит для ребят желающих попасть в киберспорт - капитан https://vk.com/nukleot1d
<br><br>RNIMU-2 Состав состоит из игроков имеющих 13,000-18,000 рейтинга в CS 2 и от калаша с венками в СS:GO. Подойдёт игрокам выше любителей - капитан https://vk.com/drslyowl
 <br> <br> RNIMU-3 Ребята играющие в своё удовольствие, ведут свои соц.сети и выкладывают хайлайты. подойдёт для игроков играющих на рейтинге до 12.000 и до калаша в CS:GO
Капитан https://vk.com/mqnwinner<br> <br> RNIMU-4 Состав новичков , ребята отвечают за посты в соц.сетях, отметки на тренировках и за организацию внутривузовских мероприятий. Капитан https://vk.com/medic2004 <br><br> """)
    start(message)
def vibor_LOL (message):
    bot.send_message(message.chat.id, "это вызывается функция для LOL'a (будут кнопки, старосты и т д)")
    start(message)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 
            """ Добро пожаловать в секцию киберспорта РНИМУ - CYBER RNM! Наша секция основывается на популярнейших дисциплинах киберспорта. Студенты имеют несколько опций присутствия в секции:
    
    1) Спорт высоких достижений - брось вызов сильнейшим студентам РНИМУ в своей дисциплине, выступай в сборной и защищай честь ВУЗа на крупных турнирах.

    2) Развитие и поддержка - если твой уровень не соответствует уровню сильнейшего состава , ты можешь начать свой путь во 2,3 или любом другом составе ,совершенствуя свой уровень на совместных тренировках + гайдах и обучениях.

    3) Обучения киберспорту - ты новичок и хочешь научиться новой дисциплине , мы готовы найти тебе коллектив со схожими целями. Вы будете проходить регулярные тренировки,на которых обучитесь азам игры и постепенно ,повышая свой уровень, совместно со всей командой. 

    4) Активист секции - тебе нравится киберспорт , но по тем или иным причинам,в данный момент ты не можешь играть в ту или иную дисциплину на высоком уровне или регулярно тренироваться. В нашей секции проходит множество мероприятий , на каждом из которых нужна светлая голова и руки.""")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Секции")
    item2 = types.KeyboardButton("FAQ")
    item3 = types.KeyboardButton("Список админов")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Что тебя интересует?", reply_markup=markup)



#Command /start
@bot.message_handler(commands=['main'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Секции")
    item2 = types.KeyboardButton("FAQ")
    item3 = types.KeyboardButton("Список админов")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Рандомный факт...", reply_markup=markup)

#Bottom 1
@bot.message_handler(func=lambda message: message.text == "FAQ")
def FAQ(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("В главное меню")
    markup.add(item1)
    bot.send_message(message.chat.id, """
Как получить зачёт по физкультуре?

Для того, чтобы получить зачёт по физкультуре нужно выполнить несколько условий

1) Если ты не соответствуешь составу сборной, первый семестр нужно тренироваться и активничать без зачёта, чтобы показать заинтересованность.

2)Распечатать заявление о переходе из академ.группы по физической культуре,получить подпись своего преподавателя и руководитель спортклуба.

3)Поставить подпись в табеле пребывающих в секции студентов.
            """, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "В главное меню")
def returning_to_main(message):
    main(message)


@bot.message_handler(func=lambda message: message.text == "Список админов")
def admins(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("В главное меню")
    markup.add(item1)
    bot.send_message(message.chat.id, "Список наших дорогих руководителей", reply_markup=markup)

@bot.message_handler(commands=['main'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Секции")
    item2 = types.KeyboardButton("FAQ")
    item3 = types.KeyboardButton("Список админов")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Привет!", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Секции")
def main_sections(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='CS GO 2', callback_data='cs_go_2')
    btn2 = types.InlineKeyboardButton(text='Heartstone', callback_data='heartstone')
    btn3 = types.InlineKeyboardButton(text='Raindbow Six Siege', callback_data='Raindbow_Six_Siege')
    btn4 = types.InlineKeyboardButton(text='Valorant', callback_data='valorant')
    btn5 = types.InlineKeyboardButton(text='League of legends', callback_data='LOL')
    btn6 = types.InlineKeyboardButton(text='MOBILE LEGENDS BANG BANG', callback_data='Mobile Legends')
    btn7 = types.InlineKeyboardButton(text='Apex Legends', callback_data='Apex')

    btn_back = types.InlineKeyboardButton(text='Назад', callback_data='назад')
    markup.add(btn1,btn2,btn3,btn4,btn5, btn6, btn7, btn_back)
    bot.send_photo(message.chat.id, open('cyberclub.jpg', 'rb'),
                       reply_markup=types.ReplyKeyboardRemove())
    #bot.send_message(message.chat.id, text="Окей, посмотрим...", reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id, 'Выбери секцию', reply_markup=markup)



@bot.callback_query_handler(func=lambda callback: callback.data)
def check_section(callback):
    if callback.data == 'cs_go_2':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='К списку секций', callback_data='Секции')
        btn2 = types.InlineKeyboardButton(text='В главное меню', callback_data='main_menu')
        kb.add(btn1,btn2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="""
Секция Counter Strike.
Одна из самых популярных секций в CYBER RNM.
Имеется несколько составов разного уровня игры.

RNIMU-1 8-10 уровень FAICET,подходит для ребят желающих попасть в киберспорт - капитан https://vk.com/nukleot1d

RNIMU-2 Состав состоит из игроков имеющих 13,000-18,000 рейтинга в CS 2 и от калаша с венками в СS:GO. Подойдёт игрокам выше любителей - капитан https://vk.com/drslyowl

RNIMU-3 Ребята играющие в своё удовольствие, ведут свои соц.сети и выкладывают хайлайты. подойдёт для игроков играющих на рейтинге до 12.000 и до калаша в CS:GO
Капитан https://vk.com/mqnwinner

RNIMU-4 Состав новичков , ребята отвечают за посты в соц.сетях, отметки на тренировках и за организацию внутривузовских мероприятий. Капитан https://vk.com/medic2004

                """, reply_markup=kb)

    if callback.data == 'Heartstone':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='К списку секций', callback_data='Секции')
        btn2 = types.InlineKeyboardButton(text='В главное меню', callback_data='main_menu')
        kb.add(btn1,btn2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="""
Секция Hearthstone.

Популярная карточная игра по мотивам серии Warcraft.
Cуществует два популярных режима Battlegrounds и Ladder. Среди сообщества врачей турниры по hearthstone имею особую ценность.
Капитан https://vk.com/lavrina_p 

                """, reply_markup=kb)

    if callback.data == 'Raindbow_Six_Siege':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='К списку секций', callback_data='Секции')
        btn2 = types.InlineKeyboardButton(text='В главное меню', callback_data='main_menu')
        kb.add(btn1,btn2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="""
Секция Rainbow Six Siege.

Одна из самых молодых секций в киберспорте. С тактической точки зрения самый интересный 3D-шутер в мире. Капитан ведёт активный набор в секцию.
Капитан - https://vk.com/lightweightbaabyy


                """, reply_markup=kb)

    if callback.data == 'valorant':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='К списку секций', callback_data='Секции')
        btn2 = types.InlineKeyboardButton(text='В главное меню', callback_data='main_menu')
        kb.add(btn1,btn2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="""
Секция Valorant.

Одна из самых молодых секций в киберспорте. Захватывающий тактический шутер, требующий от игроков меткую стрельбу, грамотное применение суперспособностей и слаженную командную игру для победы. Ведется активный набор агентов в Протокол VALORANT. Будущее за радиантами!
Капитан https://vk.com/drslyowl

                """, reply_markup=kb)
    if callback.data == 'LOL':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='К списку секций', callback_data='Секции')
        btn2 = types.InlineKeyboardButton(text='В главное меню', callback_data='main_menu')
        kb.add(btn1,btn2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="""Секция League of legends.
Одна из самых популярных моба игр на мировой арене.
Имеется несколько составов:

CRNM-1
Рейтинг: золото - грандмастер. Подойдёт для игроков, которые хотят добиться успеха в данной дисциплине и имеющих желание побеждать на турнирах.
Капитан команды: https://vk.com/within_reflection

CRNM-2
Команда новичков.
Подойдëт для людей, которые играют в своё удовольствие.
Капитан команды: https://vk.com/helldy_34""", reply_markup=kb)
    
    if callback.data == 'Mobile Legends':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='К списку секций', callback_data='Секции')
        btn2 = types.InlineKeyboardButton(text='В главное меню', callback_data='main_menu')
        kb.add(btn1,btn2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="""Секция MOBILE LEGENDS BANG BANG

Добродушная секция с приятной атмосферой в нашем общем чате😊
Имеется 3 состава, два из которых не уступают друг другу и настроенны играть серьёзно и на высоком уровне

erRorlinK [eror] первый состав который сформировался в нашей секции, тут играют ребята с большим опытом не только соло игры, а уже и с большим опытом игры в различных турнирах
Капитан https://vk.com/umarekawaruu

Aquarium [HOH] это молодой состав который постоянно развивается и уже сейчас является достойным соперником для eror, поэтому будет будет правильнее сказать что они вторые только лишь из-за того что сформировались позже
Капитан https://vk.com/hasan_po_snegu

И самый чиловый состав, где ребята просто отдыхают и не задумываются о турнирах, они наслаждаются компанией и игрой - Aurora legends [Aur], тут находятся резерв секции, многие ребята из этого состава готовы выйти на замену когда это надо
Капитан https://vk.com/tvoi_bog_id247985483""", reply_markup=kb)
        
    if callback.data == 'Apex':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='К списку секций', callback_data='Секции')
        btn2 = types.InlineKeyboardButton(text='В главное меню', callback_data='main_menu')
        kb.add(btn1,btn2)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="""Секция Apex Legends
Ведущий шутер в классическом понятии battle royale, не изменяющий своим истокам.
Ждём в нашем коллективе новых легенд.
Главный симулякр - https://vk.com/alwppp""", reply_markup=kb)
    

    if callback.data == 'Секции':
        #bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="Интересуешься чем-то ещё?", )
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='CS GO 2', callback_data='cs_go_2')
        btn2 = types.InlineKeyboardButton(text='Heartstone', callback_data='Heartstone')
        btn3 = types.InlineKeyboardButton(text='Raindbow Six Siege', callback_data='Raindbow_Six_Siege')
        btn4 = types.InlineKeyboardButton(text='Valorant', callback_data='valorant')
        btn5 = types.InlineKeyboardButton(text='League of legends', callback_data='LOL')
        btn6 = types.InlineKeyboardButton(text='MOBILE LEGENDS BANG BANG', callback_data='Mobile Legends')
        btn7 = types.InlineKeyboardButton(text='Apex Legends', callback_data='Apex')
        btn_back = types.InlineKeyboardButton(text='Назад', callback_data='назад')
        markup.add(btn1,btn2,btn3,btn4,btn5, btn6, btn7, btn_back)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="Выбери секцию", reply_markup=markup )
        bot.edit_message_media(chat_id=callback.message.chat.id, message_id=callback.message.id, media="cyberclub.jpg")

    if callback.data == 'main_menu' or callback.data == 'назад':
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text="Вернёмся к началу...", )
        main(callback.message)

#Start bot
if __name__ == '__main__':
    bot.polling(none_stop=True)
