import time


class LightsManager:

    def __init__(self, light_delay=0.5):
        self.light_delay = light_delay

    def flash_sequence(self, lights_list):
        if len(lights_list) == 0:
            # TODO warning
            return

        last_light = lights_list.pop()
        for light in lights_list:
            self.flash_light(light, self.light_delay)

        # to signify last light in sequence - double delay
        self.flash_light(last_light, 2*self.light_delay)


    def flash_all_lights(self):
        print("light up in port '{}'".format(1))
        print("light up in port '{}'".format(2))
        print("light up in port '{}'".format(3))
        print("light up in port '{}'".format(4))
        time.sleep(self.light_delay)
        print("light off in port '{}'".format(1))
        print("light off in port '{}'".format(2))
        print("light off in port '{}'".format(3))
        print("light off in port '{}'".format(4))
        time.sleep(self.light_delay)

    def flash_light(self, port, delay = None):
        if delay is None:
            delay = self.light_delay
        print("light up in port '{}'".format(port))
        time.sleep(delay)
        print("light off in port '{}'".format(port))
        time.sleep(delay)
