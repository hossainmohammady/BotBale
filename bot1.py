from balethon import Client
from balethon.conditions import at_state,private
from balethon.objects import InlineKeyboard
import pandas as pd



bot=Client(token="1400235071:ndoXjZefyWdE5bZfxQqQcXU27CYOPaTIp85MSIKI")


def search(value: str) -> str:
    # بارگذاری فایل اکسل
    df = pd.read_excel("list.xlsx",sheet_name="sheet1")

    # جستجو در ستون 'نام' با استفاده از str.contains
    results = df[df["نام"].str.contains(value, case=False, na=False)]

    if results.empty:
        return "موردی یافت نشد."

    # ایجاد خروجی قالب‌بندی‌شده
    output = "نتایج جستجو:\n\n"
    for _, row in results.iterrows():
        output += f"نام: {row['نام']}\n"
        output += f"کرایه پایه: {row['پایه']}\n"
        output += f"کرایه کل: {row['کل']}\n"
        output += f"آدرس: {row['آدرس']}\n"
        output += "-" * 30 + "\n"

    return output


@bot.on_message(private & at_state(None))
async def answer_message(message):
    await message.reply(
        "یک مورد را انتخاب کنید :",
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
    await message.reply(
        "یک مورد را انتخاب کنید :",
        InlineKeyboard(
            [("جستجوی کرایه", "search")],
            [("محاسبه کرایه", "price")]
        ))
    
@bot.on_message(private & at_state("search"))
async def answer_search(message):
    result= search(value=message.text)
    await message.reply(f"کرایه مورد نظر : {result}  ")
    message.author.del_state()
    await message.reply(
        "یک مورد را انتخاب کنید :",
        InlineKeyboard(
            [("جستجوی کرایه", "search")],
            [("محاسبه کرایه", "price")]
        ))
    
bot.run()
