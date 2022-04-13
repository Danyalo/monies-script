from telethon import TelegramClient
import re

api_id = 11111111 # get it from https://my.telegram.org
api_hash = '11111111111111111111111111111111' # get it from https://my.telegram.org

monies_id = -11111111111111 # obtain the chat id
id_1 = 11111111 # first user's id
id_2 = 11111111 # the other user's id

client = TelegramClient('anon', api_id, api_hash)


async def main():
    sum_1 = 0
    sum_2 = 0

    async for message in client.iter_messages(monies_id):
        print(message.sender_id, message.text)

        # needed because iter_messages appends a Null massage to the list for some reason
        if (message.text is None):
            continue

        number_str = re.search(r'\d+', message.text).group()
        number = int(number_str)
        print(number)

        if (message.sender_id == id_1):
            sum_1 += number
        elif(message.sender_id == id_2):
            sum_2 += number

    user_1 = (await client.get_entity(id_1)).username
    user_2 = (await client.get_entity(id_2)).username

    message = f'{user_1}\'s sum: {str(sum_1)}\n'
    message += f'{user_2}\'s sum: {str(sum_2)}\n'

    diff = abs(sum_1 - sum_2)

    message += f'Diff: {str(diff)}\n'

    if (sum_1 > sum_2):
        message += f'{user_2} should pay: {str(diff / 2)}'
    elif (sum_1 < sum_2):
        message += f'{user_1} should pay: {str(diff / 2)}'
    else:
        message += 'You\'re even.'

    print(message)
    await client.send_message(monies_id, message)


with client:
    client.loop.run_until_complete(main())
