import discord
import asyncio

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = 'MTIyNTQwNjAzNDg5NDUyMDQwMA.GSLFqT.YzbpDu3DDRdYu06hBmNXBmo370vVGvHwH3IlfY'

# Replace 'Dan's Channel ID' with the actual channel ID
dan_channel_id = 1225406610843762688

# Define intents
intents = discord.Intents.default()
intents.messages = True

# Create a Discord client with intents
client = discord.Client(intents=intents)

async def check_log_and_send():
    checker = ''
    while True:
        # Read the content of log.txt
        with open('log2.txt', 'r') as file:
            message = file.read()
        with open('log2.txt', 'w') as file:
            file.write('')
            
        
        # If there is content in the log file, send it to Dan's channel
        if (message != checker) and (message != ''):
            channel = client.get_channel(dan_channel_id)
            if channel:
                await channel.send(message)

        checker = message
        # Sleep for 60 seconds before checking again
        await asyncio.sleep(1)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    # Start the background task to check the log file and send messages
    client.loop.create_task(check_log_and_send())

@client.event
async def on_message(message):
    # Print the message content to the console
    if message.author != client.user:
        print(message.content)
        
        # Check if the message has any attachments
        attachments = message.attachments
        content = message.content
        
        # If there are attachments, append their URLs to the content
        if attachments:
            for attachment in attachments:
                content += f"\n{attachment.url}"
        
        for mention in message.mentions:
            content = content.replace(f'<@{mention.id}>', '')
            content = content.replace(f'<@!{mention.id}>', '')
    
    # Write the filtered message content to log.txt
    with open('log1.txt', 'w') as file:
        file.write(content)

# Run the bot
client.run(TOKEN)
