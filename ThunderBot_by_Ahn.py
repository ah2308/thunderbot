import asyncio
from asyncio.exceptions import SendfileNotAvailableError
from types import CellType
import discord, datetime, pytz
from discord.colour import Color
from discord import channel
from discord import reaction
from discord import embeds
from discord.ext import commands
import os

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print(client.user.id)
    print("실행준비 완료")
    game = discord.Game("ThunderBot_1.1V")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.command(pass_context=True)
async def 청소(ctx, amount=100):
    channel = ctx.command.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        message.append(message)
    await client.delete_message(message)

@client.command()
async def 발탄노말(ctx):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고",color = discord.Colour.red())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="발탄 NORMAL : 1415↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url="https://i.imgur.com/jhmW0so.jpg/")
    msg = await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    await msg.add_reaction("⭕")

@client.command()
async def 발탄하드(ctx):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고",color = discord.Colour.red())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="발탄 HARD : 1445↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url="https://i.imgur.com/jhmW0so.jpg/")
    msg = await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    await msg.add_reaction("⭕")

@client.command()
async def 비아노말(ctx):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고",color = discord.Colour.red())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="비아키스 NORMAL : 1430↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url="https://i.imgur.com/qXomO9A.jpg")
    msg = await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    await msg.add_reaction("⭕")

@client.command()
async def 비아하드(ctx):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고",color = discord.Colour.red())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="비아키스 HARD : 1460↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url="https://i.imgur.com/qXomO9A.jpg")
    msg = await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    await msg.add_reaction("⭕")

@client.command()
async def 쿠크노말(ctx):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고",color = discord.Colour.red())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="쿠크세이튼 NORMAL : 1475↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url="https://i.imgur.com/RwUFJXE.jpg")
    msg = await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    await msg.add_reaction("⭕")

@client.command()
async def 아브2관(ctx):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고",color = discord.Colour.red())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 NORMAL 1~2관문 : 1490↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url="https://imgur.com/rhKKyqE")
    msg = await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    await msg.add_reaction("⭕")

@client.command()
async def 아브4관(ctx):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고",color = discord.Colour.red())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 NORMAL 3~4관문 : 1500↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url="https://imgur.com/rhKKyqE")
    msg = await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    await msg.add_reaction("⭕")

@client.command()
async def 아브6관(ctx):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고",color = discord.Colour.red())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 NORMAL 5~6관문 : 1520↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url="https://imgur.com/rhKKyqE")
    msg = await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    await msg.add_reaction("⭕")

@client.command()
async def 하브2관(ctx):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고",color = discord.Colour.red())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 HARD 1~2관문 : 1540↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url="https://imgur.com/rhKKyqE")
    msg = await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    await msg.add_reaction("⭕")

@client.command()
async def 하브4관(ctx):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고",color = discord.Colour.red())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 HARD 3~4관문 : 1550↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url="https://imgur.com/rhKKyqE")
    msg = await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    await msg.add_reaction("⭕")

@client.command()
async def 하브6관(ctx):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고",color = discord.Colour.red())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 HARD 5~6관문 : 1560↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url="https://imgur.com/rhKKyqE")
    msg = await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    await msg.add_reaction("⭕")

@client.command()
async def 쿠크리허설(ctx):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고",color = discord.Colour.red())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="쿠크세이튼 리허설 : 1385↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url="https://i.imgur.com/RwUFJXE.jpg")
    msg = await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    await msg.add_reaction("⭕")

@client.command()
async def 아브데자뷰(ctx):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고",color = discord.Colour.red())
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 데자뷰 : 1430↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url="https://imgur.com/rhKKyqE")
    msg = await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    await msg.add_reaction("⭕")

@client.command()
async def 실험(ctx):
    await ctx.channel.send("@everyone")
    embed = discord.Embed(title="실험용 제목", color = discord.Colour.red())
    msg = await ctx.channel.send
    await ctx.channel.send(embed=embed)
    channel = ctx.command.channel
    
@client.event
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇이면 패스
        return None
    if str(reaction.emoji) == "⭕":
        await reaction.message.channel.send("💬"+ user.name + "님이(가) 참여를 희망합니다")

@client.command()
async def 입찰4(ctx, a:int):
    sum = a * 0.63
    await ctx.reply(f"{round(sum)}" + "골드를 넘어가면 손해")

@client.command()
async def 입찰8(ctx, a:int):
    sum = a * 0.75
    await ctx.reply(f"{round(sum)}" + "골드를 넘어가면 손해")


access_token = os.environ['BOT_TOKEN']
client.run(access_token)
