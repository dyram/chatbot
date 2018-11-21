from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

while True:
	message = raw_input('You :')
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('ChatBot :',reply.text);
	if message.strip() == 'Bye':
		print('ChatBot : Bye')
		break
