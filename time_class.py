class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __add__(self, other):
        total_minutes = self.hour * 60 + self.minute + other.hour * 60 + other.minute
        hour, minute = divmod(total_minutes, 60)
        return Time(hour=hour, minute=minute)

    def __sub__(self, other):
        total_minutes = self.hour * 60 + self.minute - (other.hour * 60 + other.minute)
        hour, minute = divmod(total_minutes, 60)
        return Time(hour=hour, minute=minute)

    def __gt__(self, other):
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour and self.minute > other.minute:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour and self.minute >= other.minute:
            return True
        else:
            return False

    def divide_time_in_parts(self, parts):
        total_minutes = self.hour * 60 + self.minute
        minutes_per_part = total_minutes // parts
        print(total_minutes)
        print(minutes_per_part)
        print(minutes_per_part/60)
        hours_per_part, minutes_left = divmod(minutes_per_part, 60)
        print(hours_per_part)
        return Time(hours_per_part, minutes_left)
