from flask import Flask
app = Flask(__name__)
from hub import *


@app.route("/singleStrobe")
def callSingleStrobe():
    return

@app.route('/doubleStrobe')
def callDoubleStrobe():
    return

@app.route('/rainbowStrobe')
def callRainbowStrobe():
    return

@app.route('/doubleRainbowStrobe')
def callRainbowStrobe():
    return

@app.route('/normalize ')
def callRainbowStrobe():
    return


def main():
    app.run(host='0.0.0.0', port=80)


if __name__ == '__main__':
    main()