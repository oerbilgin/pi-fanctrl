"""
Controls fan speed based on CPU temperature.

TODO: Make a class in gpiozero style
TODO: Add multiple setpoints and interpolate between them
TODO: Add logging and plotting function
"""

from gpiozero import PWMOutputDevice
from time import sleep
from gpio_ext import CPUTemperature

def main():
    temp = CPUTemperature(min_temp=50, max_temp=70, threshold=70)
    
    fan = PWMOutputDevice(17)
    fan.source = temp

    while True:
        print(temp.temperature, fan.value)
        sleep(1)

if __name__ == '__main__':
    main()