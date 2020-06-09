import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from discord.utils import get

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
VC_TOKEN = os.getenv('VC_TOKEN')
TC_TOKEN = os.getenv('TC_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx):
    print('xd')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == VC_TOKEN:
            print(member)
            channel = bot.get_channel(TC_TOKEN)
            await channel.send('hello')
            #channel = member.message.author.voice.channel
            channelv = bot.get_channel(162681501203300353)
            vc = await channelv.connect()
            vc.play(discord.FFmpegPCMAudio(source="file.mp3"))
            #TODO: Disconnect

@bot.command(pass_context=True)
async def join(ctx):
    print('elo')
    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(pass_context=True) #TODO: Make working when user joins after bot
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()

@bot.command()
async def play(ctx):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio(source="file.mp3"))

bot.run(TOKEN)

#TODO: Error handling
#TODO: Find better sound
