import discord
import config
from discord import utils, Webhook
from discord.utils import get
from discord.ext.commands import Bot
from youtube_dl import YoutubeDL
import asyncio
from time import sleep
client = Bot(command_prefix='..',intents=discord.Intents.all())
client.remove_command("help")
YDL_OPTIONS = {'format': 'worstaudio/best',
               'noplaylist': 'True', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
queue = []

async def q():
        global queue
        while len(queue) > 0:
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(download=False, url=queue[0])
                queue.pop(0)
                URL = info['formats'][0]['url']
                voice.play(discord.FFmpegPCMAudio(URL))
            await asyncio.sleep(info['duration'])

@client.command(pass_context=True)
async def play(ctx):
    global voice,queue
    channel = ctx.message.author.voice.channel
    message = ctx.message
    content = message.content.split(" ")
    queue.append(content[1])
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    if voice.is_playing():
        await ctx.message.reply("add to the q")
    else:
        await q()
@client.command(pass_context=True)
async def stop(ctx):
    voice.stop()
    print("stoped")
@client.command(pass_context=True)
async def lpl(ctx):
    print("lox")
@client.command(pass_context=True)
async def pause(ctx):
    voice.pause()
    print("paused")

@client.command(pass_context=True)
async def resume(ctx):
    voice.resume()
    print("resumed")
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("автор Nexeland"))
    print("redy")
@client.event
async def on_message(message):
    await client.process_commands(message)
      #  if message.author != client.user:
        #    await message.reply(message.content)
client.run('OTk5NjQ0NzAxMzU3NTEwNzI2.GIgRc_.MkETjYyMMCmTFDa6oqPV6OUc6lWREAx28hm-Ho')