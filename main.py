from config import *
from pm import *
from chanel import *
from group import *
from uploadGrp import *
from testgroup import *


uploadGorupId=-1001885448827
db_chanel=-1001917544445

@app.on_message(filters.all)
async def mainf(Client,message,):
  typs = message.chat.type
  typs = str(typs)
  if typs == "ChatType.CHANNEL":
    fromId=message.chat.id
    if fromId == db_chanel:
      await uplodedData(Client,message)
    
    #print(message)
    #await logC(Client,message,"tedt")
  elif typs == "ChatType.SUPERGROUP":
    #print(message)
    if message.chat.id == uploadGorupId:
      pass
      #await updata(Client,message)
    else:
      #print(message)
      if message.service:
        #print("login")
        pass
      else:
        await test(Client,message)
    
  elif typs == "ChatType.PRIVATE":
    await messageBot(Client,message)
  else:
    #print(message)
    pass
    #print("i dont under stand")
  







print('runnig   ')
app.run()