"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "robot" in user_message:
    return True
  if "follow what I do" == user_message:
    return True
  if "what sport do you like to play" in user_message:
    return True 
  if "what is your favorite color?" in user_message:
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
  if "follow what I do" == user_message:
    return "ok, tracking in progress "
  if "what sport do you like to play" in user_message:
    return "soccer"  
  if "what is your favorite color?" in user_message: 
    return "blue" 
