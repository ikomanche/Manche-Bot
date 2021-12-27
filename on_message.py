import discord
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is now online and ready to roll.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'hele':
        await message.channel.send('heleĞğ')        
    
client.run(os.getenv("token"))