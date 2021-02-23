import datetime
import re
import discord
from discord.ext import tasks, commands

client = commands.Bot(command_prefix='+')

client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('prefix -> +'))
    print("Ready")

@client.command()
async def help(ctx):
	await ctx.send("```+join ctfname\n+clear amount```")


@client.command()
async def join(ctx, channelname):
	if str(ctx.channel) == "joinctf":
		channel = discord.utils.get(ctx.guild.text_channels, name=channelname)
		await ctx.message.add_reaction('✅')
		await channel.set_permissions(ctx.message.author, read_messages=True, send_messages=True, read_message_history=True, add_reactions=True)
	else:
		await ctx.send("```use this in joinctf channel please !```")

@client.command()
async def clear(ctx, amt=5):
	if str(ctx.message.author) == "MillenniumX#2624":
		await ctx.channel.purge(limit=amt)


client.run("token")