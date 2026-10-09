import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="reload", aliases=["rl"])
    @commands.is_owner()
    async def reload(self, ctx):
        """Recarrega todas as extensões do bot."""
        for extension in list(self.bot.extensions):
            await self.bot.unload_extension(extension)
            await self.bot.load_extension(extension)
        await ctx.send("✅ Extensões recarregadas com sucesso!")

    @commands.command(name="shutdown")
    @commands.is_owner()
    async def shutdown(self, ctx):
        """Desliga o bot."""
        await ctx.send("🔴 Bot desligando...")
        await self.bot.close()


async def setup(bot):
    await bot.add_cog(Admin(bot))
