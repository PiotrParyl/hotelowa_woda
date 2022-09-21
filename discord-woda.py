from token import token
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
        
    return wynik


#================================  Woda dzisiaj ================================
def woda_dzisiaj():
    now = datetime.now()
    current_time = now.strftime("%H")
    current_time = int(current_time)
    wynik = water_use_h(current_time)
    
    return wynik



def wczoraj_itd(x):
    now = datetime.now()
    current_time = now.strftime("%H")
    current_time = int(current_time)
    zmienna = current_time + (x * 24)
    chuj = water_use_h(zmienna)
    chuj2 = chuj - water_use_h(current_time)
    return chuj2

def kurwa_mac():
    return 'kurwa mac'



#================================ Discord ================================



token_chuj = token 
intents = discord.Intents.all()

client = commands.Bot(command_prefix='!',intents=intents)

@client.command(pass_context=True)
async def r(ctx):
    channel = client.get_channel(1021783221475754057)
    await channel.send(f"=== Zużycie Wody === \n Dzisiaj: {woda_dzisiaj()} \n Wczoraj: Not jet \n 2-dni: Not jet \n 3-dni: Not jet \n 4-dni: Not jet \n 5-dni: Not jet \n 6-dni: Not jet \n ")



@client.command(pass_context=True)
async def kurwa(ctx):
    channel = client.get_channel(1017555311365722246)
    await channel.send('test')

client.run(token_chuj)
