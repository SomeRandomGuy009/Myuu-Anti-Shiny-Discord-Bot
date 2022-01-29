import discord, time, os, datetime
from discord.ext import commands
from utils.parser import conf
from keep_alive import keep_alive
start_time = time.time()  
bot = commands.Bot(command_prefix='.')
     
def description(msg):
     embeds = msg.embeds
     for embed in embeds:
         description=str(embed.description)
         return description

@bot.event
async def on_ready():
    print(f"Started to look for Greninja-ash and shinies.")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Greninja-ash and shinies."))

@bot.command()
async def route(ctx):
    channel = bot.get_channel(conf.routingchannel) 
    if ctx.channel.id == conf.routingchannel:
            poke = await bot.wait_for('message', check = lambda m: m.author.id == 438057969251254293 and m.channel == ctx.channel, timeout=5)
            if poke.embeds != []:
               if "Lv36 Greninja-Ash" in description(poke):
                    channel1 = bot.get_channel(conf.loggingchannel)
                    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
                    overwrite.send_messages = False
                    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                    msg = await channel.fetch_message(channel.last_message_id)
                    await channel1.send(embed=msg.embeds[0])
                    await ctx.send('Channel locked because Greninja-Ash was found.')  
                    time.sleep(30)
                    await ctx.send('Channel Unlocked.')
                    await channel.set_permissions(ctx.guild.default_role, send_messages=True)

            if "★" in description(poke):
                    channel1 = bot.get_channel(conf.loggingchannel)
                    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
                    overwrite.send_messages = False
                    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                    msg = await channel.fetch_message(channel.last_message_id)
                    await channel1.send(embed=msg.embeds[0])
                    await ctx.send('Channel locked because Shiny was found.') 
                    time.sleep(30)
                    await ctx.send('Channel Unlocked.')
                    await channel.set_permissions(ctx.guild.default_role, send_messages=True)   

            if f"{conf.custompoke}" in description(poke):
                    channel1 = bot.get_channel(conf.loggingchannel)
                    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
                    overwrite.send_messages = False
                    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                    msg = await channel.fetch_message(channel.last_message_id)
                    await channel1.send(embed=msg.embeds[0])
                    await ctx.send(f'Channel locked because a {conf.custompoke} was found.') 
                    time.sleep(30)
                    await ctx.send('Channel Unlocked.')
                    await channel.set_permissions(ctx.guild.default_role, send_messages=True)                  
 
@bot.command()
async def ping(ctx):
    if round(bot.latency * 1000) <= 50:
        embed=discord.Embed(title="Latency", description=f"The ping is **{round(bot.latency *1000)}** ms!", color=0x44ff44)
    elif round(bot.latency * 1000) <= 100:
        embed=discord.Embed(title="Latency", description=f"The ping is **{round(bot.latency *1000)}** ms!", color=0xffd000)
    elif round(bot.latency * 1000) <= 200:
        embed=discord.Embed(title="Latency", description=f"The ping is **{round(bot.latency *1000)}** ms!", color=0xff6600)
    else:
        embed=discord.Embed(title="Latency", description=f"The ping is **{round(bot.latency *1000)}** ms!", color=0x990000)
    await ctx.send(embed=embed)
@bot.command()
async def uptime(ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)

keep_alive()
bot.run(os.environ["TOKEN"])
