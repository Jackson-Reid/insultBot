"""
Title: Insult Bot
Author: Jackson Reid
Date Created:
"""
import os

import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
insults = (
    "You are as useless as the white crayon."
)

bot = commands.Bot(command_prefix='.')


@bot.command(name='insult')
async def insult(ctx, user: discord.Member):
    await ctx.send(f'From {user.mention}: {random.choice(insults)}')


bot.run(TOKEN)
