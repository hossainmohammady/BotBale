
from balethon import Client
from balethon.conditions import at_state,private,group,regex
from balethon.objects import InlineKeyboard
import pandas as pd

bot=Client(token="1400235071:ndoXjZefyWdE5bZfxQqQcXU27CYOPaTIp85MSIKI")

user_data={}
start_key=InlineKeyboard(
            [("جستجوی کرایه", "search")],
            [("محاسبه کرایه", "price")]
        )

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

    await message.reply("یک مورد را انتخاب کنید :",start_key)


@bot.on_message(group & regex("کرایه"))
async def group_message(message):
    word=message.text.split()
    if len(word)>2:
        return
    await message.chat.send_action("typing")
    result=search(word[1])
    await message.reply(f"کرایه مورد نظر :{result}" )

@bot.on_callback_query(at_state("price2"))
async def answer_price2(callback_query):
    result=price_func(callback_query.data)
    paye=result["پایه"]
    col=result["کل"]
    user_data[callback_query.author.id]={"name":callback_query.data,"paye": paye ,"col":col  }
    await callback_query.answer("وزن خالص را وارد کنید:")
    callback_query.author.del_state()
    callback_query.author.set_state("waight")

@bot.on_callback_query(private)
async def answer_callback_query(callback_query):
     if callback_query.data=="price":
        await callback_query.answer("مقصد مورد نظر را وارد کنید \n نام مقصد یا نام شهر کفایت می کند")
        callback_query.author.set_state("price")
     if callback_query.data=="search":
        await callback_query.answer("مقصد مورد نظر را وارد کنید \n نام مقصد یا نام شهر کفایت می کند")
        callback_query.author.set_state("search")



@bot.on_message(private & at_state("search"))
async def answer_search(message):
    await message.chat.send_action("typing")
    result= search(value=message.text)
    await message.reply(f"کرایه مورد نظر : {result}  ",start_key)
    message.author.del_state()




def price_func(value: str) -> str:
    # بارگذاری فایل اکسل
    df = pd.read_excel("list.xlsx",sheet_name="sheet1")

    # جستجو در ستون 'نام' با استفاده از str.contains
    results = df[df["نام"].str.contains(value, case=False, na=False)]

    if results.empty:
        return None

    return results

@bot.on_message(private & at_state("price"))
async def answer_price(message):
    await message.chat.send_action("typing")
    result =price_func(value=message.text)
    # ایجاد خروجی قالب‌بندی‌شده
    output=""

    if result is None:
        await message.reply("موردی یافت نشد.",start_key)
        message.author.del_state()
    else:
        for _, row in result.iterrows():
            output += f"نام: {row['نام']}\n"
            output += f"کرایه پایه: {row['پایه']}\n"
            output += f"کرایه کل: {row['کل']}\n"
            output += f"آدرس: {row['آدرس']}\n"
            output += "-" * 30 + "\n"
            await message.reply(f"{output}\n درصورت صحیح بودن مقصد مورد نظر آن را تایید کنید",InlineKeyboard([("تایید",row["نام"])]))
            output=""
        message.author.del_state()
        message.author.set_state("price2")






@bot.on_message(at_state("waight"))
async def answer_waight(message):
    waight=message.text
    try:
        waight = int(waight)
    except ValueError:
        await message.reply("❌ لطفاً وزن خالص را به صورت عدد صحیح وارد کنید.")
        return
    await message.chat.send_action("typing")
    user_id=message.author.id
    paye=user_data[user_id]["paye"]
    col=user_data[user_id]["col"]
    result_paye=int(waight)*int(paye)
    result_col=int(waight)*int(col)
    result_paye="{:,}".format(result_paye)
    result_col="{:,}".format(result_col)
    await message.reply(
        f'''📦 کرایه محاسبه شده:
    💰 کرایه پایه: {result_paye} تومان
    💰 کرایه کل: {result_col} تومان
⚠️ لطفاً مبلغ حق بیمه را نیز در نظر بگیرید.''',start_key)
    message.author.del_state()

bot.run()
