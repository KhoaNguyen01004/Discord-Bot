import discord
from discord.ui import Select


class Embed:

    def generate_default_main_embed(self, embed_title: str = "UMD Information", embed_description: str = "Get information about UMD courses. Please select your option to see more info", embed_url: str = "https://www.umd.edu/", embed_color=discord.Colour.red(), image_url: str = "https://brand.umd.edu/uploads/images/informal-seal.png"):
        embed_object = discord.Embed(
            color=embed_color, title=embed_title, description=embed_description, url=embed_url)
        embed_object.set_image(url=image_url)
        embed_object.set_author(name="umd.io", url="https://beta.umd.io/")
        return embed_object

    def generate_drop_menu(self):
        select = Select(placeholder="Options")
        select.add_option(label="Get Courses List",
                          description="Get the available courses list")
        return select
