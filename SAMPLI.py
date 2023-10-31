import asyncio
from bale import Bot, Message
import tracemalloc


client = Bot(token="1811623771:iA5TFugS5sUTWl41nvHQNp5H6FjOQ2Y2mbZhmy8Y")

@client.event
async def on_ready():
    print(client.user, "is Ready!")

@client.event
async def on_message(message: Message):
    if message.content == '/give_name_without_timeout':
        await message.reply('what is your name?')
        def answer_checker(m: Message):
            print(m.author)
            tracemalloc.start()
# کد شما در اینجا قرار می‌گیرد
            return message.author == m.author and bool(message.text)
        answer_obj: Message = await client.wait_for('message', check=answer_checker)
        return answer_obj.reply(f'Your name is {answer_obj.content}')

    elif message.content == '/give_name_with_timeout':
        await message.reply('what is your name?')

        def answer_checker(m: Message):
            return message.author == m.author and bool(message.text)
        try:
            answer_obj: Message = await client.wait_for('message', check=answer_checker, timeout=10.0)
        except asyncio.TimeoutError:
            return await message.chat.send('No response received; Therefore, the operation was canceled.')
        else:
            return answer_obj.reply(f'Your name is {answer_obj.content}')

client.run()