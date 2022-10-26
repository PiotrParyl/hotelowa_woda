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
    

    db = mysql.connector.connect(
    host='127.0.0.1',
    user='maczo420all',
    passwd='Pomidor13',
    database='metryka',
    )


    mycursor = db.cursor()

    mycursor.execute(f"SELECT * FROM woda WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 7 DAY)")

    for chuj in mycursor:
        #print(chuj[1], chuj[2])

        chuj_lista.append(chuj[1])
    print (len(chuj_lista))


    for x in chuj_lista:
        print(x)
     

    _7_dni_temu = int(chuj_lista[288]) - int(chuj_lista[0])
    _6_dni_temu = int(chuj_lista[577]) - int(chuj_lista[289])
    _5_dni_temu = int(chuj_lista[866]) - int(chuj_lista[578])
    _4_dni_temu = int(chuj_lista[1155]) - int(chuj_lista[867])
    _3_dni_temu = int(chuj_lista[1444]) - int(chuj_lista[1156])
    _2_dni_temu = int(chuj_lista[1733]) - int(chuj_lista[1445])
    _1_dni_temu = int(chuj_lista[2022]) - int(chuj_lista[1734])

    print (f"1 dni temu: {_1_dni_temu} dm3 \n 2 dni temu: {_2_dni_temu} \n 3 dni temu: {_3_dni_temu} \n 4 dni temu: {_4_dni_temu} \n 5 dni temu: {_5_dni_temu} \n 6 dni temu: {_6_dni_temu} \n 7 dni temu: {_7_dni_temu}")


print(water_per_day())

print('kurwiszon')