class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def str_update(self, time):
        h, m, s = time.split(":")
        self.hours = int(h)
        self.minutes = int(m)
        self.seconds = int(s)

    def add_clocks(self, other_Clock):
        seconds = self.seconds + other_Clock.seconds
        extra_minutes, seconds = divmod(seconds, 60)

        minutes = self.minutes + other_Clock.minutes + extra_minutes
        extra_hours, minutes = divmod(minutes, 60)

        hours = self.hours + other_Clock.hours + extra_hours
        hours %= 24
        return Clock(hours, minutes, seconds)

    def __str__(self):
        out_str = "{} hours, {} minutes and {} seconds"
        return out_str.format(self.hours, self.minutes, self.seconds)


