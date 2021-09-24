import os
import discord
from dotenv import load_dotenv



client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run("ODg3Mzc3MzU3OTAyNTk0MDU4.YUDQkA.l4o9e7C0-TUtj7maqJ16c3D70Rs")
