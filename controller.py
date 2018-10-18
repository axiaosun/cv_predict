#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/prediction_chart', methods = ['GET'])
def visualization():
    if request.method == 'GET':
        return render_template('chart.html')
    else:
        pass

if __name__ == '__main__':
	app.run(debug = True)
