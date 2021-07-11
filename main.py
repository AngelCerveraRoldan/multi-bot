## Interlan Imports
from src import wiki
from src import command_manager

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

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    call, text = command_manager.change(message.content)
    
    print(f'CALL HERE: {call}')
    print(f'TEXT HERE: {text}')

    if call == '$s':
        response = wiki.summary(text)

        await message.channel.send(response)


client.run(TOKEN)
