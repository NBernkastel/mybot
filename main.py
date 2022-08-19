import discord
import config
from discord import utils
from discord.utils import get
from discord.ext.commands import Bot
from youtube_dl import YoutubeDL
client = Bot(command_prefix=";;")
YDL_OPTIONS = {'format': 'worstaudio/best',
               'noplaylist': 'True', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("jojo"))

@client.command(pass_context=True)
async def play(ctx):
    print("work")
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(download=False,url = 'https://www.youtube.com/watch?v=2xQ3Aq1m6lk')
        URL = info['formats'][0]['url']
        voice.play(discord.FFmpegPCMAudio(URL))

client.run('OTk5NjQ0NzAxMzU3NTEwNzI2.GASCob.rCYo2YngMBB6E0SsGy6hmaGmy-Mma4O1_iOyPI')