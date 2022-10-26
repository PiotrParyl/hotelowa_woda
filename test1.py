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

    mycursor.execute(f"SELECT * FROM woda WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 1 DAY)")

    for chuj in mycursor:
        print(chuj[1], chuj[2])

        chuj_lista.append(chuj[1])
    print (len(chuj_lista))

    siurek = chuj_lista[-288] - chuj_lista[-1]

    print (f"Wczoraj zuzyto: {siurek} dm3")


print(water_per_day())

print('kurwiszon')