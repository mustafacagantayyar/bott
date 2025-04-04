from discord.ext import commands
import discord
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.contect.startswith("çevre kirliliğinin zararları ne?") or message.contect.startswith("çevre kirliliğinin zararları ne").lower:
        await message.channel.send("enerji kıtlığı,beslenme sorunları, canlı çeşitliliğinin azalması, toprakların kaybı, sağlık problemleri de gelişerek canlı yaşamının devamlılğını tehdit eder.")

bot.run("token buraya")
