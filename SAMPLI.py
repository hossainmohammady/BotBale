

import asyncio
from bale import * #CallbackQuery, Components,Message,Bot,Update,InlineKeyboard,MenuKeyboard,User,*
import xlrd
client=Bot(token="1400235071:ndoXjZefyWdE5bZfxQqQcXU27CYOPaTIp85MSIKI")
KeyPad=Components()
KeyPad.add_inline_keyboard(InlineKeyboard(text="دریافت کرایه",callback_data="price"))
# KeyPad.add_inline_keyboard(InlineKeyboard(text="محاسبه کرایه",callback_data="calc"),row=2)


# async def Read_Data(name:str):
#     print(name)
#     pm=Message()
#     loc="list.xls"
#     work=xlrd.open_workbook(loc)
#     sheet=work.sheet_by_index(0)
#     find_value=None
#     for row in range(sheet.nrows):
#         cell_value = sheet.cell_value(row, 0)  
#         if name in cell_value  :
#             pm.reply(text=f"نام:{sheet.cell_value(row,0)} \nپایه: {int(sheet.cell_value(row,1))} \n کل:{int(sheet.cell_value(row,2))} \n آدرس:{sheet.cell_value(row,3)}",components=KeyPad)

#             return find_value
	

@client.event
async def on_ready():
    print(client.user,"is ready!")

@client.event
async def on_update(update:Update):
    print(update.update_id,update.type)


@client.event
async def on_message(Pm:Message):
    if Pm.content=="/start":
        await Pm.reply(text=f"سلام {Pm.author.first_name} ,\n به ربات انجمن جوین خوش آمدید",components=KeyPad)
    if Pm.content!="نام مقصد یا قسمتی از آن را وارد کنید:":
    #if Pm.content == '/give_name_without_timeout':
        def answer_checker(m: Message):
            return Pm.author == m.author and bool(Pm.text)
        answer_obj: Message = await client.wait_for('message', check=answer_checker)
        # answer_obj.content
        name= answer_obj.content
        loc="list.xls"
        work=xlrd.open_workbook(loc)
        sheet=work.sheet_by_index(0)
        find_value=None
        for row in range(sheet.nrows):
            cell_value = sheet.cell_value(row, 0)  
            if name in cell_value  :
                await Pm.reply(text=f"نام:{sheet.cell_value(row,0)} \nپایه: {int(sheet.cell_value(row,1))} \n کل:{int(sheet.cell_value(row,2))} \n آدرس:{sheet.cell_value(row,3)}",components=KeyPad)
                find_value=([sheet.cell_value(row,0)],[sheet.cell_value(row,1)],[sheet.cell_value(row,2)],[sheet.cell_value(row,3)])
                #break
        if find_value==None:
        # if find_value=="None":
        #     print(find_value)
                await Pm.chat.send(text=f"برای |{answer_obj.content} |موردی یافت نشد!",components=KeyPad)

    
        def answer_checker(m: Message):
            return Pm.author == m.author and bool(Pm.text)
        try:
            answer_obj: Message = await client.wait_for('message', check=answer_checker, timeout=10.0)
        except asyncio.TimeoutError:
            return await Pm.chat.send('زمان پاسخگویی به اتمام رسید مجدد درخواست دهید:',components=KeyPad)
        # else:
        #     return await answer_obj.reply(f'Your name is {answer_obj.content}')

        



@client.event
async def on_callback(callback:CallbackQuery):
    print(callback.data)
    if callback.data=="price":
       await callback.message.reply(text="نام مقصد یا قسمتی از آن را وارد کنید:")
    elif callback.data=="calc":
        await callback.message.reply(text="نام مقصد یا قسمتی از آن وارد کنید:")
        #wait_for(on_message)

client.run()