from config import *
from dbs import *

db = client['ramanan']
col = db['ramanan']


@app.on_message(filters.command(["start"]))
async def my_handler(client, message):
  print(message)
  data = message.command[1] if len(message.command) > 1 else None
  if data:
    data = int(data)
    resul=col.find_one({"_id":data})
    #print(resul)
    #-1001917544445
    userId=int(message.from_user.id)
    messid=resul['messageId']
    chanl=resul['chanel']
    chanl = int(chanl)
    chek=True
    async for member in app.get_chat_members(-1001943870424):
      groupUser=member.user.id
      groupUser = int(groupUser)
      if groupUser == userId:
        chek=True
        #print("yes user inthe group")
        break
      else:
        chek=False
        #print("no user inthe group")
    if chek:
      await client.forward_messages(chat_id=message.from_user.id,from_chat_id=chanl,message_ids=int(messid)
      )
      #print(data)
    else:
      ttt =[
        [InlineKeyboardButton("🔒 JOIN NOW 🔒",url="https://t.me/RamananTalkies")
        ],[InlineKeyboardButton("👉 Retry 👈",url=f"https://t.me/ramanan_talkies_bot?start={data}")
        ]]
      print(data)
      rr = InlineKeyboardMarkup(ttt)
      fname=message.from_user.first_name
      await message.reply_text(f"Hello {fname} \nyou have not joined our group please join\n and try agine😊😊",reply_markup=rr)
      
      pass
  else:
    name = message.from_user.first_name
    await app.send_message(message.from_user.id,f"hay {name} i am ramanan bot for created in ramanan talkies group \ncreated by @akhilBabhi and @Ambrozz0 🙂🙂")









async def messageBot(client,message):
  
  ms = [
    "hay" , "Hay" , "hello" , "Hello" , "hai" , "Hai" , "helo" , "Helo"
    ]
  #print(ms)
  tt =[
  [InlineKeyboardButton("👉 JOIN NOW 👈",url="https://t.me/RamananTalkies")
    ]
   ]
  r = InlineKeyboardMarkup(tt)
  text = message.text
  if text in ms:
    await app.send_photo(message.from_user.id, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRijGlLrA-xsLksBJPydH6yEfabPsKfcEankg&usqp=CAU")
    await app.send_message(message.from_user.id,"Helo Endhanu moylalikku vendathu")
  else:
    await message.reply_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzeZtCv67U_CkfkEb602B0Kpzw47rnl2Tjnw&usqp=CAU",caption="👇👇👇👇👇👇👇👇👇👇👇👇👇\n\nIf you want any movies then join our group\n\n👇👇👇👇👇👇👇👇👇👇👇👇👇",reply_markup=r)
