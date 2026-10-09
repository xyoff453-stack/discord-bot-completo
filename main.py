import asyncio
from pathlib import Path

import discord
from discord.ext import commands

from config import TOKEN, PREFIX, GUILD_ID

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=PREFIX,
    help_command=None,
    intents=intents,
)


@bot.event
async def on_ready():
    print(f"Bot conectado como: {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{PREFIX}help | {len(bot.guilds)} servidores",
        )
    )

    if GUILD_ID:
        await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
    else:
        await bot.tree.sync()


async def load_extensions():
    for file in sorted(Path("cogs").glob("*.py")):
        if file.name.startswith("__"):
            continue
        await bot.load_extension(f"cogs.{file.stem}")


async def main():
    if not TOKEN:
        raise ValueError("DISCORD_TOKEN não foi encontrado. Crie um arquivo .env a partir do .env.example.")

    await load_extensions()
    await bot.start(TOKEN)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nEncerrando bot...")
