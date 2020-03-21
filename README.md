# Description

This is a basic polling bot where voting is done through emoticon reactions.

It supports two formats:
 - !poll This is my poll
 - !poll {This is my question} \[Choice 1\] \[Choice 2\] \[Choice 3\] \[Choice 4\] ...

The first format will simply offers three choices: 👍 , 👎 or 🤷 .

The second format will display an embed card with a letter associated to each choice.

Only authorized role (see configuration) can setup a vote.


# Configuration
The file config.yaml allows to setup your bot.
There is two entries:
 - one is a token given by discord to authenticate your bot (see Discord Setup paragraph).
 - second one is a list of role which are authorize to run poll


# Discord Setup

First you need to create a bot application:

 - Go to https://discordapp.com/developers/applications
 - Click button `New Application`
 - Enter a name for your bot (you can change it later) and click `Create`
 - Go to the `Bot` settings (third option on the left) and click `Add bot`
 - You can now customize the name of your bot and its avatar icon
 - Click the `Copy` button for the token : paste it in the config.yaml .

Note: Keep this token secret are people might abuse it to mess with your server

Now you need to invite your server:

 - Go to `OAuth2` settings : in the scope section select `bot` and then add permission to the bot.
  You need at least to authorize Send Message, Manage Message, Embed Links, Read Message History, Mention Everyone and Add Reactions.
 - Click the `Copy` button in the scope section and paste it in your browser
 - Select you server and click `Continue`

You bot is now ready to be run.


# Running the Bot

To run the bot from your PC you need:
 - python (3.6 and above) : follow instruction on https://www.python.org/downloads/
 - Install the discord library : `pip install discord --user`
 - Run the bot with `python bot.py`

For free hosting solution check https://aws.amazon.com/free or https://www.heroku.com/

You can also setup your own server with a cheap raspberry Pi.
