import discord
from components.ui.LeftRightMenu import LeftRightMenu
from components.splatoon.Amiibo import Amiibo


class ViewAmiiboMenu(LeftRightMenu):
    def __init__(self, pages : list[Amiibo]):
        super().__init__(pages)

    async def update_embed(self, interaction : discord.Interaction):
        embed = self.pages[self.page_index].create_embed()
        await interaction.response.edit_message(embed=embed, view=self)