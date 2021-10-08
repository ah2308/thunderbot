import asyncio
from asyncio.exceptions import SendfileNotAvailableError
from types import CellType
import discord, datetime, pytz
from discord import channel
from discord import reaction
from discord import embeds
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("실행준비 완료")
    game = discord.Game("ThunderBot 1.1V")
    await client.change_presence(status=discord.Status.online, activity=game)

@bot.command(pass_context=True)
async def 발탄노말(ctx, context) :
    await ctx.channel.send("@here")
    embed = discord.Embed(title = "발탄 노말 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffbbc6)
    embed.add_field(name = f"모집자 : {ctx.message.author.name}", value = f"출발일정 : {context}")
    embed.set_footer(text="ThunderBot by. 안태훈")
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def 발탄하드(ctx, context) :
    await ctx.channel.send("@here")
    embed = discord.Embed(title = "발탄 하드 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffbbc6)
    embed.add_field(name = f"모집자 : {ctx.message.author.name}", value = f"출발일정 : {context}")
    embed.set_footer(text="ThunderBot by. 안태훈")
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def 비아노말(ctx, context) :
    await ctx.channel.send("@here")
    embed = discord.Embed(title = "비아키스 노말 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffbbc6)
    embed.add_field(name = f"모집자 : {ctx.message.author.name}", value = f"출발일정 : {context}")
    embed.set_footer(text="ThunderBot by. 안태훈")
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def 비아하드(ctx, context) :
    await ctx.channel.send("@here")
    embed = discord.Embed(title = "비아키스 하드 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffbbc6)
    embed.add_field(name = f"모집자 : {ctx.message.author.name}", value = f"출발일정 : {context}")
    embed.set_footer(text="ThunderBot by. 안태훈")
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def 아브노말(ctx, context) :
    await ctx.channel.send("@here")
    embed = discord.Embed(title = "아브렐슈드 노말 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffbbc6)
    embed.add_field(name = f"모집자 : {ctx.message.author.name}", value = f"출발일정 : {context}")
    embed.set_footer(text="ThunderBot by. 안태훈")
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def 아브하드(ctx, context) :
    await ctx.channel.send("@here")
    embed = discord.Embed(title = "아브렐슈드 하드 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffbbc6)
    embed.add_field(name = f"모집자 : {ctx.message.author.name}", value = f"출발일정 : {context}")
    embed.set_footer(text="ThunderBot by. 안태훈")
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def 쿠크리허설(ctx, context) :
    await ctx.channel.send("@here")
    embed = discord.Embed(title = "쿠크세이튼 리허설 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffbbc6)
    embed.add_field(name = f"모집자 : {ctx.message.author.name}", value = f"출발일정 : {context}")
    embed.set_footer(text="ThunderBot by. 안태훈")
    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def 아브데자뷰(ctx, context) :
    await ctx.channel.send("@here")
    embed = discord.Embed(title = "아브렐슈드 데자뷰 모집", timestamp=datetime.datetime.now(pytz.timezone('UTC')), color = 0xffbbc6)
    embed.add_field(name = f"모집자 : {ctx.message.author.name}", value = f"출발일정 : {context}")
    embed.set_footer(text="ThunderBot by. 안태훈")
    await ctx.send(embed = embed)

@client.event
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇이면 패스
        return None
    if str(reaction.emoji) == "👍":
        await reaction.message.channel.send("💬"+ user.name + "님이(가) 참여를 희망합니다")

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
bot.run(access_token)
