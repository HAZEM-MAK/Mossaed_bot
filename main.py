# -*- coding: UTF8 -*-
# import requests
# import datetime
# import telegram
import json
import logging
import os
# import telegram.ext
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters,CallbackQueryHandler
from telegram import user,chat,Message,InlineKeyboardButton, InlineKeyboardMarkup ,keyboardbutton,replykeyboardmarkup

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

updater = Updater(token="1561974518:AAG79pjtHd2-dSCMMDKqIu8HG7GTUBRJEd8")
# PORT = int(os.environ.get('PORT', '3000'))
# bot = telegram.Bot(token="1561974518:AAG79pjtHd2-dSCMMDKqIu8HG7GTUBRJEd8")

# class BotHandler:
#     def __init__(self, token):
#             self.token = token
#             self.api_url = "https://api.telegram.org/bot{}/".format(token)
#
#     #url = "https://api.telegram.org/bot<token>/"
#
#     def get_updates(self, offset=0, timeout=30):
#         method = 'getUpdates'
#         params = {'timeout': timeout, 'offset': offset}
#         resp = requests.get(self.api_url + method, params)
#         result_json = resp.json()['result']
#         return result_json
#
#     def send_message(self, chat_id, text):
#         params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
#         method = 'sendMessage'
#         resp = requests.post(self.api_url + method, params)
#         return resp
#
#     def get_first_update(self):
#         get_result = self.get_updates()
#
#         if len(get_result) > 0:
#             last_update = get_result[0]
#         else:
#             last_update = None
#
#         return last_update
#

# token = '1561974518:AAG79pjtHd2-dSCMMDKqIu8HG7GTUBRJEd8' #Token of your bot
# magnito_bot = BotHandler(token) #Your bot's name

