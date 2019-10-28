import os
import dice
import discord

from dotenv import load_dotenv


from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
IMAGE_URL = os.getenv('IMAGE_URL')

#
# Discord has some strange color definitions
#
colors = {
  'DEFAULT': 0x000000,
  'WHITE': 0xFFFFFF,
  'AQUA': 0x1ABC9C,
  'GREEN': 0x2ECC71,
  'BLUE': 0x3498DB,
  'PURPLE': 0x9B59B6,
  'LUMINOUS_VIVID_PINK': 0xE91E63,
  'GOLD': 0xF1C40F,
  'ORANGE': 0xE67E22,
  'RED': 0xE74C3C,
  'GREY': 0x95A5A6,
  'NAVY': 0x34495E,
  'DARK_AQUA': 0x11806A,
  'DARK_GREEN': 0x1F8B4C,
  'DARK_BLUE': 0x206694,
  'DARK_PURPLE': 0x71368A,
  'DARK_VIVID_PINK': 0xAD1457,
  'DARK_GOLD': 0xC27C0E,
  'DARK_ORANGE': 0xA84300,
  'DARK_RED': 0x992D22,
  'DARK_GREY': 0x979C9F,
  'DARKER_GREY': 0x7F8C8D,
  'LIGHT_GREY': 0xBCC0C0,
  'DARK_NAVY': 0x2C3E50,
  'BLURPLE': 0x7289DA,
  'GREYPLE': 0x99AAB5,
  'DARK_BUT_NOT_BLACK': 0x2C2F33,
  'NOT_QUITE_BLACK': 0x23272A
}


# This is our bot
class DiceRoller(commands.Bot):
    #
    # When everything is ready, just print out some info.
    #
    async def on_ready(self):
        guild = discord.utils.get(self.guilds, name=GUILD)
        if guild:
            print(f'{self.user} is connected to the following guild:\n'
                  f'{guild.name}(id: {guild.id})\n')
            print('Bot is running.')
            print('Exit with CTRL-C or by restarting your server (or the whole hypervisor if you have doubts).')

    #
    # We only have one command, but we might get more commands and some will have required parameters, then you'll be
    # glad that this stub was implemented here.
    #
    async def on_command_error(self, context, exception):
        if isinstance(exception, commands.errors.MissingRequiredArgument):
            await context.send(content=f'Sabaka! You forgot your parameters.')


# Set command prefix to !, I feel silly about these comments
bot = DiceRoller(command_prefix='!')


#
# Add roll command
#
@bot.command(name='roll', help='Roll a standard dice notation roll.')
async def bot_roll(ctx, arg: str = '3d6'):
    roll_result = dice.roll(arg)
    #
    # This could fail for some rolls? I didn't bother to check if we can have other types of results
    #
    if type(roll_result) == dice.elements.Roll:
        total = sum(roll_result)
        if arg == '3d6':  # Print drama dice separately and check if you stunt points are generated
            sp = False
            if roll_result[0] == roll_result[1] or roll_result[0] == roll_result[2] or roll_result[1] == roll_result[2]:
                sp = True

            desc = f'\n\nRoll result: [ **{roll_result[0]}** ] [ **{roll_result[1]}** ] [ ***{roll_result[2]}*** ]\n'
            desc += f'Drama [ **{roll_result[2]}** ]\n'
            if sp:
                desc += f'Stunt points: ` {roll_result[2]}` \n'
            desc += f'Total: **[ {total} ]**\n'
            desc += f'\n'
        else:
            desc = f'\n\nRoll result:'
            for r in roll_result:
                desc += f' [ **{r}** ]'
            desc += f'\n'
            desc += f'Total: **[ {total} ]**\n'
    else:
        desc = f'\n\nRoll result: **[ {roll_result} ]**\n\n'

    resp = discord.Embed(
        description=desc,
        colour=colors['BLUE']
    )

    resp.set_author(
        name=f'{ctx.author.name} rolled {arg}',
        icon_url=f'{IMAGE_URL}/dice.png' if IMAGE_URL else ''
    )

    resp.set_thumbnail(url=f'{IMAGE_URL}/dice.png' if IMAGE_URL else '')
    await ctx.send(embed=resp)

#
# Run bot RUN!
#
bot.run(TOKEN, bot=True, reconnect=True)
