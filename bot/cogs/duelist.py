import discord as d
from discord.ext import commands
from bot.constants import EMOJI_SUCCESS, EMOJI_WARNING, PRIMARY_COLOR


class Duelist(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command()
    @d.guild_only()
    async def duelist_create_role(self, ctx: d.ApplicationContext):
        """Creates duelist role if it does not alreay exist

        Handled Cases:
        - Does not have permission to manage roles
        - Role already exists
        """
        embed = d.Embed(color=PRIMARY_COLOR)
        if not ctx.user.guild_permissions.manage_roles:  # type: ignore
            embed.description = f"{EMOJI_WARNING} You don't have the permission to manage roles. Please contact with the admin"
            await ctx.respond(embed=embed, ephemeral=True)
            return
        for role in ctx.guild.roles:  # type: ignore
            if role.name == "duelist":
                embed.description = f"{EMOJI_WARNING} {role.mention} already exists"
                await ctx.respond(embed=embed, ephemeral=True)
                return
        role = await ctx.guild.create_role(name="duelist")  # type: ignore
        embed.description = f"{EMOJI_SUCCESS} Created {role.mention} role"
        await ctx.respond(embed=embed, ephemeral=True)

    @commands.slash_command()
    @d.guild_only()
    async def duelist_get_role(self, ctx: d.ApplicationContext):
        """Get notified for open duels

        Handled Cases:
        - Already have duelist role
        - Role does not exist in guild
        """
        embed = d.Embed(color=PRIMARY_COLOR)
        for role in ctx.user.roles:  # type: ignore
            if role.name == "duelist":
                embed.description = (
                    f"{EMOJI_WARNING} You already have {role.mention} role"
                )
                await ctx.respond(embed=embed, ephemeral=True)
                return
        for role in ctx.guild.roles:  # type: ignore
            if role.name == "duelist":
                await ctx.user.add_roles(role)  # type: ignore
                embed.description = f"{EMOJI_SUCCESS} Added {role.mention} role"
                await ctx.respond(embed=embed, ephemeral=True)
                return
        embed.description = f"{EMOJI_WARNING} This server does not have `duelist` role. Please use /duelist_create_role to create the role"
        await ctx.respond(embed=embed, ephemeral=True)

    @commands.slash_command()
    @d.guild_only()
    async def duelist_remove_role(self, ctx: d.ApplicationContext):
        """Remove duelist role from user

        Handled Cases:
        - Role does not exist in guild
        - User does not have duelist role
        """
        embed = d.Embed(color=PRIMARY_COLOR)
        for role in ctx.guild.roles:  # type: ignore
            if role.name == "duelist":
                for user_role in ctx.user.roles:  # type: ignore
                    if user_role.name == "duelist":
                        await ctx.user.remove_roles(user_role)  # type: ignore
                        embed.description = (
                            f"{EMOJI_SUCCESS} Removed {role.mention} role"
                        )
                        await ctx.respond(embed=embed, ephemeral=True)
                        return
                embed.description = (
                    f"{EMOJI_WARNING} You don't have {role.mention} role"
                )
                await ctx.respond(embed=embed, ephemeral=True)
                return
        embed.description = f"{EMOJI_WARNING} This server does not have `duelist` role. Please use /duelist_create_role to create the role"
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Duelist(bot))
