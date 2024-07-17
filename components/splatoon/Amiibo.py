import discord
import requests

class Amiibo:
    def __init__(self, line : str = "", name : str = "", kit_1 : str = "", kit_2 : str = "", kit_3 : str = "", kit_4 : str = "", kit_5 : str = "") -> None:
        if line != "":
            splitted_line = line.split(",")
            self.name = splitted_line[0]
            self.kit_1 = splitted_line[1]
            self.kit_2 = splitted_line[2]
            self.kit_3 = splitted_line[3]
            self.kit_4 = splitted_line[4]
            self.kit_5 = splitted_line[5]
            self.kit_1_category = splitted_line[6]
            self.kit_2_category = splitted_line[7]
            self.kit_3_category = splitted_line[8]
            self.kit_4_category = splitted_line[9]
            self.kit_5_category = splitted_line[10]
        else:
            self.name = name
            self.kit_1 = kit_1
            self.kit_2 = kit_2
            self.kit_3 = kit_3
            self.kit_4 = kit_4
            self.kit_5 = kit_5
            self.kit_1_category = self.find_kit_category(self.kit_1)
            self.kit_2_category = self.find_kit_category(self.kit_2)
            self.kit_3_category = self.find_kit_category(self.kit_3)
            self.kit_4_category = self.find_kit_category(self.kit_4)
            self.kit_5_category = self.find_kit_category(self.kit_5)

    def __str__(self) -> str:
        return self.name + ',' + self.kit_1 + ',' + self.kit_2 + ',' + self.kit_3 + ',' + self.kit_4 + ',' + self.kit_5 + ',' + self.kit_1_category + ',' + self.kit_2_category  + ',' + self.kit_3_category + ',' +self.kit_4_category + ',' + self.kit_5_category 
    
    def find_kit_category(self, kit) -> str:
        weapon_category : str = ""
        for weapon in requests.get("https://stat.ink/api/v3/weapon").json():
            if weapon["name"]["en_US"] == kit.removesuffix('\n'):
                weapon_category = weapon["type"]["name"]["en_US"]
        return weapon_category.removesuffix('s')

    def create_embed(self) -> discord.Embed:
        embed = discord.Embed(title=self.name)
        embed.add_field(name="1. " + self.kit_1_category, value=self.kit_1, inline=False)
        embed.add_field(name="2. " + self.kit_2_category, value=self.kit_2, inline=False)
        embed.add_field(name="3. " + self.kit_3_category, value=self.kit_3, inline=False)
        embed.add_field(name="4. " + self.kit_4_category, value=self.kit_4, inline=False)
        embed.add_field(name="5. " + self.kit_5_category, value=self.kit_5, inline=False)
        
        return embed