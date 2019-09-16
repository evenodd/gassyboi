import requests
import time
from typing import Callable

class Sensor:
    def __init__(self, disconnect_handler : Callable, reconnect_handler : Callable, url : str = "http://172.19.79.88:8000/",):
        self.url = url
        self.disconnect_handler = disconnect_handler
        self.reconnect_handler = reconnect_handler
        self.connected = True

    def sample(self) -> (int, int):
        while True:
            try:
                resp = requests.get(self.url)
                if (not self.connected):
                    self.connected = True
                    self.reconnect_handler()
            except Exception as e:
                if (self.connected):
                    self.connected = False
                    print("Failed to connect to sensor: %s" % e)
                    self.disconnect_handler()
            if (self.connected):
                break
            time.sleep(1)

        content = resp.content.decode("utf-8").split(",")
        print("Sensor values CO2: %s ppm, VOC: %s ppb" % (content[0], content[1]))
        return (int(content[0]), int(content[1]))

