import random


def select_weekly_runs():
    monday_run = random.choice(["Gasworks", "Green Lake", "Ravenna"])
    tuesday_run = "Track"
    wednesday_run = random.choice(["Gasworks", "Bridge"])
    thursday_run = random.choice(["Arboretum", "Interlaken", "Laurelhurst"])
    friday_run = random.choice(["Capitol Hill", "Green Lake Zoo Loop", "Infamous Lake Union Loop", "Magnuson Park"])
    return [monday_run, tuesday_run, wednesday_run, thursday_run, friday_run]