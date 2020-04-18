"""
Controls fan speed based on CPU temperature.

TODO: Add multiple setpoints and interpolate between them
TODO: Add logging and plotting function
"""

from gpiozero import PWMOutputDevice
from time import sleep
from gpio_ext import CPUTemperature


class CPUFan():
    """
    Sets up a Fan controller that modulates PWM voltage
    based on the CPU temperature.

    Args:
        fan_pin (int): GPIO pin to pass to PWMOutputDevice
        fan_max_rpm (int, optional): Maximum RPM of your fan, if known.
            Defaults to 100.
        temp_lb (int, optional): Lower bound of CPU temp, in Celsius.
            Temperatures at or below this value keep the fan off.
            Defaults to 50.
        temp_ub (int, optional): Upper bound of CPU temp, in Celsius.
            Temperatures at or above this value max out the fan.
            Defaults to 70.
    """
    def __init__(self, fan_pin, fan_max_rpm=100, temp_lb=50, temp_ub=70):
        """CPUFan init
        """
        self.fan = PWMOutputDevice(fan_pin)
        self.temp_reader = CPUTemperature(
            min_temp=temp_lb,
            max_temp=temp_ub,
            threshold=temp_ub)

        self.fan_max_rpm = fan_max_rpm

        self.fan.source = self.temp_reader

    @property
    def fan_speed(self):
        """
        Current fan speed

        Returns:
            float: PWM value multiplied by max fan RPM
        """
        return self.fan.value * self.fan_max_rpm

    @property
    def cpu_temp(self):
        """
        Current CPU temperature, in Celsius

        Returns:
            float: Current CPU Temperature
        """
        return self.temp_reader.temperature

    def start(self, poll_interval=1, log=True):
        """
        Start temperature monitoring and fan control

        Args:
            poll_interval (int): Poll the CPU temperature every
              x seconds. Defaults to 1.
            log (bool): Whether or not to log fan_speed and cpu_temp.
              Defaults to True.

        """
        while True:
            if log:
                print(self.fan_speed, self.cpu_temp)
            sleep(poll_interval)


def main():
    fan_control = CPUFan(17)
    fan_control.start()


if __name__ == '__main__':
    main()
