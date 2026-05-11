#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_distances(sites):
    keys = list(sites.keys())

    # расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    distances = {
        f'{keys[0]}-{keys[1]}':(((sites[keys[0]][0] - sites[keys[1]][0]) ** 2 + (sites[keys[0]][1] - sites[keys[1]][1]) ** 2) ** 0.5),
        f'{keys[0]}-{keys[2]}' :(((sites[keys[0]][0] - sites[keys[2]][0]) ** 2 + (sites[keys[0]][1] - sites[keys[2]][1]) ** 2) ** 0.5),
        f'{keys[1]}-{keys[2]}' :(((sites[keys[1]][0] - sites[keys[2]][0]) ** 2 + (sites[keys[1]][1] - sites[keys[2]][1]) ** 2) ** 0.5)
    }

    return distances
