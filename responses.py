# Used to import the library we need!
import random

# This is used to call up the messages function!
def get_response(message: str) -> str:
    p_message = message.lower()
    

   # And now here are the command(s) this is used to make the bot reply to our messages "!example" 
    if p_message == '!example':
        return 'Hello this is an example!'
    
