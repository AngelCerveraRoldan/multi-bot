## Interlan Imports
from src import wiki

## External Imports
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.command(name='search', help='Use this command to look something up in wikipedia.')
async def search(ctx, *sentence):
    ## If we added another argument between ctx and *sentence, then sentence would be the every word after the third. This allows us to have multiple arguments.

    sentence = " ".join(sentence)
    
    print(sentence)

    response = wiki.summary(sentence)
    await ctx.send(response)

bot.run(TOKEN)
