#angle between hands of clock

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour * 360) / 12 + (minutes * 360) / (12 * 60)
        m = (minutes * 360) / (60)
        angle = abs(h - m)
        angle = min(360 - angle, angle)
        return (angle)
        