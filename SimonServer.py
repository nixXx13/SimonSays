import json

from flask import Flask, request

import User
from LightsManager import LightsManager
from Simon import Simon

app = Flask(__name__)
simon = None
lm = LightsManager()
user = User.FlashyUser(lm)


@app.route('/start/', methods=['POST'])
def start():
    simon = Simon(user)
    simon.start()

    return "OK"


@app.route('/answer/', methods=['POST'])
def user_answer():
    ua = json.loads(request.data)

    answer = ua["answer"]
    user.answer(answer)

    return "OK"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=600)

