import discord
import asyncio
import youtube_dl
from discord.ext import commands
import requests as rq
from discord import opus

static void UpdatePresence()
{
    DiscordRichPresence discordPresence;
    memset(&discordPresence, 0, sizeof(discordPresence));
    discordPresence.startTimestamp = 1507665886;
    discordPresence.endTimestamp = 1507665886;
    discordPresence.smallImageKey = "ap_550x550_12x12_1_transparent_t_u1";
    discordPresence.smallImageText = "Rogue - Level 10000";
    discordPresence.partyId = "ae488379-351d-4a4f-ad32-2b9b01c91657";
    discordPresence.partySize = 200;
    discordPresence.partyMax = 5;
    discordPresence.spectateSecret = "MTIzNDV8MTIzNDV8MTMyNDU0";
    discordPresence.joinSecret = "MTI4NzM0OjFpMmhuZToxMjMxMjM= ";
    Discord_UpdatePresence(&discordPresence);
}

@bot.event
async def on_ready():
    print(bot.user.name)

@bot.command(pass_context=True)
async def leave(msg):
    """
    Leave the voice channel, clear the songs list and stop the audio
    Command: s.leave
    Example: s.leave
    """
    if msg.message.server.id in players:
        await bot.voice_client_in(msg.message.server).disconnect()
        players[msg.message.server.id]['bonjour']=None

    if msg.message.author.voice_channel == bot.user.voice_channel:
        await bot.voice_client_in(msg.message.server).disconnect()


@bot.command(pass_context=True)
async def join(msg):
    """
    Join a voice channel that you are currently in
    Command: s.join
    Example: s.join
    """
    if msg.message.author.voice_channel != None:
        await bot.join_voice_channel(msg.message.author.voice_channel)
    else:
        await bot.say("Vous devez être dans un canal vocal pour utiliser cette commande")

@bot.command(pass_context=True)
async def pause(msg):
    """
    Pause the current audio streamer
    Command: s.pause
    Example: s.pause
    """
    if msg.message.server.id in players:
            
            if players[msg.message.server.id]['bonjour'] == False:
			 await bot.say("yo sa cake ")
        else:
            await bot.say("Pas de son dans le canal vocal")

bot.run('CakeDog Bot is online')
