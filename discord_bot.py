import os
import discord
from discord.ext import commands
import socket
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect
port = 10000

# Bind to the port
s.bind(('', port))

# Put the socket into listening mode
s.listen(5)

print('Server is listening')

# Replace 'YOUR_TOKEN_HERE' with your actual Discord bot token
TOKEN = os.getenv('TOKEN')

# Define intents
intents = discord.Intents.default()
intents.messages = True  # Enable the messages intent

# Set up the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)
# A forever loop until we interrupt it or 
# an error occurs
while True:

    # Establish a connection with the client
    c, addr = s.accept()

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
        print('------')
    
    # Command to respond to
    @bot.command()
    async def hello(ctx):
        await ctx.send('bye')
    
    # Command to ping the bot
    @bot.command()
    async def ping(ctx):
        await ctx.send('Bong! 🏓')

    # Close the connection with the client
    c.close()
# Event that triggers when the bot is ready

# Run the bot
bot.run(TOKEN)
