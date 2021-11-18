
import os
import requests
import discord
import json
import random
import datetime
from dotenv import load_dotenv

client = discord.Client()
load_dotenv()
Token= os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for !gas"))

@client.event

async def on_message(message):
    if message.content.startswith("!gas"):
        get_info = requests.get("https://etherchain.org/api/gasnow")
        if get_info.status_code == 200:
            get_detail =json.loads(get_info.text)
            safe = (round(get_detail['data']['standard']/1000000000))
            low = (round(get_detail['data']['slow']/1000000000))
            fast =(round(get_detail['data']['fast']/1000000000))
            rapid =(round(get_detail['data']['rapid']/1000000000))


        colours = [2196352,7590622,9383254]
        embedColor = random.choice(colours)



        embed = discord.Embed(title="Eth Gas Fees (in Gwei)", color=embedColor)
        embed.set_thumbnail(url="WHATEVER YOU WANT THE IMAGE TO BE")
        embed.add_field(name="Time", value= datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        embed.add_field(name="Rapid", value=rapid)
        embed.add_field(name="Fast", value=fast)
        embed.add_field(name="Standard", value=safe)
        embed.add_field(name="Low", value=low)
        await message.channel.send(embed=embed)

client.run(Token)



    

