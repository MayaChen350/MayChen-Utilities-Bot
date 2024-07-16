import discord
from discord.ui import View, Button

class LeftRightMenu(View):
        def __init__(self, pages : list):
            super().__init__()
            self.value = None
            self.pages = pages
            self.update_button()

        page_index = 0

        def update_button(self):
            self.children[0].disabled = self.page_index == 0 # type: ignore
            self.children[1].disabled = self.page_index + 1 == len(self.pages) # type: ignore

        async def update_embed(self, interaction : discord.Interaction):
            embed = discord.Embed(description=self.pages[self.page_index])
            embed.clear_fields()
            await interaction.response.edit_message(embed=embed, view=self)

        @discord.ui.button(style=discord.ButtonStyle.primary,label="Prev")
        async def prev(self, interaction : discord.Interaction, button : Button):
            self.page_index -= 1
            self.update_button()
            await self.update_embed(interaction)

        @discord.ui.button(style=discord.ButtonStyle.primary,label="Next")
        async def next(self, interaction : discord.Interaction, button : Button):
            self.page_index += 1
            self.update_button()
            await self.update_embed(interaction)
