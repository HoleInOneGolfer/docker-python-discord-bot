import os
import discord
from discord.ext import commands
import db


class Bot(commands.Bot):
    def __init__(self):
        # Initializing prefix-free slash configuration
        super().__init__(command_prefix="", intents=discord.Intents.default())

    async def setup_hook(self):
        db.init_db()  # Runs your isolated DB setup on script launch
        await self.tree.sync()  # Syncs your slash commands natively with Discord


bot = Bot()


@bot.event
async def on_ready():
    print(f"🚀 {bot.user.name} template container initialized and ready!")
    print(
        f"🔗 Invite Link: {discord.utils.oauth_url(bot.user.id, permissions=discord.Permissions.all())}"
    )


@bot.tree.command(name="ping", description="Check if the bot is responsive")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")


bot.run(os.getenv("DISCORD_TOKEN"))
