# -*- coding: utf-8 -*-

"""
Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some research
for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4,
    but not on a Jahrhundert unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
first_sundays = []
d = 1

for year in range(1900, 2001):
    if year % 100:  # kein Jahrhundert
        if not year % 4:  # Schaltjahr
            months[1] = 29
    elif not year % 400:  # Jahrhundert, aber durch 400 Teilbar, Schaltjahr
        months[1] = 29
    for idx, month in enumerate(months):
        for day in range(1, month + 1):
            if day == 1 and d == 7 and year > 1900:
                first_sundays.append((year, idx + 1, day, d))
            if d == 7:
                d = 1
            else:
                d += 1

    months[1] = 28

print(len(first_sundays))
