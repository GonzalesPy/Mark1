import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print("Ready to rumble :)")
	print("I was coded in Python.")
	print("My name is: " + client.user.name + ".")
	print("--------------")


@client.event
async def on_message(message):
	if message.content.lower().startswith("m:test"):
		await client.send_message(message.channel, "Test succesfull")





client.run("NDMxODM5NDcwMDMyMTI1OTUy.Daodow.DhsArTpPuP1LWEOZwzz4tblI_jA")

