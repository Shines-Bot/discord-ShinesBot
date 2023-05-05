# This code is used to call up the bots token and commands the token will then be called up again in "main.py" and it also is used to make the bots respones to-
# Messages and functions like "?" and "!".

# This is where we call up the commands and the "discord.py" library.

import discord
import responses

# Here we store the token, create it's messages and call up Discord Intents.

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

# Here is the token.

def run_discord_bot():
    TOKEN = 'SHINESBOTTOKEN'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

# Here is the function that makes the bot's activity/presence. 

    @client.event
    async def on_ready(): await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help"))
    print(f'Shines Bot💫#9825 is now running!')

# Here is the code that makes the private messages command.
    
    @client.event
    async def on_message(message):

        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
            
    # After all of the other functions we finnaly run the bot and call it up in "main.py"

    client.run(TOKEN)
