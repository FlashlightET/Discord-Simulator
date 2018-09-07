import markovify
import nltk
import re #regex
import random
import discord
import asyncio
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("NAME")
with open("SCRAPED MESSAGE DATA GOES HERE.txt") as f:
    text = f.read()

text_model = markovify.Text(text, state_size=2)

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence



client = discord.Client()

async def bot():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id='CHANNEL ID GOES HERE')
    while not client.is_closed:
        UN = '**' + random.choice(open('NAMES LIST GOES HERE.txt').readlines()) + '**'
        temp = text_model.make_sentence()
        if temp is not None: temp2 = UN + temp
        #await channel.webhooks()
        if temp is not None: await client.send_message(channel, temp2)
        await asyncio.sleep(random.randint(1, 30))



        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(bot())
client.run('TOKEN')
