import time
time.clock = time.time
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot('furry')
trainer = ListTrainer(bot)
trainer.train([
    'sure,wait for a minute',
    'Your flight is little late.'
])
response = bot.get_response('Booked')
print(response)
