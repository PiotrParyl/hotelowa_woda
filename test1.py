import os
from dotenv import load_dotenv
from dataclasses import dataclass
import discord
from discord.ext import commands
from discord.ext.commands import bot
import time
import mysql.connector 
from datetime import datetime


def water_per_day():
     
    chuj_lista = []

    dzien7 = []
    dzien6 = []
    dzien5 = []
    dzien4 = []
    dzien3 = []
    dzien2 = []
    dzien1 = []
    

    db = mysql.connector.connect(
    host='127.0.0.1',
    user='maczo420all',
    passwd='Pomidor13',
    database='metryka',
    )


    mycursor = db.cursor()

    # Dzeien 7

    mycursor.execute(f"SELECT * FROM woda WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 7 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien7.append(chuj[1])


    # Dzeien 6

    mycursor.execute(f"SELECT * FROM woda WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 6 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien6.append(chuj[1])


    # Dzeien 5

    mycursor.execute(f"SELECT * FROM woda WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 5 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien5.append(chuj[1])


    # Dzeien 4
    mycursor.execute(f"SELECT * FROM woda WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 4 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien4.append(chuj[1])


    # Dzeien 3
    mycursor.execute(f"SELECT * FROM woda WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 3 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien3.append(chuj[1])


    # Dzeien 2
    mycursor.execute(f"SELECT * FROM woda WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 2 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien2.append(chuj[1])


    # Dzeien 1

    mycursor.execute(f"SELECT * FROM woda WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 1 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien1.append(chuj[1])


    for x in chuj_lista:
        print(x)
     

    _7_dni_temu = int(dzien7[287]) - int(dzien7[0])
    _6_dni_temu = int(dzien6[287]) - int(dzien6[0])
    _5_dni_temu = int(dzien5[287]) - int(dzien5[0])
    _4_dni_temu = int(dzien4[287]) - int(dzien4[0])
    _3_dni_temu = int(dzien3[287]) - int(dzien3[0])
    _2_dni_temu = int(dzien2[287]) - int(dzien2[0])
    _1_dni_temu = int(dzien1[287]) - int(dzien1[0])

    #print (f" 1 dni temu: {_1_dni_temu} dm3 \n 2 dni temu: {_2_dni_temu} \n 3 dni temu: {_3_dni_temu} \n 4 dni temu: {_4_dni_temu} \n 5 dni temu: {_5_dni_temu} \n 6 dni temu: {_6_dni_temu} \n 7 dni temu: {_7_dni_temu}")

    return {
    'dzien1':_1_dni_temu,
    'dzien2':_2_dni_temu,
    'dzien3':_3_dni_temu,
    'dzien4':_4_dni_temu,
    'dzien5':_5_dni_temu,
    'dzien6':_6_dni_temu,
    'dzien7' :_7_dni_temu}



def pump_per_day():
     
    chuj_lista = []

    dzien7 = []
    dzien6 = []
    dzien5 = []
    dzien4 = []
    dzien3 = []
    dzien2 = []
    dzien1 = []
    

    db = mysql.connector.connect(
    host='127.0.0.1',
    user='maczo420all',
    passwd='Pomidor13',
    database='metryka',
    )


    mycursor = db.cursor()

    # Dzeien 7

    mycursor.execute(f"SELECT * FROM pompa WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 7 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien7.append(chuj[1])


    # Dzeien 6

    mycursor.execute(f"SELECT * FROM pompa WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 6 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien6.append(chuj[1])


    # Dzeien 5

    mycursor.execute(f"SELECT * FROM pompa WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 5 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien5.append(chuj[1])


    # Dzeien 4
    mycursor.execute(f"SELECT * FROM pompa WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 4 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien4.append(chuj[1])


    # Dzeien 3
    mycursor.execute(f"SELECT * FROM pompa WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 3 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien3.append(chuj[1])


    # Dzeien 2
    mycursor.execute(f"SELECT * FROM pompa WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 2 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien2.append(chuj[1])


    # Dzeien 1

    mycursor.execute(f"SELECT * FROM pompa WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 1 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        dzien1.append(chuj[1])


    for x in chuj_lista:
        print(x)
     

    _7_dni_temu = float(dzien7[287]) - float(dzien7[0])
    _6_dni_temu = float(dzien6[287]) - float(dzien6[0])
    _5_dni_temu = float(dzien5[287]) - float(dzien5[0])
    _4_dni_temu = float(dzien4[287]) - float(dzien4[0])
    _3_dni_temu = float(dzien3[287]) - float(dzien3[0])
    _2_dni_temu = float(dzien2[287]) - float(dzien2[0])
    _1_dni_temu = float(dzien1[287]) - float(dzien1[0])

    #print (f" 1 dni temu: {_1_dni_temu} dm3 \n 2 dni temu: {_2_dni_temu} \n 3 dni temu: {_3_dni_temu} \n 4 dni temu: {_4_dni_temu} \n 5 dni temu: {_5_dni_temu} \n 6 dni temu: {_6_dni_temu} \n 7 dni temu: {_7_dni_temu}")

    return {
    'dzien1':_1_dni_temu,
    'dzien2':_2_dni_temu,
    'dzien3':_3_dni_temu,
    'dzien4':_4_dni_temu,
    'dzien5':_5_dni_temu,
    'dzien6':_6_dni_temu,
    'dzien7' :_7_dni_temu}