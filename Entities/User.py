from queue import Queue

"""
Simon users logic
"""


class User:

    """
    This method should be implemented by sub classes.
    it is used in turn method
    """
    def _get_user_input(self):
        raise Exception("Not implemented")

    """
    This method is used by the hosting server and invokes uses's turn
    """
    def turn(self, game):

        while len(game) > 0:

            user_input = self._get_user_input()
            expected_num = game.pop(0)
            if not same_numbers(user_input, expected_num):
                # print("User entered {}, expected {}.Returning False".format(user_input, expected_num))
                return False

            # print("User entered same as expected {}".format(user_input))
        return True

    def start(self):
        print("Starting")

    def finish(self):
        print("Finished")


class CmdUser(User):

    def _get_user_input(self):
        return input()


class FlashyUser(User):

    def __init__(self, lights_manager):
        self.queue = Queue()
        self.game_on = True
        self.lights_manager = lights_manager

    """
    server pulls user's input from queue.
    queue is filled in answer method.
    """
    def _get_user_input(self):
        answer = self.queue.get()
        self.lights_manager.flash_light(answer)
        return answer

    def answer(self, answer):
        if self.game_on:
            self.queue.put(answer)

    def start(self):
        self.lights_manager.flash_all_lights()
        self.game_on = True

        # making sure queue is empty
        if not self.queue.empty():
            print("Queue had {} old msgs. clearing queue".format(self.queue.qsize()))
            while not self.queue.empty():
                self.queue.get()

        super().start()

    def turn(self, game):
        self.lights_manager.flash_sequence(list(game))
        return super().turn(game)

    def finish(self):
        self.lights_manager.flash_all_lights()
        self.game_on = False
        super().finish()

def same_numbers(a, b):
    return "{}".format(a) == "{}".format(b)

