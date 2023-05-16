from dbs import *
from config import *
db = client['ramanan']
col = db['ramanan']



async def uploadMovie(msgId,chId,name,title,b):
  resul=col.find({"_id":b})
  i=0
  for ren in resul:
    i=i+1
  if i > 0:
    b=random.randrange(10000000)
  else:
    pass
  upData={"_id":b,"Name":name,"title":title,"messageId":msgId,"chanel":chId}
  col.insert_one(upData)
  print("done")




async def uploadData(Client,message,name,url,chanel):
  print("uplodinggg")
  data = {"name":name,"url":url,"chanel":chanel}
  col.insert_one(data)
  print("doneee")
  #await app.send_message(message.from_user.id,"uploded to data base")


async def movieSerc(Client,message,qury):
  resul=col.find({"name":qury})
  print(resul)
  i=0
  for rs in resul:
    i=i+1
    print(rs)
    name = rs["name"]
    url = rs["url"]
    button1=[
      [InlineKeyboardButton(f"👉 {name} 👈",url=url)
      ]
      ]
    bt = InlineKeyboardMarkup(button1)
    await message.reply_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzeZtCv67U_CkfkEb602B0Kpzw47rnl2Tjnw&usqp=CAU",caption="Thear is your result ",reply_markup=bt) 
  print(i)
  if i==0:
    await message.reply_text("സ്പെല്ലിങ് കറക്റ്റ് ആണോ എന്ന് ചെക്ക് ചെയുക \nഅല്ലെങ്കിൽ ആ മൂവി ഞങ്ങടെ  കയിൽ ഇല്ല ഉടനെ  അപ്‌ലോഡ് ചെയ്യുന്നേആയിരിക്കുംം ")
    await logC(Client,message)
  else:
    pass




async def uplodedData(Client,message):
  caption = message.caption
  splitC= caption.split("|")
  movieName = splitC[0]
  movieName = movieName.lower()
  title = splitC[1]
  chanelId=message.chat.id
  messageId=message.id
  gmt = time.gmtime()
  a = calendar.timegm(gmt)
  b=random.randrange(100000000000)
  c = str(a)
  d = str(b)
  e = c+d
  idd = int(e)
  await uploadMovie(messageId,chanelId,movieName,title,a)