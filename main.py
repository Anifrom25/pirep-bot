import os
import discord
from discord.ext import commands
import asyncio
import logging

# ===== LOGGING =====
logging.basicConfig(level=logging.INFO)

# ===== CONFIG =====
TOKEN = os.getenv("TOKEN")  # set in cloud env

RITESH_ID = 711594344611577947
TIGER_ID = 692341086638833664
ZEFF_ID = 533235204870111234
PRITISH_ID = 388039659525242880

ALLOWED_CHANNELS = {
    1458799579037171712,
    1246895842581938279,
    1495763871242391662,
}

# ===== DISCORD SETUP =====
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ===== EVENTS =====
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    try:
        if message.author.bot:
            return

        if message.channel.id not in ALLOWED_CHANNELS:
            return

        content_lower = message.content.lower()
        mentioned_ids = [user.id for user in message.mentions]

        # ===== RITESH =====
        if RITESH_ID in mentioned_ids and "pirep" in content_lower:
            await message.channel.send(
                f"{message.author.mention} Ritesh321 naya hai idhar, bacche ko chhor do."
            )

        # ===== TIGER =====
        elif TIGER_ID in mentioned_ids and "pirep" in content_lower:
            await message.channel.send(
                f"{message.author.mention} TIGER_ANI checks PIREPs roughly every 24 hours, be patient."
            )

        # ===== ZEFF =====
        elif ZEFF_ID in mentioned_ids and "pirep" in content_lower:
            await message.channel.send(
                f"{message.author.mention} Zepto is busy delivering food. He will check PIREPs in a few hours."
            )

        # ===== PRITISH =====
        elif PRITISH_ID in mentioned_ids and "pirep" in content_lower:
            await message.channel.send(
                f"{message.author.mention} Focus on studies. Donâ€™t tag Pritish unnecessarilyâ€”open a ticket if needed."
            )

    except Exception as e:
        print("Error:", e)

    finally:
        await bot.process_commands(message)

# ===== AUTO-RESTART LOOP =====
async def runner():
    while True:
        try:
            if not TOKEN:
                raise Exception("TOKEN not set in environment")

            await bot.start(TOKEN)

        except Exception as e:
            print(f"Bot crashed: {e}")
            print("Restarting in 5 seconds...")
            await asyncio.sleep(5)

# ===== START =====
asyncio.run(runner())
