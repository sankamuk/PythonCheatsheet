def day_counter(nth_day):
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for c, d in zip(range(nth_day), week_days):
        yield d