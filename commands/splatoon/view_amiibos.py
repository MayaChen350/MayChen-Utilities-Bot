import discord
from discord.ext import commands
from discord import app_commands
import requests

@commands.hybrid_command()
async def view_amiibos(ctx):
    embed = discord.Embed()