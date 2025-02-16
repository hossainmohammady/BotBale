from balethon import Client
from balethon.conditions import at_state,private
from balethon.objects import InlineKeyboard



bot=Client(token="1400235071:ndoXjZefyWdE5bZfxQqQcXU27CYOPaTIp85MSIKI")

@bot.on_message(private & at_state(None))
async def answer_message(message):
    await message.reply(
        "Click a button!",
        InlineKeyboard(
            [("جستجوی کرایه", "search")],
            [("محاسبه کرایه", "price")]
        )
    )


@bot.on_callback_query()
async def answer_callback_query(callback_query):
     if callback_query.data=="price":
        await callback_query.answer("مقصد مورد نظر را وارد کنید \n نام مقصد یا نام شهر کفایت می کند")
        callback_query.author.set_state("price")
     if callback_query.data=="search":
        await callback_query.answer("مقصد مورد نظر را وارد کنید \n نام مقصد یا نام شهر کفایت می کند")
        callback_query.author.set_state("search")

@bot.on_message(private & at_state("price"))
async def answer_price(message):
    await message.reply("مقصد مورد نظر  :   ")
    message.author.del_state()
    
@bot.on_message(private & at_state("search"))
async def answer_search(message):
    await message.reply("کرایه مورد نظر :   ")
    message.author.del_state()
    
bot.run()
