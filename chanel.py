from config import *

chanelId ="-1001964391098"

async def logC(Client,message):
  Name = message.from_user.first_name
  uName = message.from_user.username
  txt = message.text
  
  print(message)
  await app.send_message(chanelId,f"Name : {Name}\nUser name : {uName}\nRequested Movie : {txt}")