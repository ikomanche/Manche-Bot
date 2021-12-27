import discord
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

"""
client = discord.Client()
@client.event
async def on_ready():
    print('Ready')
client.run('')
"""


# https://discordpy.readthedocs.io/en/latest/intents.html
# https://discord.com/developers/docs/topics/gateway#gateway-intents
# https://discord.com/developers/docs/topics/gateway#list-of-intents


class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 925072155891368016

    async def on_ready(self):
        print('Ready')

    async def on_raw_reaction_add(self, payload):
        """
        Give a role based on a reaction emoji
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        
        # print(payload.emoji.name)

        if payload.emoji.name == '🥔':
            role = discord.utils.get(guild.roles, name='Mancheler')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='Sekmeler')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🐒':
            role = discord.utils.get(guild.roles, name='Pipetler')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        """
        Remove a role based on a reaction emoji
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '🥔':
            role = discord.utils.get(guild.roles, name='Mancheler')
            await member.remove_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name='Sekmeler')
            await member.remove_roles(role)
        elif payload.emoji.name == '🐒':
            role = discord.utils.get(guild.roles, name='Pipetler')
            await member.remove_roles(role)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run(os.getenv("token"))