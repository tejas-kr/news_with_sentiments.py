from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
from urllib import request as req
from textblob import TextBlob


app = Flask(__name__)
app.secret_key = '#@ck|><|@tk@r0b#@!'

def analyse(news):
	sample = TextBlob(news)
	if sample.sentiment.polarity > 0:
		return '🙂'
	elif sample.sentiment.polarity == 0:
		return '😔'
	else:
		return '😞'

app.jinja_env.globals.update(analyse=analyse)

@app.route('/')
def index():
	url = req.urlopen('http://www.hindustantimes.com/rss/topnews/rssfeed.xml')
	soup = bs(url, 'xml')
	headlines = [text for text in soup.find_all('title')]
	news = [text for text in soup.find_all('description')]
	return render_template('analyse.html', headlines=headlines, news=news)

if __name__ == "__main__":
	app.run(debug=True)