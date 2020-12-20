"""
Server version of Simon says

"""
import json

from flask import Flask, request

from Entities import User
from Lights.LightsManager import LightsManager
from Entities.Simon import Simon

app = Flask(__name__)
simon = None
lm = LightsManager()
user = None


@app.route('/start/', methods=['GET'])
def start():
    global user
    user = User.FlashyUser(lm)
    simon = Simon(user)
    simon.start()

    return "OK"


@app.route('/test/', methods=['GET'])
def ping():
    lm.flash_light(1)
    lm.flash_light(2)
    lm.flash_light(3)
    lm.flash_light(4)
    return "OK"


@app.route('/answer/', methods=['POST'])
def user_answer():
    ua = json.loads(request.data)

    answer = ua["answer"]
    user.answer(answer)

    return "OK"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=600)

