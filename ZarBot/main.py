import discord
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    pass
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!ping'):
    embed = discord.Embed(title="Ping de prueba", color=0xFFFFFF)
    embed.add_field(
        name="Ping de prueba realizado para comprobar que el bot funciona.",
        value=(""),
        inline=False)
    await message.channel.send(embed=embed)


keep_alive()
client.run('MTE2MzQzMzM2MjczMjYxNzczOA.GkhjM-.C6Bs1pUJJLQly6DYX_ruXf8fJNi9tlnZnNkgK0')
