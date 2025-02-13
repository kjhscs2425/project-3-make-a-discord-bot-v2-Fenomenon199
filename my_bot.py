"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "follow what I do" == user_message.lower():
    return True
  if "what sport do you like to play" in user_message.lower():
    return True 
  if "what is your favorite color?" in user_message.lower():
    return True
  if "Do you have any siblings?" in user_message.lower(): 
    return True 
  if "Do you have any pets?" in user_message.lower(): 
    return True 
  if "what is your favorite subject in school?" in user_message.lower(): 
    return True  
  if "What do you do for your job?" in user_message.lower(): 
      return True 
  if "do you like your job?" in user_message.lower(): 
      return True 
  if "Whats your favorite way to spend a weekend?" in user_message.lower(): 
    return True 
  if "What is your favorite cuisine?" in user_message. lower() : 
    return True 
  else: 
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  if "follow what I do" == user_message.lower():
    return "ok, tracking in progress "
  if "what sport do you like to play" in user_message. lower():
    return "soccer"  
  if "what is your favorite color?" in user_message.lower(): 
    return "blue" 
  if "Do you have any siblings?" in user_message.lower(): 
    return "I have no siblings" 
  if "Do you have any pets?" in user_message.lower():
    return " I have a dog and three cats" 
  if "what is your favorite subject in school?" in user_message.lower():  
    return " math is my favorite subject in school" 
  if "What do you do for your job?" in user_message.lower(): 
    return "I work for a corporate buisness " 
  if "do you like your job?" in user_message.lower():
    return  "It can be challenging at times" 
  if "Whats your favorite way to spend a weekend?" in user_message.lower(): 
    return " Going to the beach"
  if "What is your favorite cuisine?" in user_message.lower():
    return "Thai food"