import discord
from discord.ext import commands
from discord import app_commands
from components.ui.ViewAmiiboMenu import ViewAmiiboMenu
from components.splatoon.Amiibo import Amiibo
import requests


@commands.hybrid_command()
async def view_amiibos(ctx):
    file = open("data/splatoon/amiibo_kits", "r")
    amiibo_list = []
    for l in file:
        amiibo_list.append(Amiibo(line=l))
    file.close()
    amiibo_list.reverse()
    view = ViewAmiiboMenu(amiibo_list)
    await ctx.send(embed=amiibo_list[0].create_embed(),view=view)