# coding: utf-8
from __future__ import unicode_literals
import sys;reload(sys);sys.setdefaultencoding('utf8')

from flask import Flask, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

#english_bot = ChatBot("English Bot")
#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")

deepThought = ChatBot("deepThought")
deepThought.set_trainer(ChatterBotCorpusTrainer)
deepThought.train("chatterbot.corpus.chinese")

list = []
file = open('train_datas.txt')
try:
	for line in file:
		list.append(line.strip('\n'))
finally:
	file.close()
deepThought.set_trainer(ListTrainer)
deepThought.train(list)


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/get/<string:query>")
def get_raw_response(query):
	return str(deepThought.get_response(query).text)


if __name__ == "__main__":
	app.run()
