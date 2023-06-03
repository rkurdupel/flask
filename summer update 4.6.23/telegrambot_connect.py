import telebot
from telebot import types
import sqlite3
from settings import *
import time

token = "5955004061:AAF6RFnFHYVW-Fvi3zdsgtTYFTxkvVHNLUQ"
chat_id = "463312066"
bot = telebot.TeleBot(token = token)

@bot.message_handler(commands = ["start"])

def start(message):
    bot.send_message(message.chat.id, text = "Welcome to Roman's Coffee House !\nNew orders will appear here")
    print(message.chat.id)

print(PATH_INSTANCE + "coffee_house.db")

@bot.message_handler()

def receive_order():
    conn = sqlite3.connect(PATH_INSTANCE + "coffee_house.db")
    cursor = conn.cursor()

    list_of_all_orders = []
    cursor.execute('''SELECT * FROM receive_order''')

    data = cursor.fetchall()
    print(data)

    #order_id = 0
    for order in data:
        #print(order)
        order_id = order[0]
        #print(order_id)

        if order_id in list_of_all_orders:
            print(1)
            # list_of_all_orders.append(order_id) # add order id to the list so it won't repeat
            #print(list_of_all_orders)
        else:
            print(5)
            
            list_of_all_orders.append(order_id) # add order id to the list so it won't repeat
            #list_of_all_orders.append(order_id) # add order id to the list so it won't repeat
            
            order_details = f"               NEW ORDER | {order[0]} |\n---------------------------------------\n\nOrder details:\n\n{order[8]}                                               ${order[7]} total\n\nCustomer info:\n\n{order[1]}\n{order[2]}\n{order[3]}\n{order[4]}\n{order[5]}\n{order[6]}\n\n---------------------------------------"   
            bot.send_message(chat_id, order_details)

           
            

       

while True:
    receive_order()
    time.sleep(1)   # set delay for few seconds
    bot.infinity_polling()  # launch the bot



   


# scripts runs together with flask, another terminal