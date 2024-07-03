import discord
from discord.ext import commands
from config import TOKEN
import requests
import io
import PIL
from aiLogic import classificate_image


bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot started")


@bot.command()
async def s(ctx: commands.Context):
    if ctx.message.attachments:
        url = ctx.message.attachments[0]
        response = requests.get(url).content
        image = PIL.Image.open(io.BytesIO(response))
        class_name, confidence_score = classificate_image(image)
        await ctx.send(f"На картинке - {class_name} с вероятностью {confidence_score}% ")
    else:
        await ctx.send("Вы забыли добавить картинку")

bot.run(token=TOKEN)

