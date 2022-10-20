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

    db = mysql.connector.connect(
    host='127.0.0.1',
    user='maczo420all',
    passwd='Pomidor13',
    database='metryka',
    )


    mycursor = db.cursor()

    mycursor.execute(f"SELECT * FROM woda WHERE date BETWEEN '2022-10-19 00:00:00' AND '2022-10-19 23:59:59'")

    for chuj in mycursor:
        print(chuj)



water_per_day()

print('kurwiszon')