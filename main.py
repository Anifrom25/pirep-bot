import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")  # IMPORTANT

RITESH_ID = 711594344611577947

ALLOWED_CHANNELS = [
    1458799579037171712,
    1246895842581938279,
    1495763871242391662 # ticket
]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id not in ALLOWED_CHANNELS:
        return

    content_lower = message.content.lower()

    if any(user.id == RITESH_ID for user in message.mentions) and "pirep" in content_lower:
        await message.channel.send(
            f"{message.author.mention} Ritesh will check PIREPs in a few hours."
        )

    await bot.process_commands(message)

bot.run(TOKEN)
