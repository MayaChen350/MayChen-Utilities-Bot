# base files
import discord
from discord.ext import commands
from commands.splatoon.view_amiibos import view_amiibos
import settings
# from utils import *

#commands
from commands.splatoon.edit_amiibo import edit_amiibo
from commands.splatoon.remove_amiibo import remove_amiibo

def run():
    intents = discord.Intents.all()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

################################
# BASE                        
################################
    @bot.event
    async def on_ready(): 
        await bot.wait_until_ready()
        await bot.tree.sync()
        print("Bot is ready.")

    @bot.event
    async def on_command_error(ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("Parameters are missing.")
        else:
            await ctx.send(error)
################################
# Commands
################################             
    bot.add_command(edit_amiibo)
    bot.add_command(remove_amiibo)
    bot.add_command(view_amiibos)
################################
    bot.run(settings.DISCORD_API_SECRET, root_logger=True) # type: ignore

################################

if __name__ == "__main__":
    run()
