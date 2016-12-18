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
months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

for year in range(1901, 1902):
    for i, month in enumerate(months):
        for days in range(1, month + 1):
            print(year, i+1, days, month)
