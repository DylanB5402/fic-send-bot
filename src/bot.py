import discord
from discord import app_commands
from discord.ext import commands
import config


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.tree.command()
@commands.dm_only()
async def sendfic(interaction : discord.Interaction, url : str):
    await interaction.response.send_message(f'hello world! url is {url}')

@client.tree.command(name='sync', description='Owner only')
@commands.dm_only()
async def sync(interaction: discord.Interaction):
    if interaction.user.id == 282647338793566219:
        await client.tree.sync()
        print('Command tree synced.')
        await interaction.response.send_message('You are synced')
    else:
        await interaction.response.send_message('You must be the owner to use this command!')

client.run(config.bot_token)