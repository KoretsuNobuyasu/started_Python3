#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/11.

# import
from flask import Flask, render_template

# class

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('flask2.html')


@app.route('/echo/<thing>')
def echo(thing):
    return render_template('flask2.html', thing=thing)

app.run(port=9999, debug=True)



if __name__ == '__main__':
    main()