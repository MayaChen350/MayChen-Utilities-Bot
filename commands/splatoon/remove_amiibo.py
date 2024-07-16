from discord.ext import commands
from commands.splatoon.edit_amiibo import update_amiibo_list

@commands.hybrid_command()
async def remove_amiibo(ctx, name: str):
    file = open("data/splatoon/amiibo_kits", "r")
    content : str = ""
    # Find if the name of the amiibo is in the list, so it will not include the old version
    for line in file:
        if line.split(',')[0] != name:
            content += line.strip("\n") + "\n"
    file.close()

    file = open("data/splatoon/amiibo_kits", "w")
    file.write(content)
    file.close()
    update_amiibo_list()
    await ctx.send("Done!")