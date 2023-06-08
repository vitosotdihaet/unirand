import discord
import random


async def send_message(message, msg, private):
    try:
        response = get_response(msg)
        if private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(f'[ERRO] Could not send message: {e}!')


full_range = (0x20, 0xFFFF)
alchemical_range = (0x1F700, 0x1F77F)

def get_response(msg: str) -> str:
    msg = msg.lower()

    if msg[:len('unirand')] == 'unirand':
        if len(msg) > len('unirand') and msg[len('unirand') + 1:][0].isdigit():            
            return '# ' + generate_random_unicode(int(msg[len('unirand') + 1:]))
        else:
            return '# ' + generate_random_unicode(1)
        

def generate_random_unicode(n: int, random_range=full_range) -> str:
    if n == 0: n = 1
    random_bytes = [random.randint(random_range[0], random_range[1]) for _ in range(n)]
    return ''.join(map(chr, random_bytes))