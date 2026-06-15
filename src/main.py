import os
import discord
from discord.ext import commands
import db


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="", intents=discord.Intents.default())

    async def setup_hook(self):
        db.init_db()  # Runs table creation

        await self.tree.sync()


bot = Bot()


@bot.event
async def on_ready():
    print(f"🚀 {bot.user.name} template container initialized and ready!")

    # Track every server the bot is already in on startup
    for guild in bot.guilds:
        db.add_guild(guild.id)

    print(
        f"🔗 Invite Link: {discord.utils.oauth_url(bot.user.id, permissions=discord.Permissions.all())}"
    )


@bot.event
async def on_guild_join(guild: discord.Guild):
    """Fires instantly when invited to a new server."""
    db.add_guild(guild.id)
    print(f"➕ Added new server: {guild.name} ({guild.id})")


@bot.tree.command(name="ping", description="Check if the bot is responsive")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")


@bot.tree.command(name="hello", description="Greet the bot")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hello, {interaction.user.mention}!", ephemeral=True
    )


bot.run(os.getenv("DISCORD_TOKEN"))
