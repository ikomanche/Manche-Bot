import discord

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
    
client.run('OTI0Mjg0NjYwNTE3ODM4OTI4.YccVKw.adQyW9jdPk4NBevEgKkT8YlxSns')