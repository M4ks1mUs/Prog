#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_circle(radius, point_1, point_2):
    circle_area = round(3.1415926 * radius**2, 4)

    distance_p1 = (point_1[0]**2 + point_1[1]**2) ** 0.5
    result_1 = distance_p1 <= radius

    distance_p2 = (point_2[0]**2 + point_2[1]**2) ** 0.5
    result_2 = distance_p2 <= radius

    return circle_area, result_1, result_2
