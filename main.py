## Interlan Imports
from src import wiki

## External Imports
import os
import discord
from dotenv import load_dotenv

## Discord Bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

## This will print when the bot is ready to be used
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
