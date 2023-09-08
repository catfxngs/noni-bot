import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

with open('config.json') as f:
    data = json.load(f)
    prefix = data["PREFIX"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)
