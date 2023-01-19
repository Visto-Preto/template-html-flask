#coding: UTF-8
from flask import Flask, render_template, url_for
import os

class Cache_Medias():
	def cache_create():
		path_videos = os.listdir("static/videos")
		for i in path_videos:
			os.system(r"ffmpeg -i static/videos/{} static/cache/{}.png -n".format(i, i[:-4]))

		path_cache = os.listdir("static/cache")
		return path_cache


__author__ = "VistoPreto"

app = Flask(__name__)

@app.route('/')
def	homepage():
	return render_template('index.html', path_cache = Cache_Medias.cache_create())

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")

