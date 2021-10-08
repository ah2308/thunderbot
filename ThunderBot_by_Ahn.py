import asyncio
from asyncio.exceptions import SendfileNotAvailableError
from types import CellType
import discord, datetime, pytz
from discord import channel
from discord import reaction
from discord import embeds
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("실행준비 완료")
    game = discord.Game("ThunderBot_1.1V")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    
    if message.content.startswith("!쿠크리허설"):
        await message.channel.send("@everyone")
        embed = discord.Embed(title="쿠크세이튼 리허설 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name=message.content[7:], value="참여를 원하시면 아래 👍이모지를 눌러주세요", inline=False)
        embed.set_footer(text="ThunderBot by. 안태훈")
        msg = await message.channel.send(embed=embed)
        channel = message.channel
        await msg.add_reaction("👍")

    if message.content.startswith("!아브데자뷰"):
        await message.channel.send("@everyone")
        embed = discord.Embed(title="아브렐슈드 데자뷰 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name=message.content[7:], value="참여를 원하시면 아래 👍이모지를 눌러주세요", inline=False)
        embed.set_footer(text="ThunderBot by. 안태훈")
        msg = await message.channel.send(embed=embed)
        channel = message.channel
        await msg.add_reaction("👍")

    if message.content.startswith("!비아노말"):
        await message.channel.send("@everyone")
        embed = discord.Embed(title="비아키스 노말 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name=message.content[6:], value="참여를 원하시면 아래 👍이모지를 눌러주세요", inline=False)
        embed.set_footer(text="ThunderBot by. 안태훈")
        msg = await message.channel.send(embed=embed)
        channel = message.channel
        await msg.add_reaction("👍")

    if message.content.startswith("!비아하드"):
        await message.channel.send("@everyone")
        embed = discord.Embed(title="비아키스 하드 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name=message.content[6:], value="참여를 원하시면 아래 👍이모지를 눌러주세요", inline=False)
        embed.set_footer(text="ThunderBot by. 안태훈")
        msg = await message.channel.send(embed=embed)
        channel = message.channel
        await msg.add_reaction("👍")

    if message.content.startswith("!발탄노말"):
        await message.channel.send("@everyone")
        embed = discord.Embed(title="발탄 노말 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name=message.content[6:], value="참여를 원하시면 아래 👍이모지를 눌러주세요", inline=False)
        embed.set_footer(text="ThunderBot by. 안태훈")
        msg = await message.channel.send(embed=embed)
        channel = message.channel
        await msg.add_reaction("👍")

    if message.content.startswith("!발탄하드"):
        await message.channel.send("@everyone")
        embed = discord.Embed(title="발탄 하드 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name=message.content[6:], value="참여를 원하시면 아래 👍이모지를 눌러주세요", inline=False)
        embed.set_footer(text="ThunderBot by. 안태훈")
        msg = await message.channel.send(embed=embed)
        channel = message.channel
        await msg.add_reaction("👍")

    if message.content.startswith("!아브노말"):
        await message.channel.send("@everyone")
        embed = discord.Embed(title="아브렐슈드 노말 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name=message.content[6:], value="참여를 원하시면 아래 👍이모지를 눌러주세요", inline=False)
        embed.set_footer(text="ThunderBot by. 안태훈")
        msg = await message.channel.send(embed=embed)
        channel = message.channel
        await msg.add_reaction("👍")
        
    if message.content.startswith("!아브하드"):
        await message.channel.send("@everyone")
        embed = discord.Embed(title="아브렐슈드 하드 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name=message.content[6:], value="참여를 원하시면 아래 👍이모지를 눌러주세요", inline=False)
        embed.set_footer(text="ThunderBot by. 안태훈")
        msg = await message.channel.send(embed=embed)
        channel = message.channel
        await msg.add_reaction("👍")

@client.event
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇이면 패스
        return None
    if str(reaction.emoji) == "👍":
        await reaction.message.channel.send("💬"+ user.name + "님이(가) 참여를 희망합니다")

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
