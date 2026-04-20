import discord
from discord.ext import commands

TOKEN = "PASTE_YOUR_TOKEN_HERE"  # or use env later

RITESH_ID = 711594344611577947
TIGER_ID = 692341086638833664

ALLOWED_CHANNELS = [
    1458799579037171712,  # Career Mode
    1246895842581938279,  # Maharaja Lounge
    1495763871242391662,  # ticket
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
    mentioned_ids = [user.id for user in message.mentions]

    # ===== RITESH =====
    if RITESH_ID in mentioned_ids and "pirep" in content_lower:
        await message.channel.send(
            f"{message.author.mention} Ritesh will check PIREPs in a few hours."
        )

    # ===== TIGER =====
    elif TIGER_ID in mentioned_ids and "pirep" in content_lower:
        await message.channel.send(
            f"{message.author.mention} TIGER_ANI checks PIREPs roughly every 24 hours. Thanks for your patience."
        )

    await bot.process_commands(message)

bot.run(TOKEN)
