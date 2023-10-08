from datetime import datetime

class Time:
    def __init__(self, oclock, minute, second):
        if 0 <= oclock <= 23 and 0 <= minute <= 59 and 0 <= second <= 59:
            self.oclock = oclock
            self.minute = minute
            self.second = second
        else:
            raise ValueError("Wrong time!")

    def format_time(self):
        return f"{self.oclock:02d}:{self.minute:02d}:{self.second:02d}"

    def format_time_usa(self):
        if self.oclock < 12:
            time_am_pm = "AM"
        else:
            time_am_pm = "PM"

        am_pm_oclock = self.oclock if self.oclock <= 12 else self.oclock - 12
        return f"{am_pm_oclock:02d}:{self.minute:02d}:{self.second:02d} {time_am_pm}"

    def minutes_difference_from_now(self):
        time_now = datetime.now().time()
        time_diff = abs((self.oclock * 60 + self.minute) - (time_now.hour * 60 + time_now.minute))
        return time_diff


def sort_time(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j].minutes_difference_from_now() > arr[j + 1].minutes_difference_from_now():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

times = [Time(15, 58, 3), Time(4, 18, 3), Time(12, 0, 0)]

sort_time(times)

for time in times:
    print(time.format_time(), "|", time.format_time_usa(), end=" | ")
    print(f"Difference: {time.minutes_difference_from_now()} minutes")
