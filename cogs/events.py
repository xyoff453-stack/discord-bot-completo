import discord
from discord.ext import commands


class EventHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"🎉 Bem-vindo(a), {member.mention}! Leia as regras e divirta-se.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"👋 {member.name} saiu do servidor.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ Você não tem permissão para usar este comando.")
            return

        if isinstance(error, commands.CommandNotFound):
            return

        await ctx.send(f"❌ Ocorreu um erro: {error}")


async def setup(bot):
    await bot.add_cog(EventHandler(bot))
