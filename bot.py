import asyncio
from bale import Bot, Update, Message,Components,InlineKeyboard,CallbackQuery,MenuKeyboard
client = Bot(token="1400235071:ndoXjZefyWdE5bZfxQqQcXU27CYOPaTIp85MSIKI")

def readData( name:str):
	exec

@client.event
async def on_ready():
	print(client.user, "is Ready!")
	


@client.event
async def on_update(update:Update):
    print(update.update_id,update.type)
    
@client.event
async def on_message(message: Message):
	if message.content == "/start":
		
		
		component = Components()
		# component.add_inline_keyboard(InlineKeyboard(text="what is python-bale-bot?", callback_data="python-bale-bot:help"))
		# component.add_inline_keyboard(InlineKeyboard(text="محاسبه کرایه",callback_data="dil"),row=2)
		# component.add_inline_keyboard(InlineKeyboard(text="محاسبه کرایه",callback_data="dil"),row=2)
		kry=MenuKeyboard(text="محاسبه کرایه")
		kry2=MenuKeyboard(text="لیست کرایه کل و پایه")
	
		component.add_menu_keyboard(menu_keyboard=kry)
		component.add_menu_keyboard(menu_keyboard=kry2,row=1)
	
		await message.reply(
			f"*Hi {message.author.first_name}, Welcome to python-bale-bot bot*",
			components=component
		)
	if message.text=="محاسبه کرایه":
		await message.reply(text="نام شهر محل تخلیه را وارد کنید :" )
	

@client.event
async def on_callback(callback: CallbackQuery):
	
	if callback.data == "python-bale-bot:help":
		await callback.message.reply(
			"*python-bale-bot* is a Python library for building bots on the Bale messenger platform. Bale is a messaging app that provides a secure and private messaging experience for users. The python-bale-bot library provides a simple and easy-to-use interface for building bots on the Bale platform, allowing developers to create bots that can send and receive messages, handle events, and perform various actions on behalf of users."
		)

client.run()