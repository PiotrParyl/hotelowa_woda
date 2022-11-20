import os
from dotenv import load_dotenv
from dataclasses import dataclass
import discord
from discord.ext import commands
from discord.ext.commands import bot
import time
import mysql.connector 
from datetime import datetime
from test1 import *




load_dotenv()










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

def stan_licznika():

    values_list = []

    db = mysql.connector.connect(
    host='127.0.0.1',
    user='maczo420all',
    passwd='Pomidor13',
    database='metryka',
    )

    mycursor = db.cursor()
    mycursor.execute(f"SELECT value FROM woda ORDER BY ID DESC LIMIT 1")

    for chuj in mycursor:
        siema = list(chuj)
        siema2 = list(siema[0])

        
        joined = "".join(siema2)

        values_list.append(joined)
    
    return values_list[0]



    



#================================ Discord ================================



token_chuj = os.getenv('token') 
intents = discord.Intents.all()

client = commands.Bot(command_prefix='!',intents=intents)


@client.command(pass_context=True)
async def h(ctx):
    channel = client.get_channel(1021783221475754057)
    await channel.send(f"=== Help === \n !w - Zużycie wody \n !ws - Aktualny stan licznika \n !p - Zużycie pompy ")


@client.command(pass_context=True)
async def ws(ctx):
    channel = client.get_channel(1021783221475754057)
    await channel.send(f"Aktualny stan licznika - {stan_licznika()}")



@client.command(pass_context=True)
async def w(ctx):
    channel = client.get_channel(1021783221475754057)
    await channel.send(f"=== Zużycie Wody === \n Dzisiaj: {woda_dzisiaj()} \n Wczoraj: {water_per_day()['dzien1']}  \n 2-dni: {water_per_day()['dzien2']} \n 3-dni: {water_per_day()['dzien3']} \n 4-dni: {water_per_day()['dzien4']} \n 5-dni: {water_per_day()['dzien5']} \n 6-dni: {water_per_day()['dzien6']} \n ")

@client.command(pass_context=True)
async def p(ctx):
    channel = client.get_channel(1021783221475754057)
    await channel.send(f"=== Zużycie Pompy === \n Dzisiaj: error420 \n Wczoraj: {pump_per_day()['dzien1']}  \n 2-dni: {pump_per_day()['dzien2']} \n 3-dni: {pump_per_day()['dzien3']} \n 4-dni: {pump_per_day()['dzien4']} \n 5-dni: {pump_per_day()['dzien5']} \n 6-dni: {pump_per_day()['dzien6']} \n ")




@client.command(pass_context=True)
async def kurwa(ctx):
    channel = client.get_channel(1017555311365722246)
    await channel.send('test')

client.run(token_chuj)
