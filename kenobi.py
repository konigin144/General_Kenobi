import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from discord.utils import get
from asyncio import sleep

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
VC_TOKEN = os.getenv('VC_TOKEN')
TC_TOKEN = os.getenv('TC_TOKEN')

bot = commands.Bot(command_prefix='$')

async def af(vc):
    await vc.disconnect(force=True)

@bot.command()
async def test(ctx):
    print('xd')

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
    while vc.is_playing():
        await sleep(1)
    await vc.disconnect()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == int(VC_TOKEN):
            #channel = bot.get_channel(720005745369677906)
            #await channel.send('hello')
            #channel = member.message.author.voice.channel
            channelv = bot.get_channel(int(VC_TOKEN))
            vc = await channelv.connect()
            vc.play(discord.FFmpegPCMAudio(source="file.mp3"))
            while vc.is_playing():
                await sleep(1)
            await vc.disconnect()
        
bot.run(TOKEN)

#TODO: Error handling
#TODO: Find better sound
