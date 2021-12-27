import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Online')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'cool' and message.author != client.user:
        await message.add_reaction('\U0001F60E')


@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )


@client.event
async def on_reaction_add(reaction, user):
    if user != client.user:
        await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


client.run('OTI0Mjg0NjYwNTE3ODM4OTI4.YccVKw.adQyW9jdPk4NBevEgKkT8YlxSns')