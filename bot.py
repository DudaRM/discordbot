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



@client.event
async def on_ready():
    print(conn)
    #print(f'{client.user} has connected to Discord!')

client.run(TOKEN)