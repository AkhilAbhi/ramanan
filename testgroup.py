from config import *
from dbs import *
from chanel import *

db = client['ramanan']
col = db['ramanan']





async def test(Client,message):
  qury = message.text
  qury = qury.lower()
  print(qury)
  resul=col.find({"Name":qury})
  #button = InlineKeyboardButton("Open URL", url=url)
  keyboard = []
  i=0
  for rs in resul:
    i=i+1
    #print(rs)
    ms = rs["_id"]
    m = rs["chanel"]
    
    ur = f"https://t.me/ramanan_talkies_bot?start={ms}"
    button = InlineKeyboardButton(rs["title"], url=ur)
    row = [button]
    keyboard.append(row)
  inline_keyboard = InlineKeyboardMarkup(keyboard)
  #button2 = InlineKeyboardButton("Open URL", url=url)
  #bt=[InlineKeyboardButton("Open URL", url=url),InlineKeyboardButton("Open URL", url=url)]
  #keyboard = InlineKeyboardMarkup([[bt]])
  if i > 0:
    await message.reply_text(f"Here is what i found for your query ({message.text})", reply_markup=inline_keyboard)
  else:
    await message.reply_text(f"sorry i can't find any movie!! ({message.text})\nCheck if the spelling is correct")
    await logC(Client,message)
    
  #print("test")
 
