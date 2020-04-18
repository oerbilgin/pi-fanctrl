from gpiozero import CPUTemperature as old_CPUTemperature

# Overwrite existing value property to actually return btwn 0 and 1
# TODO: make PR for this
class CPUTemperature(old_CPUTemperature):
    @property
    def value(self):
        """
        Returns the current CPU temperature as a value between 0.0
        (representing the *min_temp* value) and 1.0 (representing the
        *max_temp* value). These default to 0.0 and 100.0 respectively, hence
        :attr:`value` is :attr:`temperature` divided by 100 by default.
        """
        temp_range = self.max_temp - self.min_temp
        val = (self.temperature - self.min_temp) / temp_range
        if val < 0:
            val = 0
        elif val > 1:
            val = 1
        return val
