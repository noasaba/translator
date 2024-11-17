import discord
import requests
import json
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
tree = bot.tree  # For slash commands

# JSON file to save settings
CONFIG_FILE = 'channel_config.json'

# Function to load settings
def load_config():
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"source_channel_id": None, "target_channel_id": None}

# Function to save settings
def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

# Load settings on startup
config = load_config()
source_channel_id = config.get("source_channel_id")
target_channel_id = config.get("target_channel_id")
print("Configuration loaded successfully.")
print(f"Source Channel ID: {source_channel_id}, Target Channel ID: {target_channel_id}")

def translate_text(text, target_lang='EN'):
    url = "https://api-free.deepl.com/v2/translate"
    params = {
        "auth_key": DEEPL_API_KEY,
        "text": text,
        "target_lang": target_lang
    }
    response = requests.post(url, data=params)
    return response.json()["translations"][0]["text"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    await tree.sync()  # Sync slash commands
    print("Slash commands have been synced")

@tree.command(name="set_channels", description="Set the source and target channels for translation")
async def set_channels(interaction: discord.Interaction, source: discord.TextChannel, target: discord.TextChannel):
    """Set the source (A) and target (B) channels using a slash command"""
    global source_channel_id, target_channel_id
    source_channel_id = source.id
    target_channel_id = target.id

    # Save settings
    save_config({"source_channel_id": source_channel_id, "target_channel_id": target_channel_id})
    
    await interaction.response.send_message(f"Source: {source.mention}\nTarget: {target.mention}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Check messages from the source channel
    if source_channel_id and target_channel_id and message.channel.id == source_channel_id:
        translated_text = translate_text(message.content)
        
        # Send the translation result to the target channel
        target_channel = bot.get_channel(target_channel_id)
        if target_channel:
            await target_channel.send(f"**Translated message from {message.author.name}:**\n{translated_text}")

    await bot.process_commands(message)

bot.run(TOKEN)
