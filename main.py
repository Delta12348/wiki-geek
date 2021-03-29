import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
@client.event
async def on_ready(): 
  print("We have logged in as {0.user}".format(client))

bot = commands.Bot(command_prefix="$")

@bot.command()
async def test(ctx, arg): 
  await ctx.send(arg)

@client.event
async def on_message(message):
  if message.author == client.user: 
    return
  if message.content.startswith("$hello"):
    await message.channel.send("Hello!")

client.run(os.getenv("TOKEN"))