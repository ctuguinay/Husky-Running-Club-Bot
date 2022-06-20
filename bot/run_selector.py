import random


def select_weekly_runs():
    monday_run = random.choice(["gasworks", "green_lake", "ravenna"])
    tuesday_run = "track"
    wednesday_run = random.choice(["gasworks", "bridge"])
    thursday_run = random.choice(["arboretum", "interlaken", "laurelhurst"])
    friday_run = random.choice([1, 2, 3, 4])
    return [monday_run, tuesday_run, wednesday_run, thursday_run, friday_run]

print(select_weekly_runs())
