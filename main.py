import discord
from random import randint

client = discord.Client()


@client.event
async def on_ready():
    print('Usuário {0.user} logado'.format(client))


@client.event
async def on_message(mensagem):
    if mensagem.author == client.user:
        return

    if mensagem.content.startswith('!Bot'):
        await mensagem.channel.send('PixelBot aqui')

    if mensagem.content.startswith('!D20'):
        await mensagem.channel.send(randint(1, 20))

client.run('Insert your Discord bot TOKEN here!')
