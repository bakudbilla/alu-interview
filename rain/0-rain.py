#!/usr/bin/python3
""" Rain -This  calculates amount of water retained"""


def rain(walls):
    """It  Calculates how many squares units of water
    will be retained after it rains"""

    water = 0
    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for k in range(i + 1, len(walls)):
            right = max(right, walls[k])
        water += min(left, right) - walls[i]

    return water
