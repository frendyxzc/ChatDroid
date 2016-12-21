# coding: utf-8
from __future__ import unicode_literals
import sys;reload(sys);sys.setdefaultencoding('utf8')

import json
from flask import Flask, render_template
from flask import request
from flask import redirect
from flask import jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

#english_bot = ChatBot("English Bot")
#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")

chatDroid = ChatBot("chatDroid")
chatDroid.set_trainer(ChatterBotCorpusTrainer)
chatDroid.train("chatterbot.corpus.chinese")

list = []
file = open('train_datas.txt')
try:
	for line in file:
		list.append(line.strip('\n'))
finally:
	file.close()
chatDroid.set_trainer(ListTrainer)
chatDroid.train(list)


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/get/<string:query>")
def get_raw_response(query):
	return str(chatDroid.get_response(query).text)

@app.route('/chat', methods=['POST'])
def register():
	print request.headers
	print request.form['input']
	return str(chatDroid.get_response(request.form['input']).text)

if __name__ == "__main__":
	app.run()
