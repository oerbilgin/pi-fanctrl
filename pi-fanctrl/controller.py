"""
Controls fan speed based on CPU temperature.

TODO: Add multiple setpoints and interpolate between them
TODO: Add logging and plotting function
"""

from gpiozero import PWMOutputDevice
from time import sleep
from gpio_ext import CPUTemperature


class FanController():
    def __init__(self, fan_pin, temp_lb=50, temp_ub=70):
        self.fan = PWMOutputDevice(fan_pin)
        self.temp_reader = CPUTemperature(
            min_temp=temp_lb,
            max_temp=temp_ub,
            threshold=temp_ub)

        self.fan.source = self.temp_reader

    @property
    def fan_speed(self):
        return self.fan.value

    @property
    def cpu_temp(self):
        return self.temp_reader.temperature

    def start(self):
        while True:
            print(self.fan_speed, self.cpu_temp)
            sleep(1)


def main():
    fan_control = FanController(17)
    fan_control.start()


if __name__ == '__main__':
    main()
