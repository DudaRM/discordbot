import os

import discord
import sqlite3
from sqlite3 import Error
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

database_file = "botdatabase.db"

def create_connection(db_file):
    try:
        conn=sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

conn = create_connection(database_file)

def create_user(author):
    try:
        sql = 'INSERT INTO usuario(nome) VALUES(?)'
        cur = conn.cursor()
        cur.execute(sql,[str(author)])
        conn.commit()
        return cur.lastrowid

    except Error as e:
        print(e)

title = 'Bot agenda'
arg_missing_message = discord.Embed(title=title, description='Arguments are missing')
blue_color = discord.Color.blue()
gray_color = discord.Color.light_gray()
red_color = discord.Color.red()


@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content == ('botPlanner>addUser'):
        idUser = create_user(message.author)
        await message.channel.send(embed=(discord.Embed(title=title, description="Account created successfully your id is: "+str(idUser), color=blue_color)))
        return

client.run(TOKEN)