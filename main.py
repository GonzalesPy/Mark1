import statics as s
import discord
import random
import io
import requests
import asyncio

client = discord.Client()

minutes = 0
hours = 0


@client.event
async def on_ready():
	print ("------------------------")
	print("Ready to rumble :)")
	print("I was coded in Python")
	print("and my name is " + client.user.name + ".")
	print("------------------------")
	await client.change_presence(game=discord.Game(name="Python"))


@client.event
async def on_message(message):
#basics
	#online test
	if message.content.lower().startswith("m:test"):
		await client.send_message(message.channel, "Test succesfull")

	#change game
	if message.content.lower().startswith("m:game"):
		for keys in s.adminIDS:
			if s.adminIDS[keys] == message.author.id:
				game = message.content[6:]
				await client.change_presence(game=discord.Game(name=game))
				await client.send_message(message.channel, "I changed my game to'" + game + "'")

	#uptime
	if message.content.lower().startswith("m:uptime"):
		await client.send_message(message.channel, "I am {0} hour/s and {1} minutes online on the server {2}.".format(hours, minutes, message.server))

#moderation

#fun
	#random reaction
	if message.content.lower().startswith("m:reaction"):
		choice = random.randint(0, len(s.emojis)-1)
		await client.add_reaction(message, s.emojis[choice])

	#post pictures/gifs
	if message.content.lower().startswith("m:picture"):
		choice = random.randint(0, len(s.urls)-1)
		response = requests.get(s.urls[choice], stream = True)
		await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='Picture.gif', content="Wow there is a PICTURE!")

	#random gifs
	if message.content.lower().startswith("m:gif"):
		gif_tag = message.content[6:]
		rgif = s.g.random(tag=str(gif_tag))
		response = requests.get(str(rgif.get('data', {}).get("image_original_url")),stream = True)
		await client.send_file (message.channel, io.BytesIO(response.raw.read ()), filename='GIF.gif',content="Wow there is a GIF!")

#basics
#leave/jon message
@client.event
async def on_member_join(member):
	server = client.get_server("431145382110691332")
	channel = server.get_channel("431145382110691334")
	msg = "Welcome {0} to {1} please read the rules!".format(member.mention, member.server.name)
	await client.send_message(channel, msg)

@client.event
async def on_member_remove(member):
	print("done1")
	server = client.get_server("431145382110691332")
	channel = server.get_channel("431145382110691334")
	msg = "Bye {0} I hope you had fun! :(".format(member.name)
	await client.send_message(channel, msg)
	print("done1")

async def uptime():
	await client.wait_until_ready()
	global minutes
	minutes = 0
	global hours
	hours = 0
	while not client.is_closed:
		await asyncio.sleep(60)
		minutes += 1
		if minutes == 60:
			minutes = 0
			hours += 1

client.loop.create_task(uptime())
client.run("")