screennum=0
def menu(bot,update):
    """Echo the user message."""
    # bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    global screennum
    users =['hazem','mohammed']
    first_chat_id=update.message.chat_id
    first_chat_text=update.message.text
    first_chat_name="  "
    # if screennum == 0:  # [["ادخل الرمز لتفعيل المنتج"], ["حول"]]
    #     if first_chat_text == 'ادخل الرمز لتفعيل المنتج':
    #         json_keyboard = json.dumps({'keyboard': [["اطلس لإإدارة المشروعات الصغيرة"], ["مساعدة"],["رجوع"]],
    #                                        'one_time_keyboard': False,
    #                                        'resize_keyboard': True})
    #         bot.send_message(first_chat_id,
    #                            text='اختر المنتج الذي تود تفعيله عزيزي ' + first_chat_name,
    #                            reply_markup=json_keyboard)
    #         screennum=1
    #     else:
    #         json_keyboard = json.dumps({'keyboard': [["ادخل الرمز لتفعيل المنتج"], ["حول"]],
    #                                             'one_time_keyboard': False,
    #                                             'resize_keyboard': True})
    #         bot.send_message(first_chat_id,
    #                                  text= 'اهلا بك في خدمات مساعد سيد '+first_chat_name,
    #                                  reply_markup=json_keyboard)
    #
    # elif screennum == 1: #[["اطلس لإإدارة المشروعات الصغيرة"], ["مساعدة"],["رجوع"]]
    #     if first_chat_text == 'اطلس لإإدارة المشروعات الصغيرة':
    #         json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #                                             'one_time_keyboard': False,
    #                                             'resize_keyboard': True})
    #         bot.send_message(first_chat_id,
    #                                  text='قم بإدخال اسم المستخدم الذي قمت بالتسجيل به   ' ,
    #                                  reply_markup=json_keyboard)
    #         screennum=3
    #
    #     elif first_chat_text == 'مساعدة':
    #         bot.forwardMessage(first_chat_id, '373878314', '835')
    #     elif first_chat_text == 'رجوع':
    #         json_keyboard = json.dumps({'keyboard': [["ادخل الرمز لتفعيل المنتج"], ["حول"]],
    #                                            'one_time_keyboard': False,
    #                                            'resize_keyboard': True})
    #         bot.send_message(first_chat_id,
    #                                 text='اهلا بك في خدمات مساعد سيد ' + first_chat_name,
    #                                 reply_markup=json_keyboard)
    #         screennum = 0
    #
    # elif screennum == 3: #[["رجوع"]]
    #     if first_chat_text in users:
    #         json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #                                             'one_time_keyboard': False,
    #                                             'resize_keyboard': True})
    #         bot.send_message(first_chat_id,
    #                                  text='قم بإدخال الرمز الذي حصلت عليه من المنتج عزيزي  ' + first_chat_name,
    #                                  reply_markup=json_keyboard)
    #         screennum=4
    #     elif first_chat_text == 'رجوع':
    #         json_keyboard = json.dumps({'keyboard': [["ادخل الرمز لتفعيل المنتج"], ["حول"]],
    #                                             'one_time_keyboard': False,
    #                                             'resize_keyboard': True})
    #         bot.send_message(first_chat_id,
    #                                  text='اهلا بك في خدمات مساعد سيد ' + first_chat_name,
    #                                  reply_markup=json_keyboard)
    #         screennum = 0
    #     else :
    #         json_keyboard = json.dumps({'keyboard': [["المحاولة مرة اخرى"],["رجوع"]],
    #                                             'one_time_keyboard': False,
    #                                             'resize_keyboard': True})
    #         bot.send_message(first_chat_id,
    #                                  text='إن هذا الأسم غير مسجل يرجا  التأكد من صحة الإسم اوالمحاولة لاحقا '
    #                                  ,reply_markup=json_keyboard)
    #         screennum=5
    # elif screennum == 4:  # [["رجوع"]]
    #      if  first_chat_text.isnumeric() :
    #         json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #                              'one_time_keyboard': False,
    #                              'resize_keyboard': True})
    #         max=0
    #         print(first_chat_text)
    #         for x in first_chat_text:
    #             max+=(ord(x)-48)
    #         code=(max) * 2272511
    #         print(code)
    #         bot.send_message(first_chat_id,
    #                          text='رمز التفعيل الخاص بك هو ' ,
    #                          reply_markup=json_keyboard)
    #         bot.send_message(first_chat_id,
    #                          text= code)
    #         bot.send_message(first_chat_id,
    #                          text='شكرا لثقتك في منتجاتنا سيد '+ first_chat_name)
    #
    #      elif first_chat_text == 'رجوع':
    #         json_keyboard = json.dumps({'keyboard': [["ادخل الرمز لتفعيل المنتج"], ["حول"]],
    #                                      'one_time_keyboard': False,
    #                                      'resize_keyboard': True})
    #         bot.send_message(first_chat_id,
    #                           text='اهلا بك في خدمات مساعد سيد ' + first_chat_name,
    #                           reply_markup=json_keyboard)
    #         screennum = 0
    # elif screennum == 5:
    #      if first_chat_text == 'المحاولة مرة اخرى':
    #          json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #                                      'one_time_keyboard': False,
    #                                      'resize_keyboard': True})
    #          bot.send_message(first_chat_id,
    #                           text='قم بإدخال اسم المستخدم الذي قمت بالتسجيل به   ',
    #                           reply_markup=json_keyboard)
    #          screennum = 3
    #      elif first_chat_text == 'رجوع':
    #          json_keyboard = json.dumps({'keyboard': [["ادخل الرمز لتفعيل المنتج"], ["حول"]],
    #                                      'one_time_keyboard': False,
    #                                      'resize_keyboard': True})
    #          bot.send_message(first_chat_id,
    #                           text='اهلا بك في خدمات مساعد سيد ' + first_chat_name,
    #                           reply_markup=json_keyboard)
    #          screennum = 0
    #             #
    #             # if first_chat_text == 'Hi':
    #             #     magnito_bot.send_message(first_chat_id, 'Morning ' + first_chat_name)
    #             #     new_offset = first_update_id + 1
    #             # elif first_chat_text == 'ادخل الرمز لتفعيل المنتج':
    #             #     json_keyboard = json.dumps({'keyboard': [["اطلس لإإدارة المشروعات الصغيرة"], ["مساعدة"],["رجوع"]],
    #             #                                 'one_time_keyboard': False,
    #             #                                 'resize_keyboard': True})
    #             #     bot.send_message(first_chat_id,
    #             #                      text='اختر المنتج الذي تود تفعيله عزيزي ' + first_chat_name,
    #             #                      reply_markup=json_keyboard)
    #             #
    #             #     new_offset = first_update_id + 1
    #             #
    #             # elif first_chat_text == 'اطلس لإإدارة المشروعات الصغيرة':
    #             #     json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #             #                                 'one_time_keyboard': False,
    #             #                                 'resize_keyboard': True})
    #             #     bot.send_message(first_chat_id,
    #             #                      text='قم بإدخال الرمز الذي حصلت عليه من المنتج عزيزي  ' + first_chat_name,
    #             #                      reply_markup=json_keyboard)
    #             #     new_offset = first_update_id + 1
    #             # elif first_chat_text == 'مساعدة':
    #             #     json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #             #                                 'one_time_keyboard': False,
    #             #                                 'resize_keyboard': True})
    #             #     bot.forwardMessage(first_chat_id, '373878314', '835')
    #             #     new_offset = first_update_id + 1
    #             # elif  first_chat_text.isnumeric() :
    #             #     json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #             #                                 'one_time_keyboard': False,
    #             #                                 'resize_keyboard': True})
    #             #     max=0
    #             #     print(first_chat_text)
    #             #     for x in first_chat_text:
    #             #         max+=(ord(x)-48)
    #             #     code=(max+2) * 2272511;
    #             #     print(code)
    #             #     bot.send_message(first_chat_id,
    #             #                      text='رمز التفعيل الخاص بك هو ' ,
    #             #                      reply_markup=json_keyboard)
    #             #     bot.send_message(first_chat_id,
    #             #                      text= code)
    #             #     bot.send_message(first_chat_id,
    #             #                      text='شكرا لثقتك في منتجاتنا سيد '+ first_chat_name)
    #             #     new_offset = first_update_id + 1
    #             #
    #             # else:
    #             #     json_keyboard = json.dumps({'keyboard': [["ادخل الرمز لتفعيل المنتج"], ["حول"]],
    #             #                                 'one_time_keyboard': False,
    #             #                                 'resize_keyboard': True})
    #             #     bot.send_message(first_chat_id,
    #             #                      text= 'اهلا بك في خدمات مساعد سيد '+first_chat_name,
    #             #                      reply_markup=json_keyboard)
    #             #     new_offset = first_update_id + 1

    print(update.message.text)
    print(screennum)
