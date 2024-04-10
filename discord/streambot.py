import discord

# Intents declaration
intents = discord.Intents.all()
intents.guilds = True  # Enable the guilds intent
intents.members = True  # Enable the members intent
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    # This event is called when the bot has successfully connected to Discord
    print(f'We have logged in as {client.user}')

# Event decorator to register an event for message receiving
@client.event
async def on_message(message):
    # Print the message content to console
    print(f'Message from {message.author}: {message.content}')
    
    # Write the message content to log file
    with open('C:/Users/User/Desktop/discord/stream/log.txt', 'w') as file:
        file.write(f'Message from {message.author}: {message.content}\n')
        file.close() 


client.run('MTIyNzUyNjAxMTk3NDA2MjA5MA.G6CF0b.C-AttV1hS02ANzqqoC2TN0xIAURkqJsciocHFU')
