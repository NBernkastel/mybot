
import discord
import config
from discord import utils, RequestsWebhookAdapter
from discord.utils import get
from discord.ext.commands import Bot
from youtube_dl import YoutubeDL
from discord import Webhook
client = Bot(command_prefix='..')
client.remove_command("help")
YDL_OPTIONS = {'format': 'worstaudio/best',
               'noplaylist': 'True', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}
@client.command(pass_context=True)
async def play(ctx):
    print("work")
    global voice
    channel = ctx.message.author.voice.channel
    message = ctx.message
    cont = message.content.split(" ")
    print(cont)
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(download=False,url = cont[1])
        URL = info['formats'][0]['url']
        voice.play(discord.FFmpegPCMAudio(URL))
@client.command(pass_context=True)
async def stop(ctx):
    voice.stop()
    print("stoped")
@client.command(pass_context=True)
async def pause(ctx):
    voice.pause()
    print("paused")

@client.command(pass_context=True)
async def resume(ctx):
    voice.resume()
    print("resumed")
@client.command(pass_context=True)
async def help(ctx):
    webhook = Webhook.from_url(config.webhook,adapter=RequestsWebhookAdapter())
    embed = discord.Embed(colour = discord.colour.Color.red(),title= config.help,)
    webhook.send(embed=embed,username= "help")
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("jojo"))
    print("redy")
@client.event
async def on_message(message):
    if await client.process_commands(message) == False:
        print(message.content)
client.run('OTk5NjQ0NzAxMzU3NTEwNzI2.GIgRc_.MkETjYyMMCmTFDa6oqPV6OUc6lWREAx28hm-Ho')