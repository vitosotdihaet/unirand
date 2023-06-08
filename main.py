import discord
import os
import response


token = ''

def get_token():
    global token

    if os.path.exists('./token.txt'):
        token = open('token.txt', 'r').readline()
    else:
        print('No token file is found! (token.txt)')


def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'[INFO] {client.user} is alive!!!')

    @client.event
    async def on_message(message):
        if client.user == message.author: return

        # author = str(message.author)
        msg = str(message.content)
        # channel = str(message.channel)

        await response.send_message(message, msg, False)

    client.run(token)


if __name__ == '__main__':
    get_token()

    if token != '':
        run_bot()