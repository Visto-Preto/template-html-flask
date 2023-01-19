#!/usr/bin/python

#coding: UTF-8
from flask import Flask, render_template, url_for
import os


__author__ = "VistoPreto"

app = Flask(__name__)

@app.route('/')
def	homepage():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")

