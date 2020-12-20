import random
import threading

"""
Simon server's logic
"""


class Simon(threading.Thread):

    def __init__(self, user):
        super().__init__()
        self.user = user

    def play(self):
        self.run()

    def run(self):
        success = True
        game = []

        print("New game started")
        self.user.start()
        while success:
            new_number = random.randint(1, 4)
            game.append(new_number)
            print("Round #{} - {}".format(len(game), game))
            success = self.user.turn(list(game))

        print("User successfully passed {} rounds, failed at round {}".format(len(game)-1, len(game)))
        self.user.finish()


