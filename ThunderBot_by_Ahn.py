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
abrelshud = "https://cdn.discordapp.com/attachments/917722475599659008/917722696962441216/irun-hiper-31.jpg"
koukusaten = "https://i.imgur.com/RwUFJXE.jpg"
baltan = "https://i.imgur.com/jhmW0so.jpg/"
viackiss = "https://i.imgur.com/qXomO9A.jpg"

@client.event
async def on_ready():
    print(client.user.id)
    print("실행준비 완료")
    game = discord.Game("ThunderBot_1.1V")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.command()
async def 발탄노말(ctx, *, message=None):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고", description = "일시 : " + f"{message}", color = discord.Colour.red())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="발탄 NORMAL : 1415↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url=baltan)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("⭕")

@client.command()
async def 발탄하드(ctx, *, message=None):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고", description = "일시 : " + f"{message}", color = discord.Colour.red())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="발탄 HARD : 1445↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url=baltan)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("⭕")

@client.command()
async def 비아노말(ctx, *, message=None):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고", description = "일시 : " + f"{message}", color = discord.Colour.red())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="비아키스 NORMAL : 1430↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url=viackiss)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("⭕")

@client.command()
async def 비아하드(ctx, *, message=None):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고", description = "일시 : " + f"{message}", color = discord.Colour.red())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="비아키스 HARD : 1460↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url=viackiss)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("⭕")

@client.command()
async def 쿠크노말(ctx, *, message=None):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고", description = "일시 : " + f"{message}", color = discord.Colour.red())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="쿠크세이튼 NORMAL : 1475↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url=koukusaten)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("⭕")

@client.command()
async def 아브2관(ctx, *, message=None):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고", description = "일시 : " + f"{message}", color = discord.Colour.red())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 NORMAL 1~2관문 : 1490↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url=abrelshud)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("⭕")

@client.command()
async def 아브4관(ctx, *, message=None):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고", description = "일시 : " + f"{message}", color = discord.Colour.red())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 NORMAL 3~4관문 : 1500↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url=abrelshud)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("⭕")

@client.command()
async def 아브6관(ctx, *, message=None):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고", description = "일시 : " + f"{message}", color = discord.Colour.red())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 NORMAL 5~6관문 : 1520↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url=abrelshud)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("⭕")

@client.command()
async def 하브2관(ctx, *, message=None):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고", description = "일시 : " + f"{message}", color = discord.Colour.red())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 HARD 1~2관문 : 1540↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url=abrelshud)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("⭕")

@client.command()
async def 하브4관(ctx, *, message=None):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고", description = "일시 : " + f"{message}", color = discord.Colour.red())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 HARD 3~4관문 : 1550↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url=abrelshud)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("⭕")

@client.command()
async def 하브6관(ctx, *, message=None):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고", description = "일시 : " + f"{message}", color = discord.Colour.red())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 HARD 5~6관문 : 1560↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url=abrelshud)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("⭕")

@client.command()
async def 쿠크리허설(ctx, *, message=None):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고", description = "일시 : " + f"{message}", color = discord.Colour.red())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="쿠크세이튼 리허설 : 1385↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url=koukusaten)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("⭕")

@client.command()
async def 아브데자뷰(ctx, *, message=None):
    await ctx.channel.send("@here")
    embed = discord.Embed(title="레이드 모집 공고", description = "일시 : " + f"{message}", color = discord.Colour.red())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="ThunderBot_1.1v", icon_url="https://i.imgur.com/i84hned.png")
    embed.add_field(name="아브렐슈드 리허설 : 1430↑", value="아래 ⭕를 눌러 참여신청", inline=False)
    embed.set_image(url=abrelshud)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction("⭕")

@client.event
async def on_reaction_add(reaction, user, avamember : discord.Member=None):
    if user.bot == 1: #봇이면 패스
        return None
    if str(reaction.emoji) == "⭕":
        await reaction.message.channel.send("🟢" + user.name + "님이(가) 참여")

@client.command()
async def 입찰(ctx, a:int):
    sum = a * 0.63
    sum2 = a * 0.75
    await ctx.reply(f"4인 기준{round(sum)}" + "골드가 상회입찰\n"+f"8인 기준{round(sum2)}"+"골드가 상회입찰")


access_token = os.environ['BOT_TOKEN']
client.run(access_token)
