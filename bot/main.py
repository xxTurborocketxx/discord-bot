# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

# IMPORT THE OS MODULE.
import os

import asyncio

import time

import discord

import random

import logging

from discord.ext.commands import Bot

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot: Bot = commands.Bot(command_prefix='$', help_command=None)
bot.message_counter = 0

print("The Bot is now fully loaded. Developed by xxTurborocketxx")


# ON_MESSAGE() EVENT LISTENER. NOTICE IT IS USING @BOT.EVENT AS OPPOSED TO @BOT.COMMAND().
@bot.event
async def on_message(message):
    # CHECK IF THE MESSAGE SENT TO THE CHANNEL IS "HELLO".
    if message.content == "hello":
        # SENDS A MESSAGE TO THE CHANNEL.
        await message.channel.send("Hello my friend")


@bot.event
async def on_message(message):
    # CHECK IF THE MESSAGE SENT TO THE CHANNEL IS "HELLO".
    if message.content == "K6":
        # SENDS A MESSAGE TO THE CHANNEL.
        await message.channel.send("K6 is hot :smirk:")


@bot.event
async def on_message(message):
    # CHECK IF THE MESSAGE SENT TO THE CHANNEL IS "HELLO".
    if message.content == "no u":
        # SENDS A MESSAGE TO THE CHANNEL.
        await message.channel.send("no u :smirk:")

    # INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
    await bot.process_commands(message)


# COMMAND $PING. INVOKES ONLY WHEN THE MESSAGE "$PING" IS SEND IN THE DISCORD SERVER.
# ALTERNATIVELY @BOT.COMMAND(NAME="PING") CAN BE USED IF ANOTHER FUNCTION NAME IS DESIRED.
@bot.command(
    # ADDS THIS VALUE TO THE $HELP PING MESSAGE.
    help="Uses come crazy logic to determine if pong is actually the correct value or not.",
    # ADDS THIS VALUE TO THE $HELP MESSAGE.
    brief="Prints pong back to the channel."
)
async def ping(ctx):
    await ctx.send('My ping is {0}'.format(round(bot.latency, 1)))


@bot.command()
async def help(ctx, args=None):
    help_embed = discord.Embed(title="My Bot's Help!", color=0x9F00FB)
    command_names_list = [x.name for x in bot.commands]

    # If there are no arguments, just list the commands:
    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i + 1) + ". " + x.name for i, x in enumerate(bot.commands)]),
            inline=False
        )
        help_embed.add_field(
            name="Details",
            value="Type `$help <command name>` for more details about each command.",
            inline=False
        )

    # If the argument is a command, get the help text from that command:
    elif args in command_names_list:
        help_embed.add_field(
            name=args,
            value=bot.get_command(args).help
        )

    # If someone is just trolling:
    else:
        help_embed.add_field(
            name="Nope.",
            value="Don't think I got that command, boss!"
        )

    await ctx.send(embed=help_embed)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$help"))


# COMMAND $PRINT. THIS TAKES AN IN A LIST OF ARGUMENTS FROM THE USER AND SIMPLY PRINTS THE VALUES BACK TO THE CHANNEL.
@bot.command(
    # ADDS THIS VALUE TO THE $HELP PRINT MESSAGE.
    help="Looks like you need some help.",
    # ADDS THIS VALUE TO THE $HELP MESSAGE.
    brief="Prints the list of values back to the channel."
)
async def print(ctx, *args):
    response = ""

    # LOOPS THROUGH THE LIST OF ARGUMENTS THAT THE USER INPUTS.
    for arg in args:
        response = response + " " + arg

    # SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
    await ctx.channel.send(response)


