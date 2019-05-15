import discord
from discord.ext import commands

class Events(commands.Cog):
  def __init__(self, bot):
    self.bot=bot
    
  @commands.Cog.listener()
  async def on_member_join(self, member):
    role=discord.utils.get(member.guild.roles, name="Frog")
    await member.add_roles(role)
    
def setup(bot):
  bot.add_cog(Events(bot))
