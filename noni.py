import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json

# Loads .env file if it exists
load_dotenv()

# Pulls token from said .env file
TOKEN = os.getenv("DISCORD_TOKEN")

with open('config.json') as f:
    data = json.load(f)
    prefix = data["PREFIX"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print('Bot is online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Checks for existing .env with bot token
try:
    f = open('.env')
    f.close()
# If .env doesn't exist, asks user for token
except FileNotFoundError:
    TOKEN = input("Paste your bot's token: ")
    # If user saves token, .env is created and ignored by git
    if input("Remember token? Y/n: ") == "Y" or "y":
        open(".env","w+").write(f"DISCORD_TOKEN={TOKEN}")
    else:
        print("Token not saved.")

# Bot starts
client.run(TOKEN)
