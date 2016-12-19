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
	return str(deepThought.get_response(query).text)

@app.route("/chat/", methods=['GET', 'POST'])
def get_response(query):
	if request.method == 'POST':
		input = request.args.get('input')
		ans = str(chatDroid.get_response(input).text)
		dict1 = json.loads(ans)
		return json.dumps(dict1["resp"])
	else:
		return '<h1>只接受post请求！</h1>'


if __name__ == "__main__":
	app.run()
