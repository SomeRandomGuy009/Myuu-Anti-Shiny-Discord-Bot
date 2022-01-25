# Myuu-Anti-Shiny-Discord-Bot

# What is this used for?
If you play Myuu bot, this is really useful for you but maybe harms the market. Currently it prevents these from getting killed: Shiny Pokémon and Greninja-Ash. This helps you not accidently kill any rare Pokémon you've been hunting for a while. (Thanks to NebbyBot's top.gg description)

# Why I made it?
Since, I was legit fed up of NebbyBot's lag (not criticising it), I decided to make my own but in python and host it in replit. It took me around 2hrs at max. 

# How to use it?
Locally:

1. Download Python (3.8 or higher preferred)
2. Clone or download the repo. (unzip if downloaded)
3. Do cd Myuu-Anti-Shiny-Discord-Bot and then pip install -r requirements.txt
4. Remove the keep_alive.py file and the lines about keep_alive from main.py.
5. Create .env file and put your bot token in it: TOKEN=xxxxxx
6. Put the required channel ids in main.py and run this file.

In repl.it:
1. Create a repl, clone this file or import it from github.
2. Install the requirements.txt file.
3. Go to secrets tab, create a secret with the name of TOKEN and put the Bot's token in the field.
4. Put the required channel ids in main.py file.
5. Click on Run button.
6. After the keep_alive server starts, use uptimerobot to keep it online for almost 24/7.

# Current Features:
1. Locks channel for everyone if a shiny or greninja-ash is found (30s locktime)
2. Can only lock one channel at the moment.

# Any upcoming features?
- Look at multiple channels.
- Anti - Starter killing
- Logging with embed instead of text.
- Lock channel for a particular role instead of everyone.
- Lock channels for Admins as well.

# If anyone got any issues, raise it here. If you wanna discuss about some features, my discord id: SomeRandomGuy#1337

# Submit a PR if u want any other feature to be added. I'll take a look at it and merge.

# Note: I just used the idea of Nebby Bot, didn't copy it. NebbyBot is most probably written in discord.js, while this is written in python.
# 2nd Note: I don't encourage macro/autotyper usage.
