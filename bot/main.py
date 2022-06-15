import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command(name="test")
@commands.has_role("Officer")
async def ping(ctx):
    embed=discord.Embed(title="Green Lake Zoo Loop", url="https://www.mapmyfitness.com/routes/view/embedded/5050970416?width=600&height=400&&line_color=E68006c6&rgbhex=c60680&distance_markers=0&unit_type=imperial&map_mode=ROADMAP&show_marker_every=1&last_updated=undefined'",
    description="Test Embed", color=0xFF5733)
    embed.set_thumbnail(url="imgs/zoo_loop.jpeg")
    await ctx.send(embed=embed)

if __name__ == "__main__":
    bot.run(TOKEN)
