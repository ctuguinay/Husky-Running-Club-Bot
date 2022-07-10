# Husky Running Club Bot

## What are the Prerequisites for Using this Repository?
You must have an account for Discord [[Link](https://discordapp.com/developers/applications/)], GitHub [[Link](https://github.com/join)] , and Heroku [[Link](https://signup.heroku.com/)].

## 1st Step: How do I create a bot and get a bot token?
* Create an application in the developer portal by clicking [here](https://discordapp.com/developers/applications/)
* Open up your new application and click 'Add Bot' under the Bot settings to create your bot.
* After creating the bot, click the 'Copy' button under the title Token. Take note of your token as you will need it later.

## 2nd Step: How to Host this Bot Locally

* Make sure you have at LEAST Python 3.7.0.
* Download the repository and navigate to the top of the repository.
* Run the following to setup the environment:
```
pip install -r requirements
```

* Then navigate to the `/bot` folder: 
```
cd bot
```

* Create a `.env` file with the following:
```
DISCORD_TOKEN=$DISCORD_TOKEN
ON_LOCAL=True
CHANNEL=$CHANNEL
```

* Replace `$DISCORD_TOKEN` with your own Discord bot Token.
* Replace `$CHANNEL` as your desired output channel's ID, which can be found by turning on Developer Mode in settings, right clicking your desired channel, and selecting the Copy ID option.

* In the `/bot` folder, run the following to start the bot:
```
python main.py --set_mode locally
```

## 3rd Step: How to Host this Bot on Heroku

### How to fork the repository and set it up to work with Heroku?
* Fork a copy of this repository by clicking the 'Fork' on the upper right-hand.
* Create an application for Heroku by clicking [here](https://dashboard.heroku.com/new-app).
* Under 'Deploy', do the following:
  * Deployment Method => Connect your GitHub
  * App connected to GitHub => Search for the forked repository
  * Automatic Deploy => Enable Automatic Deploy (to redeploy after every commit)
* Under 'Settings', click on 'Reveal Config Vars' and enter the following:
  * KEY => DISCORD_TOKEN
  * VALUE => (Enter the bot token that you copied from the developer portal)
  * Click the 'Add' button after entering all of this information.
* Under 'Resources', do the following:
  * Click on the 'Pencil' icon.
  * Switch the worker from off to on.
  * Click 'Confirm' to finalize the decision.
  * NOTE: You are allocated 550 free Dyno hours, which will not last the entire month. However, if you provide a credit card to verify your identity, you are given an additional 450 hours, which will allow your bot to run indefinitely.
  
## Todo:
* Implement testing, with Pytest and either dpytest or another bot to read this bot's messages.