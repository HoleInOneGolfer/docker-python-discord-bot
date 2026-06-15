import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from pathlib import Path

import db

if load_dotenv():
    print(".env file loaded successfully.")
else:
    print("No .env file found or failed to load (using system environment variables).")

if "DEV_MODE" in os.environ:
    DATA_DIR = Path("./data")
    print("DEV_MODE is enabled.")
else:
    DATA_DIR = Path("/data")
    print("DEV_MODE is disabled.")

DB_FILE_PATH = DATA_DIR / "db.sqlite"

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if not DISCORD_TOKEN:
    print("DISCORD_TOKEN is not set. Please set it in the .env file or system environment variables.")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has logged in!")
    print(f"Invite URL: {discord.utils.oauth_url(bot.user.id, permissions=discord.Permissions(permissions=8))}")

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="developing new bots"))

    db.init_db(DB_FILE_PATH)

    try:
        print("Scrubbing ghost guild commands...")
        for guild in bot.guilds:
            db.save_guild(DB_FILE_PATH, guild.id, guild.name)

            bot.tree.clear_commands(guild=guild)
            await bot.tree.sync(guild=guild)

        print("Syncing global commands...")
        synced = await bot.tree.sync()
        print(f"Successfully synced {len(synced)} global command(s)!")

    except Exception as e:
        print(f"Error during sync: {e}")

@bot.event
async def on_guild_join(guild: discord.Guild):
    print(f"Joined a new server: {guild.name} (ID: {guild.id})")
    db.save_guild(DB_FILE_PATH, guild.id, guild.name)

    try:
        bot.tree.clear_commands(guild=guild)
        await bot.tree.sync(guild=guild)
    except Exception as e:
        print(f"Failed to sync newly joined guild tree: {e}")

@bot.tree.command(name="ping", description="Responds with Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

@bot.tree.command(name="hello", description="Responds with a friendly greeting!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}!", ephemeral=True)

@bot.tree.command(name="dm", description="Sends you a direct message!")
async def dm(interaction: discord.Interaction):
    try:
        await interaction.user.send("This is a direct message from the bot!")
        await interaction.response.send_message("I've sent you a DM!", ephemeral=True)
    except discord.Forbidden:
        await interaction.response.send_message("I couldn't send you a DM. Please check your privacy settings.", ephemeral=True)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error

bot.run(DISCORD_TOKEN)
