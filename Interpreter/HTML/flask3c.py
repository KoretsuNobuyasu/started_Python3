#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# Created by nobuskate on 2018/01/14.

# import
from flask import Flask, render_template, request


# class


app = Flask(__name__)

@app.route('/echo/')
def echo():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['place'] = request.args.get('place')
    return render_template('flask3.html',**kwargs)


def main():
    app.run(port=9999, debug=True)
    return 0


if __name__ == '__main__':
    main()