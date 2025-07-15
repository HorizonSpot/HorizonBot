import os
import discord
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as exc:
        print(f'Failed to sync commands: {exc}')


# COMMANDS
@bot.tree.command(name="hello", description="Introduce yourself to HorizonBot")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello, I'm HorizonBot, right now I don't have much functionality but I guess I exist :3", ephemeral=True)

@bot.tree.command(name="socials", description="See all of Horizon's socials")
async def socials(interaction: discord.Interaction):
    await interaction.response.send_message("YouTube: https://www.youtube.com/@HorizonSpot \n X: https://x.com/Horizon_Spot \n Itch: https://horizonspot.itch.io/")

@bot.tree.command(name="progress", description="Show progress on the next game")
async def progress(interaction: discord.Interaction):
    await interaction.response.send_message("Game name: 'Permission to Die' \n Status: Prototyping & making concepts")


# Run
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
