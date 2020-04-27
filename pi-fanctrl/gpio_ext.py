from gpiozero import CPUTemperature as old_CPUTemperature


# Overwrite existing value property to actually return btwn 0 and 1
# TODO: make PR for this
class CPUTemperature(old_CPUTemperature):
    def __init__(self, min_pwm_strength=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_pwm_strength = min_pwm_strength

    @property
    def value(self):
        """
        Returns the current CPU temperature as a value between 0.0
        (representing the *min_temp* value) and 1.0 (representing the
        *max_temp* value). These default to 0.0 and 100.0 respectively, hence
        :attr:`value` is :attr:`temperature` divided by 100 by default.
        """

        slope = (
            (1.0 - self.min_pwm_strength)
            / (self.max_temp - self.min_temp)
        )
        intercept = self.min_pwm_strength - self.min_temp * slope

        val = intercept + slope * self.temperature

        if val < self.min_pwm_strength:
            val = 0
        elif val > 1:
            val = 1

        return val


if __name__ == '__main__':
    cpu = CPUTemperature(min_pwm_strength=0.5, min_temp=55, max_temp=70)
    print(cpu.temperature, cpu.value)
