import os
import discord
from discord.ext import commands
import pytest
import argparse

# Parser to parse whether you are running through local or through Heroku
parser = argparse.ArgumentParser(description='Parser for Husky Running Club Discord Bot.')
parser.add_argument("--set_mode",
                    help="Sets whether you are running locally or through heroku. Will only take locally or heroku as values.",
                    default="locally")
args = parser.parse_args()
mode = args.set_mode

# Check if the mode arg was set properly.
if mode == "locally":
    from dotenv import load_dotenv
    load_dotenv()
elif mode == "heroku":
    try:
        from dotenv import load_dotenv
        load_dotenv()
        if os.getenv("ON_LOCAL"):
            raise ValueError("The heroku arg should not be used on a local machine.")
    except:
        pass
else:
    raise ValueError("You should only use heroku or locally as set_mode args.")

assert(mode == "locally" or mode == "heroku")

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    channel = bot.get_channel(990343297329397820)
    login_message = f"Logged in as {bot.user.name}."
    print(login_message)
    await channel.send(login_message)
    bot.load_extension("cogs.maincog")

if __name__ == "__main__":
    bot.run(TOKEN)