import discord
from discord.ext import commands
import json
from datetime import datetime, date

#Example for rewrite, not async.

class Upvote:
    def __init__(self, bot):
        self.bot = bot
        self.config = 'config.json'

    @commands.command(hidden=True)
    async def vote(self, ctx):
        """Vote Command"""

        today = datetime.today().strftime('%Y-%m-%d')
        voters = self.get_userids(today)
        userid = str(ctx.author.id)

        if userid in voters:
            check = self.write_userids(today, userid)
            if check == "already_voted":
                return await ctx.send("You already voted, please try again tommorow.")
            await ctx.send("Whoop, seems like you voted. Here's your reward: ____")
        else:
            await ctx.send("Seems like you haven't voted. You can vote here: {}".format(self.get_config("voteurl")))


    def get_config(self, key=None):
        with open(self.config, 'r') as x:
    	    data = json.load(x)
        if key is None:
            return data
        return data[key]

    def get_userids(self, key=None):
        with open(self.get_config("upvotepath"), 'r') as x:
    	    data = json.load(x)
        if key is None:
            return data
        elif data.get(key) is None:
            return False
        return data[key]

    def write_userids(self, key, id):
        data = self.get_userids()
        if self.get_userids(key) is False:
            data[key] = []
            data[key + "_voted"] = []
        if id in data[key + "_voted"]:
            return "already_voted"
        data[key + "_voted"].append(id)
        with open(self.get_config("upvotepath"), 'w') as x:
            json.dump(data, x)
        return True

def setup(bot):
    bot.add_cog(Upvote(bot))
