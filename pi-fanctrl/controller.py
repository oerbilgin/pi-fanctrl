"""
Controls fan speed based on CPU temperature.

TODO: Add multiple setpoints and interpolate between them
TODO: Add logging and plotting function
"""
from cpu_fan import CPUFan
import os

LOGPATH = os.path.expanduser('~/.logs')


def logger(cpu_temp, fan_speed):
    with open(os.path.join(LOGPATH, 'fanctrl.log'), 'a') as f:
        f.write(f"{{'cpu_temp': {cpu_temp}, 'fan_speed': {fan_speed}}},\n")

    print(
        f"{{'cpu_temp': {cpu_temp}, 'fan_speed': {fan_speed}}},"
        )


def main(dry_run=False):
    if not os.path.isdir(LOGPATH):
        os.makedirs(LOGPATH)
    print(f'Logs in: {LOGPATH}')

    fan_control = CPUFan(
        17,
        fan_max_rpm=1,
        logger=logger,
        temp_lb=60,
        temp_ub=70,
        min_pwm_strength=0.5,
        dry_run=dry_run)
    fan_control.start(poll_interval=1)


if __name__ == '__main__':
    main()
