# CHECK OUT README.TXT FOR INFORATION ABOUT HOW TO RUN THIS
# PLEASE CONSIDER DONATING. K THX BYE X)

import discord
from discord.ext import commands
import json
from xyz import xyz
import asyncio
import os
from keep_alive import keep_alive

with open('settings.json') as s:
  settings = json.load(s)

client = commands.Bot(command_prefix=settings['prefix'])
token = settings['token']

@client.event
async def on_ready():
  print(f'{client.user.name} is ready')

@client.event
async def on_message(message):
  if message.author.id == 365975655608745985:
    with open('settings.json') as s:
      settings = json.load(s)

    if message.channel.id in settings['allowed_channels_ids']:
      if message.embeds:
        if 'Guess' in message.embeds[0].description:
          url = message.embeds[0].image.url
          name = xyz(url).start()
          timer = settings['timer']

          await asyncio.sleep(timer)

          await message.channel.send(f'p!catch {name}')
  
  await client.process_commands(message)

@client.command()
async def trade(ctx):
  with open('settings.json') as s:
    settings = json.load(s)

  if ctx.channel.id in settings['allowed_channels_ids']:
    if ctx.author.id in settings['allowed_users_ids']:
      await ctx.send(f'p!trade {ctx.author.mention}')
      
      def check(m):
        return m.content == 'p!accept' and m.channel == ctx.channel and m.author == ctx.author

      msg = await client.wait_for('message',check = check)
      if msg:
        await ctx.send('p!pokemon')
        await asyncio.sleep(.3)
        await ctx.send('Enter the number of pokemon you wanna transfer (starting from 1) ex- `54` max- 300')

        def check(m):
          return m.channel == ctx.channel and m.author.id == ctx.author.id

        msg2 = await client.wait_for('message',check = check)
        if msg2:
          try:
            poks = int(msg2.content)
            temp = ''

            if poks <= 300:
              for x in range(1,poks+1):
                temp += str(x)
                temp += ' '
            else:
              await ctx.send('oh no! something\'s wrong')

            await ctx.send(f'p!p add {temp}')
            await asyncio.sleep(.3)
            await ctx.send('p!confirm')
            await asyncio.sleep(.3)
            await ctx.send('Press `p!confirm` to confirm the trade.')

              
          except:
            await ctx.send('oh no! something\'s wrong')


keep_alive()    
client.run(token,bot=False)