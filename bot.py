import asyncio
import pstats
from bale import Bot, Update, Message,Components,InlineKeyboard,CallbackQuery,MenuKeyboard, User
import xlrd 
client = Bot(token="1400235071:ndoXjZefyWdE5bZfxQqQcXU27CYOPaTIp85MSIKI")

def readData( name:str):
 loc="list.xls"
 work=xlrd.open_workbook(loc)
 sheet=work.sheet_by_index(0)
 find_value=None
 for row in range(sheet.nrows):
    cell_value = sheet.cell_value(row, 0)  # ستون اول
    if name in cell_value  :
        find_value=[sheet.cell_value(row,0),sheet.cell_value(row,1),sheet.cell_value(row,2),sheet.cell_value(row,3)]
        return find_value
	


@client.event
async def on_ready():
	print(client.user, "is Ready!")
	
@client.event
async def on_update(update:Update):
	print(update.update_id,update.type)
	

component = Components()
component.add_inline_keyboard(InlineKeyboard(text="لیست کرایه مقصد",callback_data="pricelist"))
component.add_inline_keyboard(InlineKeyboard(text="محاسبه کرایه",callback_data="price"),row=2)
@client.event
async def on_message(message: Message):
	if message.content == "/start":
		
		
		
		#kry=MenuKeyboard(text="محاسبه کرایه")
		#kry2=MenuKeyboard(text="لیست کرایه کل و پایه")
	
		# component.add_menu_keyboard(menu_keyboard=kry)
		# component.add_menu_keyboard(menu_keyboard=kry2,row=1)
	
		await message.reply(
			f"سلام {message.author.first_name}, به ربات دریافت اطلاعات کرایه انجمن کالای جوین خوش آمدید",
			components=component
		)
	if message.text=="لیست کرایه کل و پایه":
		await message.reply(text="نام گیرنده یا قسمتی از آن را وارد کنید :" )
	value=readData(message.text)
	if (value is not None):
		await message.reply(f"نام:  {value[0]}\nکرایه پایه :{int(value[1])}\nکرایه کل: {int(value[2])}\nآدرس :{value[3]}")
		
	else:
		
		await message.reply("موردی یافت نشد",components=component)
		
@client.event
async def on_user_input(message: User):
	pass

@client.event
async def on_callback(callback: CallbackQuery):
	if callback.data == "pricelist":
		await callback.message.reply("نام گیرنده یا قسمتی از آن را وارد کنید ")
	elif callback.data == "price" :
		await callback.message.reply("مقصد را وارد کنید :")


client.run()