@bot.command(name="avatar")
async def avatar(ctx, *, avamember: discord.Member = None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    await ctx.send('Cleared by {}'.format(ctx.author.mention))
    await ctx.message.delete()


@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")


@bot.event
async def on_message(message):
    user = message.author
    if message.content.startswith("bruh"):
        embed = discord.Embed(title="Bruh Counter intensifies",
                              description=f"{user} said the word Bruh! \n Bless this dude!", color=0x9F00FB)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/821156208249405473/0e3ab36c4a3a2a65a4faa76b2cc49c98.webp?size=1024")
        embed.set_footer(text="by xxTurborocketxx")
        await message.channel.send(embed=embed)
        bot.message_counter += 1
    await bot.process_commands(message)


@bot.command(name="bruh")
async def bruh(ctx):
    embed = discord.Embed(title="Bruh Counter",
                          description="The word bruh has been said {} times!".format(ctx.bot.message_counter),
                          color=0x9F00FB)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/821156208249405473/0e3ab36c4a3a2a65a4faa76b2cc49c98.webp?size=1024")
    embed.add_field(name="Conclusion", value="The word bruh is overrated.", inline=True)
    embed.set_footer(text="by xxTurborocketxx")
    await ctx.send(embed=embed)


@bot.command(name="turbo")
async def turbo(ctx):
    await ctx.channel.send("Turbo is the coolest")


@bot.command(name="diyar")
async def diyar(ctx):
    await ctx.channel.send("Diyar ist nicht toll")


@bot.command(name="marv")
async def marv(ctx):
    await ctx.channel.send("Marv ist ganz toll")


@bot.command(name="crusader")
async def crusader(ctx):
    await ctx.channel.send("Crusader is gay")


@bot.command(name="pprate")
async def pprate(ctx):
    await ctx.channel.send("you have a very smol pp lol")


@bot.command(name="turtle")
async def turtle(ctx):
    await ctx.channel.send("https://imgur.com/gallery/Mn6YH")


@bot.command(name="twitch")
async def twitch(ctx):
    await ctx.channel.send("https://www.twitch.tv/xxTurborocketxx")


@bot.command(name="astrania")
async def astrania(ctx):
    await ctx.channel.send("https://discord.gg/QXmGDjTe9P")


@bot.command(name="killme")
async def killme(ctx):
    await ctx.channel.send("you are now dead")


@bot.command(name="marvyt")
async def marvyt(ctx):
    await ctx.channel.send("https://www.youtube.com/Marv21HD")


@bot.command(name="goodbot")
async def goodbot(ctx):
    await ctx.channel.send("Thank you")


@bot.command(name="frog")
async def frog(ctx):
    await ctx.channel.send("https://giphy.com/gifs/frog-mXnu6HiBvOckU")


@bot.command(name="snake")
async def snake(ctx):
    await ctx.channel.send(
        "https://tenor.com/view/serpiente-bailando-serpiente-bailando-dancing-snake-marinnadas-gif-20741343")


@bot.command(name="cat")
async def cat(ctx):
    await ctx.channel.send("https://giphy.com/gifs/easy-ear-MCfhrrNN1goH6")


@bot.command(name="fish")
async def fish(ctx):
    await ctx.channel.send("https://tenor.com/view/bubble-fish-goldfish-wat-wut-gif-15150581")


@bot.command(name="yeet")
async def yeet(ctx):
    embed = discord.Embed(title="Yeet", description="To discard an item at a high velocity", color=0x9F00FB)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/821156208249405473/0e3ab36c4a3a2a65a4faa76b2cc49c98.webp?size=1024")
    embed.set_footer(text="by xxTurborocketxx")
    await ctx.send(embed=embed)


@bot.command(name="why")
async def why(ctx):
    await ctx.channel.send("https://tenor.com/view/confused-white-persian-guardian-why-gif-11908780")


@bot.command(name="nom")
async def nom(ctx):
    embed = discord.Embed(title="Nom",description="The sound made when eating something (or someone). Can be referred to as nomming as a verb, and is often pronounced in the sentence om nom nom.",color=0x9F00FB)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/821156208249405473/0e3ab36c4a3a2a65a4faa76b2cc49c98.webp?size=1024")
    embed.set_footer(text="by xxTurborocketxx")
    await ctx.send(embed=embed)


@bot.command(name="FVD")
async def fvd(ctx):
    await ctx.channel.send("Stap in makker we breken het partij kartel")


@bot.command(name="spotify")
async def spotify(ctx):
    await ctx.channel.send("https://open.spotify.com/user/laser_supra?si=Acv9AHvkRXeWeCzehmU5nQ")


@bot.command(name="dlb")
async def dlb(ctx):
    await ctx.channel.send("https://open.spotify.com/artist/5sUcZwHpvdUn4TyjqMMMfo?si=bPC9rfmYQHKrkOMqwAezng")


@bot.command(name="skyline")
async def skyline(ctx):
    embed = discord.Embed(title="Nissan Skyline",
                          description="The Nissan Skyline (Japanese: 日産・スカイライン, Nissan Sukairain) is a brand of automobile originally produced by the Prince Motor Company starting in 1957, and then by Nissan after the two companies merged in 1967. After the merger, the Skyline and its larger counterpart, the Nissan Gloria, were sold in Japan at dealership sales channels called Nissan Prince Shop.",
                          color=0x9F00FB)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/821156208249405473/0e3ab36c4a3a2a65a4faa76b2cc49c98.webp?size=1024")
    embed.set_footer(text="by xxTurborocketxx")
    await ctx.send(embed=embed)


@bot.command(name="s2000")
async def s2000(ctx):
    embed = discord.Embed(title="Honda S2000",
                          description="The Honda S2000 is an open top sports car that was manufactured by Japanese automobile manufacturer Honda, from 1999 to 2009. First shown as a concept car at the Tokyo Motor Show in 1995, the production version was launched on April 15, 1999 to celebrate the company's 50th anniversary. The S2000 is named for its engine displacement of two liters, carrying on in the tradition of the S500, S600, and S800 roadsters of the 1960s.",
                          color=0x9F00FB)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/821156208249405473/0e3ab36c4a3a2a65a4faa76b2cc49c98.webp?size=1024")
    embed.set_footer(text="by xxTurborocketxx")
    await ctx.send(embed=embed)


@bot.command(name="chaser")
async def chaser(ctx):
    embed = discord.Embed(title="Toyota Chaser",
                          description="The Toyota Chaser is a mid-size car produced by Toyota in Japan. Most Chasers are four-door sedans and hardtop sedans; a two-door hardtop coupé was available on the first generation only. It was introduced on the 1976 Toyota Corona Mark II platform, and was sold new by Toyota at Toyota Vista Store dealerships only in Japan, together with the Toyota Cresta.",
                          color=0x9F00FB)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/821156208249405473/0e3ab36c4a3a2a65a4faa76b2cc49c98.webp?size=1024")
    embed.set_footer(text="by xxTurborocketxx")
    await ctx.send(embed=embed)


@bot.command(name="jdm")
async def jdm(ctx):
    embed = discord.Embed(title="JDM",
                          description="Japanese domestic market refers to Japan's home market for vehicles. For the importer, these terms refer to vehicles and parts designed to conform to Japanese regulations and to suit Japanese buyers. The term is abbreviated JDM.",
                          color=0x9F00FB)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/821156208249405473/0e3ab36c4a3a2a65a4faa76b2cc49c98.webp?size=1024")
    embed.set_footer(text="by xxTurborocketxx")
    await ctx.send(embed=embed)


@bot.command(name="cringe")
async def cringe(ctx):
    await ctx.channel.send(
        "https://cdn.discordapp.com/attachments/788185828559290418/821751009084309504/uamee_-_COMRADE_YOU_JUST_POSTED_CRINGE_HARDBASS.mp4")


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)
