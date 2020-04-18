"""
Controls fan speed based on CPU temperature.

TODO: Add multiple setpoints and interpolate between them
TODO: Add logging and plotting function
"""
from cpu_fan import CPUFan


def logger(cpu_temp, fan_speed):
    print(
        f"{{'cpu_temp': {cpu_temp}, 'fan_speed': {fan_speed}}},"
        )


def main():
    fan_control = CPUFan(17, logger=logger)
    fan_control.start()


if __name__ == '__main__':
    main()
