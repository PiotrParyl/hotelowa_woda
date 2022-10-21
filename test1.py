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

    mycursor.execute(f"SELECT * FROM woda WHERE DATE(date) >= (DATE(NOW()) - INTERVAL 10 DAY)")

    for chuj in mycursor:
        chuj_lista.append(chuj[1])

    wynik = chuj_lista[-1] - chuj_lista[0]

    return wynik



print(water_per_day())

print('kurwiszon')