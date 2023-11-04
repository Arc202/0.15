import random
import discord
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
      
    async def on_message(self, message):
      if message.content[0] == '!':
        match message.content:
          case "!3doors":
            import random
          

random_number = random.randint(1, 100)
print(random_number)
          case "!hello":
            await message.channel.send('dang wasgud my homie')
          case default: await message.channel.send('error')

  
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTA5MDQxMzMyMDk0ODk1NzI2NQ.G11gNw.NjZMrEQHUnT9uDcNzMxeOIWdIYV174961McpNI')
