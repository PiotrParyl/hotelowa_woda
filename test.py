from dataclasses import dataclass
import discord
from discord.ext import commands
from discord.ext.commands import bot
import time
import mysql.connector 
from datetime import datetime










#================================ Woda na godzine ================================ 
def water_use_h(x):
    values_list = []

    values = x * 12

    db = mysql.connector.connect(
    host='127.0.0.1',
    user='maczo420all',
    passwd='Pomidor13',
    database='metryka',
    )

    mycursor = db.cursor()
    mycursor.execute(f"SELECT value FROM woda ORDER BY ID DESC LIMIT {values}")

    for chuj in mycursor:
        siema = list(chuj)
        siema2 = list(siema[0])

        
        joined = "".join(siema2)

        values_list.append(joined)

    wynik = int(values_list[0]) - int(values_list[-1])    
        
    return values_list

print (water_use_h(1))
