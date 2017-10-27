from flask import Flask
app = Flask(__name__)
from garage import toggleDoor, getGarageState, fakeGetGarageState
from flask import render_template

# isOpen=getGarageState()
isOpen=False
isMoving=False


@app.route("/garageToggle")
def garageToggle():
    # toggleDoor()
    # isOpen = fakeGetGarageState(isOpen)
    return isOpen

@app.route('/')
def garageUI():
    return render_template('garageUI.html',isOpen=isOpen)

@app.route('/test')
def hello_world():
    return 'Hello, World!'


def main():
    app.run(host='0.0.0.0', port=80)


if __name__ == '__main__':
    main()