def start(bot,update):
    """Echo the user message."""
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    print(update.message.text)
def error(bot,update):
    """Log Errors caused by Updates."""
    logger.warning('update "%s" caused error "%s"', bot, update.error)

def main():
    new_offset = 0
    screennum = 0

    print('hi, now launching...')
    updater.start_polling()
    # updater.idle()
    # while True:
    #     all_updates=magnito_bot.get_updates(new_offset)
    #
    #     if len(all_updates) > 0:
    #         for current_update in all_updates:
    #             print(current_update)
    #             first_update_id = current_update['update_id']
    #             if 'text' not in current_update['message']:
    #                 first_chat_text='New member'
    #             else:
    #                 first_chat_text = current_update['message']['text']
    #             first_chat_id = current_update['message']['chat']['id']
    #             if 'first_name' in current_update['message']:
    #                 first_chat_name = current_update['message']['chat']['first_name']
    #             elif 'new_chat_member' in current_update['message']:
    #                 first_chat_name = current_update['message']['new_chat_member']['username']
    #             elif 'from' in current_update['message']:
    #                 first_chat_name = current_update['message']['from']['first_name']
    #             else:
    #                 first_chat_name = "unknown"
    #
    #
    #
    #             if screennum == 0:#[["ادخل الرمز لتفعيل المنتج"], ["حول"]]
    #
    #                 if first_chat_text == 'ادخل الرمز لتفعيل المنتج':
    #                     json_keyboard = json.dumps({'keyboard': [["اطلس لإإدارة المشروعات الصغيرة"], ["مساعدة"],["رجوع"]],
    #                                                 'one_time_keyboard': False,
    #                                                 'resize_keyboard': True})
    #                     bot.send_message(first_chat_id,
    #                                      text='اختر المنتج الذي تود تفعيله عزيزي ' + first_chat_name,
    #                                      reply_markup=json_keyboard)
    #                     new_offset = first_update_id + 1
    #                     screennum=1
    #                 else:
    #                     json_keyboard = json.dumps({'keyboard': [["ادخل الرمز لتفعيل المنتج"], ["حول"]],
    #                                                 'one_time_keyboard': False,
    #                                                 'resize_keyboard': True})
    #                     bot.send_message(first_chat_id,
    #                                      text= 'اهلا بك في خدمات مساعد سيد '+first_chat_name,
    #                                      reply_markup=json_keyboard)
    #                     new_offset = first_update_id + 1
    #
    #             elif screennum == 1: #[["اطلس لإإدارة المشروعات الصغيرة"], ["مساعدة"],["رجوع"]]
    #
    #                 if first_chat_text == 'اطلس لإإدارة المشروعات الصغيرة':
    #                     json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #                                                 'one_time_keyboard': False,
    #                                                 'resize_keyboard': True})
    #                     bot.send_message(first_chat_id,
    #                                      text='قم بإدخال اسم المستخدم الذي قمت بالتسجيل به   ' ,
    #                                      reply_markup=json_keyboard)
    #                     new_offset = first_update_id + 1
    #                     screennum=3
    #
    #                 elif first_chat_text == 'مساعدة':
    #                     bot.forwardMessage(first_chat_id, '373878314', '835')
    #                     new_offset = first_update_id + 1
    #
    #                 elif first_chat_text == 'رجوع':
    #                     json_keyboard = json.dumps({'keyboard': [["ادخل الرمز لتفعيل المنتج"], ["حول"]],
    #                                                 'one_time_keyboard': False,
    #                                                 'resize_keyboard': True})
    #                     bot.send_message(first_chat_id,
    #                                      text='اهلا بك في خدمات مساعد سيد ' + first_chat_name,
    #                                      reply_markup=json_keyboard)
    #                     new_offset = first_update_id + 1
    #                     screennum = 0
    #
    #             elif screennum == 3: #[["رجوع"]]
    #                 if first_chat_text in users:
    #                     json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #                                                 'one_time_keyboard': False,
    #                                                 'resize_keyboard': True})
    #                     bot.send_message(first_chat_id,
    #                                      text='قم بإدخال الرمز الذي حصلت عليه من المنتج عزيزي  ' + first_chat_name,
    #                                      reply_markup=json_keyboard)
    #                     new_offset = first_update_id + 1
    #                     screennum=4
    #                 elif first_chat_text == 'رجوع':
    #                     json_keyboard = json.dumps({'keyboard': [["ادخل الرمز لتفعيل المنتج"], ["حول"]],
    #                                                 'one_time_keyboard': False,
    #                                                 'resize_keyboard': True})
    #                     bot.send_message(first_chat_id,
    #                                      text='اهلا بك في خدمات مساعد سيد ' + first_chat_name,
    #                                      reply_markup=json_keyboard)
    #                     new_offset = first_update_id + 1
    #                     screennum = 0
    #                 else :
    #                     json_keyboard = json.dumps({'keyboard': [["المحاولة مرة اخرى"],["رجوع"]],
    #                                                 'one_time_keyboard': False,
    #                                                 'resize_keyboard': True})
    #                     bot.send_message(first_chat_id,
    #                                      text='إن هذا الأسم غير مسجل يرجا  التأكد من صحة الإسم اوالمحاولة لاحقا '
    #                                      ,reply_markup=json_keyboard)
    #                     new_offset=first_update_id + 1
    #                     screennum=5
    #             elif screennum == 4:  # [["رجوع"]]
    #                 if  first_chat_text.isnumeric() :
    #                     json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #                                                 'one_time_keyboard': False,
    #                                                 'resize_keyboard': True})
    #                     max=0
    #                     print(first_chat_text)
    #                     for x in first_chat_text:
    #                         max+=(ord(x)-48)
    #                     code=(max+2) * 2272511
    #                     print(code)
    #                     bot.send_message(first_chat_id,
    #                                      text='رمز التفعيل الخاص بك هو ' ,
    #                                      reply_markup=json_keyboard)
    #                     bot.send_message(first_chat_id,
    #                                      text= code)
    #                     bot.send_message(first_chat_id,
    #                                      text='شكرا لثقتك في منتجاتنا سيد '+ first_chat_name)
    #                     new_offset = first_update_id + 1
    #                 elif first_chat_text == 'رجوع':
    #                     json_keyboard = json.dumps({'keyboard': [["ادخل الرمز لتفعيل المنتج"], ["حول"]],
    #                                                 'one_time_keyboard': False,
    #                                                 'resize_keyboard': True})
    #                     bot.send_message(first_chat_id,
    #                                      text='اهلا بك في خدمات مساعد سيد ' + first_chat_name,
    #                                      reply_markup=json_keyboard)
    #                     new_offset = first_update_id + 1
    #                     screennum = 0
    #             elif screennum == 5:
    #                 if first_chat_text == 'المحاولة مرة اخرى':
    #                     json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #                                                 'one_time_keyboard': False,
    #                                                 'resize_keyboard': True})
    #                     bot.send_message(first_chat_id,
    #                                      text='قم بإدخال اسم المستخدم الذي قمت بالتسجيل به   ',
    #                                      reply_markup=json_keyboard)
    #                     new_offset = first_update_id + 1
    #                     screennum = 3
    #                 elif first_chat_text == 'رجوع':
    #                     json_keyboard = json.dumps({'keyboard': [["ادخل الرمز لتفعيل المنتج"], ["حول"]],
    #                                                 'one_time_keyboard': False,
    #                                                 'resize_keyboard': True})
    #                     bot.send_message(first_chat_id,
    #                                      text='اهلا بك في خدمات مساعد سيد ' + first_chat_name,
    #                                      reply_markup=json_keyboard)
    #                     new_offset = first_update_id + 1
    #                     screennum = 0
    #             #
    #             # if first_chat_text == 'Hi':
    #             #     magnito_bot.send_message(first_chat_id, 'Morning ' + first_chat_name)
    #             #     new_offset = first_update_id + 1
    #             # elif first_chat_text == 'ادخل الرمز لتفعيل المنتج':
    #             #     json_keyboard = json.dumps({'keyboard': [["اطلس لإإدارة المشروعات الصغيرة"], ["مساعدة"],["رجوع"]],
    #             #                                 'one_time_keyboard': False,
    #             #                                 'resize_keyboard': True})
    #             #     bot.send_message(first_chat_id,
    #             #                      text='اختر المنتج الذي تود تفعيله عزيزي ' + first_chat_name,
    #             #                      reply_markup=json_keyboard)
    #             #
    #             #     new_offset = first_update_id + 1
    #             #
    #             # elif first_chat_text == 'اطلس لإإدارة المشروعات الصغيرة':
    #             #     json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #             #                                 'one_time_keyboard': False,
    #             #                                 'resize_keyboard': True})
    #             #     bot.send_message(first_chat_id,
    #             #                      text='قم بإدخال الرمز الذي حصلت عليه من المنتج عزيزي  ' + first_chat_name,
    #             #                      reply_markup=json_keyboard)
    #             #     new_offset = first_update_id + 1
    #             # elif first_chat_text == 'مساعدة':
    #             #     json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #             #                                 'one_time_keyboard': False,
    #             #                                 'resize_keyboard': True})
    #             #     bot.forwardMessage(first_chat_id, '373878314', '835')
    #             #     new_offset = first_update_id + 1
    #             # elif  first_chat_text.isnumeric() :
    #             #     json_keyboard = json.dumps({'keyboard': [["رجوع"]],
    #             #                                 'one_time_keyboard': False,
    #             #                                 'resize_keyboard': True})
    #             #     max=0
    #             #     print(first_chat_text)
    #             #     for x in first_chat_text:
    #             #         max+=(ord(x)-48)
    #             #     code=(max+2) * 2272511;
    #             #     print(code)
    #             #     bot.send_message(first_chat_id,
    #             #                      text='رمز التفعيل الخاص بك هو ' ,
    #             #                      reply_markup=json_keyboard)
    #             #     bot.send_message(first_chat_id,
    #             #                      text= code)
    #             #     bot.send_message(first_chat_id,
    #             #                      text='شكرا لثقتك في منتجاتنا سيد '+ first_chat_name)
    #             #     new_offset = first_update_id + 1
    #             #
    #             # else:
    #             #     json_keyboard = json.dumps({'keyboard': [["ادخل الرمز لتفعيل المنتج"], ["حول"]],
    #             #                                 'one_time_keyboard': False,
    #             #                                 'resize_keyboard': True})
    #             #     bot.send_message(first_chat_id,
    #             #                      text= 'اهلا بك في خدمات مساعد سيد '+first_chat_name,
    #             #                      reply_markup=json_keyboard)
    #             #     new_offset = first_update_id + 1
    #
    # updater.idle()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
PORT = os.getenv('PORT', default=8000)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, menu))
dp.add_handler(CommandHandler("start", start))
dp.add_error_handler(error)
updater.bot.setWebhook('https://cryptic-spire-59669.herokuapp.com/1561974518:AAG79pjtHd2-dSCMMDKqIu8HG7GTUBRJEd8')
updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path="1561974518:AAG79pjtHd2-dSCMMDKqIu8HG7GTUBRJEd8")
    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
# updater.bot.set_webhook("cryptic-spire-59669"+ "1561974518:AAG79pjtHd2-dSCMMDKqIu8HG7GTUBRJEd8")
