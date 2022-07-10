import discord
from discord.ext import commands
from scripts.run_selector import select_weekly_runs
from scripts.set_dictionaries import set_dict, set_long_names


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dict = set_dict()
        self.long_names = set_long_names()

    @commands.command(name="initialize")
    @commands.has_role("Officer")
    async def ping(self, ctx):
        channel = self.bot.get_channel(990343297329397820)
        with open('bot/weekly_index.txt', 'w') as f:
            f.write("0")
        await channel.send("Initialized Quarter.")

    @commands.command(name="weekly")
    @commands.has_role("Officer")
    async def ping(self, ctx):
        try:
            channel = self.bot.get_channel(990343297329397820)
            weekly_runs = select_weekly_runs()
            with open('bot/weekly_runs.txt', 'w') as f:
                for index in range(len(weekly_runs)):
                    run = weekly_runs[index]
                    if run == "Bridge":
                        run = "520 Bridge"
                    f.write(run)
                    f.write('\n')
                    weekly_runs[index] = run
            with open('bot/weekday_index.txt', 'w') as f:
                f.write("0")
            with open('bot/weekly_index.txt', 'r') as f:
                weekly_index = f.readlines()[0]
                weekly_index = int(weekly_index)
            with open('bot/weekly_index.txt', 'w') as f:
                weekly_next_index = weekly_index + 1
                weekly_next_index = str(weekly_next_index)
                f.write(weekly_next_index)
            await channel.send("**Here is our Week " + weekly_next_index + " Run Schedule:**")
            weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            for index in range(len(weekly_runs)):
                run = weekly_runs[index]
                weekday = weekdays[index]
                await channel.send(weekday + ": " + run)
            embed = discord.Embed(title="Husky Running Club Routes", url="https://dawgs.run/routes/",
                                  description="You can view all our routes here.", color=0xFF5733)
            file = discord.File("bot/imgs/hrc_logo.jpg", filename="hrc_logo.jpg")
            embed.set_thumbnail(url="attachment://hrc_logo.jpg")
            await channel.send(file=file, embed=embed)
        except:
            await channel.send("Error. Have not initialized bot for the quarter.")

    @commands.command(name="daily")
    @commands.has_role("Officer")
    async def ping(self, ctx):
        channel = self.bot.get_channel(990343297329397820)
        try:
            with open('bot/weekday_index.txt', 'r') as f:
                index = f.readlines()[0]
                index = int(index)
            with open('bot/weekday_index.txt', 'w') as f:
                next_index = index + 1
                next_index = str(next_index)
                f.write(next_index)
            if index < 5:
                with open('bot/weekly_runs.txt', 'r') as f:
                    run = f.readlines()[index]
                    run = run.replace("\n", "")
                    underscore = run.replace(" ", "_")
                    if index != 1 and index != 4:
                        message_one = "**Today's run is " + run + "!**"
                        message_two = "Be at the Quad by 5:00pm"
                        message_three = "Here are links to maps of the different distances we will run:"
                        await channel.send(message_one)
                        await channel.send(message_two)
                        await channel.send(message_three)
                        for mile in [3, 5, 7]:
                            link = self.dict[run][3]
                            path_append = "bot/imgs/" + underscore + "/"
                            path = underscore + "_" + str(mile) + ".png"
                            embed = discord.Embed(title=run, url="https:" + link,
                                                  description="Map Link for " + run + " " + str(mile) + " route.",
                                                  color=0xFF5733)
                            file = discord.File(path_append + path, filename=path)
                            embed.set_thumbnail(url="attachment://" + path)
                            await channel.send(file=file, embed=embed)
                    elif index == 1:
                        message_one = "**Today is a " + run + " day!**"
                        message_two = "Be at the Quad at 5:30pm. We will jog to Roosevelt from there together."
                        await channel.send(message_one)
                        await channel.send(message_two)
                    elif index == 4:
                        message_one = "**Today's long run is " + run + "!**"
                        message_two = "Be at the Quad by 5:00pm."
                        message_three = "Here is the link to the map of the run:"
                        await channel.send(message_one)
                        await channel.send(message_two)
                        await channel.send(message_three)
                        link = self.long_names[run]
                        path_append = "bot/imgs/long_names/"
                        path = underscore + ".png"
                        embed = discord.Embed(title=run, url="https:" + link,
                                              description="Map Link for " + run + " route.", color=0xFF5733)
                        file = discord.File(path_append + path, filename=path)
                        embed.set_thumbnail(url="attachment://" + path)
                        await channel.send(file=file, embed=embed)
                        await channel.send("*Note: Since this is a fairly long run, feel free to turn back whenever.*")

            else:
                await channel.send("Error. Only 5 weekdays.")
        except:
            await channel.send("Error. Did not set weekly runs.")

    @commands.command(name="weekly_index")
    @commands.has_role("Officer")
    async def ping(self, ctx):
        channel = bot.get_channel(990343297329397820)
        try:
            with open('bot/weekly_index.txt', 'r') as f:
                await channel.send("Weekly Index: " + f.readlines()[0])
        except:
            with open('bot/weekly_index.txt', 'w') as f:
                f.write("0")
            with open('bot/weekly_index.txt', 'r') as f:
                await channel.send("Weekly Index: " + f.readlines()[0])

    @commands.command(name="weekday_index")
    @commands.has_role("Officer")
    async def ping(self, ctx):
        channel = bot.get_channel(990343297329397820)
        try:
            with open('bot/weekday_index.txt', 'r') as f:
                await channel.send("Weekday Index: " + f.readlines()[0])
        except:
            with open('bot/weekday_index.txt', 'w') as f:
                f.write("0")
            with open('bot/weekday_index.txt', 'r') as f:
                await channel.send("Weekday Index: " + f.readlines()[0])

    @commands.command(name="set_weekly_index")
    @commands.has_role("Officer")
    async def ping(self, ctx):
        channel = bot.get_channel(990343297329397820)
        try:
            weekly_index = ctx.message.content.replace("!set_weekly_index ", "")
            with open('bot/weekly_index.txt', 'w') as f:
                f.write(weekly_index)
                await channel.send("Set weekly index to: " + weekly_index)
        except:
            await channel.send("Error. Try: !set_weekly_index int")

    @commands.command(name="set_weekday_index")
    @commands.has_role("Officer")
    async def ping(self, ctx):
        channel = self.bot.get_channel(990343297329397820)
        try:
            weekday_index = ctx.message.content.replace("!set_weekday_index ", "")
            with open('bot/weekday_index.txt', 'w') as f:
                f.write(weekday_index)
                await channel.send("Set weekday index to: " + weekday_index)
        except:
            await channel.send("Error. Try: !set_weekday_index int")

    @commands.command(name="backup_weekly_runs")
    @commands.has_role("Officer")
    async def ping(self, ctx):
        channel = self.bot.get_channel(990343297329397820)
        try:
            with open('bot/weekly_runs.txt', 'r') as f, open('bot/backup_weekly_runs.txt', 'w') as w:
                for index in range(5):
                    run = f.readline()
                    w.write(run)
            await channel.send("Backed up weekly runs.")
        except:
            await channel.send("Error. Weekly runs have not been initialized.")

    @commands.command(name="use_backup_weekly_runs")
    @commands.has_role("Officer")
    async def ping(self, ctx):
        channel = self.bot.get_channel(990343297329397820)
        try:
            with open('bot/backup_weekly_runs.txt', 'r') as f, open('bot/weekly_runs.txt', 'w') as w:
                for index in range(5):
                    run = f.readline()
                    w.write(run)
            await channel.send("Using backedup weekly runs.")
        except:
            await channel.send("Error. Backup weekly runs have not been initialized.")

    @commands.command(name="shutdown")
    @commands.has_role("Officer")
    async def ping(self, ctx):
        channel = self.bot.get_channel(990343297329397820)
        await channel.send("Bot logging off.")
        await self.bot.close()


def setup(bot):
    bot.add_cog(MainCog(bot))
