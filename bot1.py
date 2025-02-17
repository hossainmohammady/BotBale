from balethon import Client
from balethon.conditions import at_state,private
from balethon.objects import InlineKeyboard
import pandas as pd



bot=Client(token="1400235071:ndoXjZefyWdE5bZfxQqQcXU27CYOPaTIp85MSIKI")


def search(value):
    # بارگذاری فایل Excel
    df = pd.read_excel("list.xlsx", sheet_name="sheet1")
    
    # جستجو در ستون مشخص
    results = df[df["نام"].str.contains(value, case=False, na=False)]
    
    # نمایش نتایج جستجو
    if not results.empty:
        return results
    else:
        return "مقدار جستجو شده یافت نشد."


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
    result= search(value=message.text)
    print( result.to_string())
    await message.reply(f"کرایه مورد نظر : {result.to_string()}  ")
    message.author.del_state()
    
bot.run()
