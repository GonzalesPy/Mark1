import discord

client = discord.Client()

@client.async_event
def on_ready():
	