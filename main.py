import discord, os, json, requests

from discord.ext import commands

DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
CLASH_TOKEN = os.environ["CLASH_TOKEN"]
bot = commands.Bot(command_prefix=[os.environ["PREFIX"]], intents=discod.Intents.default())

@bot.event
async def on_ready():
  print(f"Ready!")

@bot.event
async def on_message(message):
  await message.channel.send(f"👋")

@bot.command()
async def ping(message):
  async with bot.channel.typing():
    result = f"Pong! {round(bot.latency, 1)}"
  await message.channel.send(result)

try:
  bot.run(DISCORD_TOKEN)
except Exception as e:
  print(f"Error when logging in: {e}")


utils.Alive()
