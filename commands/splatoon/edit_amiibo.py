import discord
from discord.ext import commands
from discord import app_commands
import requests

from components.splatoon.Amiibo import Amiibo

weapon_list = [] # list of any available splatoon 3 weapons in the game
for weapon in requests.get("https://stat.ink/api/v3/weapon").json():
    weapon_list.append(weapon["name"]["en_US"])

amiibo_list = [] # list of the amiibo's names in the amiibo_kits file

def update_amiibo_list() -> None:
    amiibo_list.clear()
    file = open("data/splatoon/amiibo_kits", "r")
    for line in file:
        amiibo_list.append(line.split(',')[0])
    file.close()
    
update_amiibo_list()

async def veemo(interaction : discord.Interaction, current : str) -> list[app_commands.Choice[str]]:
    w_list = [] # list of the weapon's name (en_US)
    index : int = 0
    for weapon in weapon_list:
        if current.lower() in weapon.lower():
            w_list.append(app_commands.Choice(name=weapon,value=weapon))
            index = index + 1
        if index == 10:
            break
    # weapon_list.append(app_commands.Choice(name="weapon",value="weapon"))
    # weapon_list.append(app_commands.Choice(name="wdddeapon",value="ddweapon"))
    return w_list

async def get_amiibo_name(interaction : discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
    a_list = [] # list of the amiibos recorded in the files
    index : int = 0
    for amiibo in amiibo_list:
        if current.lower() in amiibo.lower():
            a_list.append(app_commands.Choice(name=amiibo,value=amiibo))
            index = index + 1
        if index == 10:
            break
    return a_list

@commands.hybrid_command()
@app_commands.autocomplete(name=get_amiibo_name,kit_1=veemo,kit_2=veemo,kit_3=veemo,kit_4=veemo,kit_5=veemo)
async def edit_amiibo(ctx, name: str, kit_1 : str, kit_2: str, kit_3: str, kit_4 : str, kit_5 : str):
    new_amiibo : Amiibo = Amiibo(name, kit_1, kit_2, kit_3, kit_4, kit_5)

    file = open("data/splatoon/amiibo_kits", "r")
    content : str = ""
    # Find if the name of the amiibo is in the list, so it will not include the old version
    for line in file:
        if line.split(',')[0] != name:
            content += line.strip("\n") + "\n"
    file.close()

    file = open("data/splatoon/amiibo_kits", "w")
    file.write(content + str(new_amiibo))
    file.close()
    update_amiibo_list()
    await ctx.send("Done!")