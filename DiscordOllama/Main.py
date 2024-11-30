import discord
import Reply    
from Reply import ReplyIt
from discord.ext import commands

BOT_TOKEN = ""
MODEL = ""

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
Reply.initialize_chat_history()
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(f'{message.author.name} {message.content}')
    Reply = ReplyIt(f'{message.author.name}: {message.content}')
    print(f'{bot.user.name} {Reply}')
    await message.channel.send(Reply)
    await bot.process_commands(message)

try:
    bot.run(BOT_TOKEN)
except discord.errors.LoginFailure as e:
    print(f"Invalid bot token: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
