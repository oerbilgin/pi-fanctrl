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


def main(dry_run=False):
    fan_control = CPUFan(
        17,
        fan_max_rpm=1,
        logger=logger,
        temp_lb=50,
        temp_ub=70,
        min_pwm_strength=0.5,
        dry_run=dry_run)
    fan_control.start()


if __name__ == '__main__':
    main()
