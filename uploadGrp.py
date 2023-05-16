from config import *
from mong import *


Name=""
url=""
chanel=""

async def chekking(Client,message):
  text=message.text
  if text=="!up":
    await updata(Client,message)
  else:
    pass




async def updata(Client,message):
  chekWich=message.text[0]
  if chekWich=="›":
    global chanel
    print("done")
    tempc = message.text
    print("done")
    chanel = tempc.replace("›","")
    await message.reply_text("അതുപോലെ അദ്യം #ഇട്ടട്ടു മിവിയുടെ name കൊടുക്ക്")
  elif chekWich == "#":
    global Name
    tempN = message.text
    Name = tempN.replace("#","")
    await message.reply_text("ലാസ്റ്റ് aa ഫയലിന്റ്റ് url ₹ കൊടുക്ക്")
  elif chekWich == "₹":
    global url
    tempu = message.text
    url = tempu.replace("₹","")
    await message.reply_text("അവസനും ഡാറ്റബാസിലോട്ട് അപ്‌ലോഡ് ചെയ്യാൻ + എന്ന് കൊടുക്ക്‌")
  elif chekWich == "+":
    if len(Name) > 3 and len(chanel) > 3 and len(url) > 3:
      await uploadData(Client,message,Name,url,chanel)
    else:
      await message.reply_text("Niggale Endhokkeyo miss chythattunde !helpe ennu send chyeu")
    #print(Name)
    #print(chanel)
    #print(url)
  elif message.text == "!help":
    await commands(Client,message)
  else:
    text = "This message has <b>bold</b> and <i>italic</i> text."
    await Client.send_message(message.chat.id, text, parse_mode="HTML")
   #await message.reply_text("!help ennu send cheyu")
  
    
    
  
async def commands(Client,message):
  await message.reply_text(" › ee simpel ettu chanalintte username send cheyu")
  await message.reply_text(" # ee simpel ettu movieude name send cheyu")
  await message.reply_text(" ₹ ee simpel ettu movieude url send cheyu")
  await message.reply_text("avasanm ethokke databasilotte uplod cheyan + send chyu")
  await message.reply_text("pretheykam sredhikkuva adhym simpel ettukazhinju space kanalle angane vannal databasil uplod chyumpol adhym space kanum")
  await message.reply_text("athupole ellam curet ay type chythu kazhinje upload cheyavu")





async def getUplodData(Client,message):
  data=message.text[0]
  if data=="!":
    global Name
    #print(Name)
    
    
    #print(Name)
    await message.reply_text("Name was saved", quote=True)
  elif data== "$":
    #print("url")
    global url
    tempName = message.text
    url = tempName.replace("$","")
    await message.reply_text("url was saved", quote=True)
  elif data== "^":
    #print("up")
    if len(Name) > 1 and len(url) > 5:
      await message.reply_text("uploding to database", quote=True)
      await uploadData(Client,message,Name,url)
      #print("suss")
      #print(len(Name)
    else:
      await message.reply_text("Name and url id requird")
    #print(Name)