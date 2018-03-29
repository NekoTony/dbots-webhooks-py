# DiscordBots Webhook  Py Handler

 Hello! This is an example to help people use [Discord Bots](https://discordbots.org/) webhooks to handle upvotes/and reward them based on if they upvoted.

This is just an example to use the webhooks. You may modify if you would like, and fork if you want to contribute. 

Everything should work but I'm still adding things, making it formal.

Made by NekoTony#0047
 
**Requirements:**
 Flask 0.12.2
 Discord.py 1.0.0a
 Python3
 
### Installation
**Flask:** I recommended checking out these urls:

[Official Flask Docs](http://flask.pocoo.org/docs/0.12/installation/)
[How to Configure NGINX for a Flask Web Application](http://www.patricksoftwareblog.com/how-to-configure-nginx-for-a-flask-web-application/)

**Discord.py Rewrite:**

    python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py\[voice\]

*Current don't have an async example, Fork if you would like to add one.*

**Python3**
[Download Python](https://www.python.org/downloads/)

### How to Use

First, download the files in the config. Once you have installed anything, add **vote.py** to wherever you store your modules and **flask.py** wherever you store your python files.

**Configuration:**

To config the webhooks to your settings, you'll need to edit **config.json**.  Please ignore the preset data there.

|botid| auth | post | voteurl| upvotepath | reset |
|--|--|--|--|--|--|
| Your discord bot ID| Your Authorization keyword that you had set thru bot/edit on the official site. | Where you want the Dbots to send upvotes. Ex: http://myurl/post/too| Link to where people can vote for your bot | Where upvotes.json is located | Whether or not you want to store past day upvotes. 0 is default, meaning you would like to store past days. Otherwise, if you want to store only the current day upvotes then set it to 1. Set it to 1 if you want to save space.
 
 Also, make sure your config path is correct as well. You can set that `self.config` in **vote.py**.

Once you config it, start the flask server and the **upvotes.json** will update when an someone has upvoted your bot on the site.

**Storage:**

All upvotes are stored in a .json file and can be easily accessed with simple json knowledge. Here's an example to access them:

