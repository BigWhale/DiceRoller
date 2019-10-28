# DiceRoller

A really simple dice roller bot for Discord made for The Expanse RPG.

You'll have to create a Discord application and a bot and then run this
program with the credentials you got from Discord. There are plenty of
manuals on the internet on how to do this.

## Installation & running

```$ pip install```

Create .env file with the following entries:
```
DISCORD_TOKEN=
DISCORD_GUILD=""
IMAGE_URL=
```

And enter your discord token and your server name. If you want an image to show
as a thumbnail when player are making thaier rolls make sure that you have an
image named `dice.png` at the IMAGE_URL.

```$ ./main.py```

## Daemonizing it

Use supervisord or even screen, this really is a tiny program.

## Usage & syntax

`!roll` - rolls a default 3D6 roll, returning individual throws, drama dice, stunt
points and total result

`!roll 5d6+2` - rolls a 5D6+2 roll

More on dice rolling syntax at https://pypi.org/project/dice/

Every roll that returns a list of dice will display results for everty die and a
total. Rolls that return a single number will display just that number.

## Bugs

No error handling, you're on your own. This was whipped up in a couple of hours
and I never wrote a Discord bot before, so YMMV.

