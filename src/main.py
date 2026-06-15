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

    db.init_db(DATA_DIR / "db.sqlite")

bot.run(DISCORD_TOKEN)
