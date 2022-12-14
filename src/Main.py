import discord
from discord.ext import commands
import asyncio
import json
import API
import EmbedHandler

intents = discord.Intents.all()

client = commands.Bot(command_prefix="$", intents=intents)


@client.event
async def on_ready():
    print(f"I have logged in as {client.user}")


@client.command()
async def joke(message: discord.Message):
    if message.author == client.user:
        return
    joke = API.Joke().get_joke_json()
    async with message.channel.typing():
        await asyncio.sleep(0.6)
    await message.channel.send(joke["setup"])

    def check(m: discord.Message):
        return m.author.id == message.author.id and m.channel.id == message.channel.id
    await client.wait_for("message", check=check)
    async with message.channel.typing():
        await asyncio.sleep(0.6)
    await message.channel.send(joke["punchline"])


@client.command()
async def meme(message: discord.Message):
    meme = API.Meme()
    meme.get_meme_json()
    meme.get_meme()
    async with message.channel.typing():
        await asyncio.sleep(0.6)
    await message.channel.send(file=discord.File("resources/meme.png"))


@client.command()
async def umd(message: discord.Message):
    embed = EmbedHandler.Embed()
    async with message.channel.typing():
        await asyncio.sleep(0.6)
    await message.channel.send(embed=embed.generate_default_main_embed())



def main():
    token = ""
    with open(file="resources/token.json", mode="r") as read:
        token = json.loads(read.read())

    client.run(
        token=token["discord_token"])


if __name__ == "__main__":
    main()
