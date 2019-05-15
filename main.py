import discord, asyncio, random, os
from discord.ext import commands
from datetime import datetime

config=os.environ

class RageFrog(commands.Bot):
  def __init__(self):
    super().__init__(command_prefix=config['PREFIX'])
    self.config = config
    self.startup_extensions = ['modules.events'
                              ]
    self.path = os.path.dirname(os.path.realpath(__file__))
  
  async def on_ready(self):
    self.loop.create_task(self.presence())
  
  async def presence(self):
    while not self.is_closed():
      await self.change_presence(
        activity=discord.Streaming(
          name=random.choice(
            (
              "ragefrog",
              "sadfrog",
              "tiredfrog",
              "winkfrog",
              "normalfrog"
            )
          ),
          url='https://twitch.tv/mer'
        ),
      )
      await asyncio.sleep(45)
      
  def run(self):
    loaded=0
    for extension in self.startup_extensions:
      try:
        self.load_extension(extension)
        loaded +=1
      except Exception as er:
        print(er)
      print(f"Loaded {loaded} cogs")
      
      
    super().run(self.config['TOKEN'],reconnect=True)
        
if __name__ == "__main__":
  RageFrog().run()
