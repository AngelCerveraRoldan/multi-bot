## Interlan Imports
from src import wiki
from src import images

## External Imports
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

## Bot setup

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

bot = commands.Bot(
    command_prefix = commands.when_mentioned_or('$'),
    description = 'We pretty much all think that Kingsley is reasonably good looking.',
    help_command = help_command
)

## COMMANDS

## Search Commands
@bot.command(name='what', help='Use this command to get a 2 sentence summary of a topic.')
async def search(ctx, *sentence):
    ## If we added another argument between ctx and *sentence, then sentence would be the every word after the third. This allows us to have multiple arguments.
    sentence = " ".join(sentence)
    
    await ctx.send('Searching...')

    response = wiki.summary(sentence)
    await ctx.send(response)

@bot.command(name='search', help='Use this command to look something up in wikipedia.')
async def search(ctx, *sentence):
    sentence = " ".join(sentence)
    
    await ctx.send('Searching...')

    response = wiki.search(sentence)
    await ctx.send(response)

    await ctx.delete_message(ctx.message)

@bot.command(name='image', help='Find an image of something.')
async def image(ctx, *sentence):   
    sentence = ' '.join(sentence)
    
    image_list = images.get_photo(sentence)
    
    await ctx.send(image_list)



bot.run(TOKEN)
