#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/11.

# import
from flask import Flask
# class


app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
    return thing


def main():
    app.run(port=9999, debug=True)
    return 0


if __name__ == '__main__':
    main()