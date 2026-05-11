#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_family_info():
    my_family_height = [
        ['Алексей', 174],
        ['Лариса', 165],
        ['Марк', 182],
        ['Макарий', 186],
        ['Максим', 184],
        ['Миша', 178],
        ['Маша', 164]
    ]

    father_height = f'Рост отца - {my_family_height[0][1]} см'
    summ = my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1]+my_family_height[3][1]+my_family_height[4][1]+my_family_height[5][1]+my_family_height[6][1]
    total_height = f'Общий рост моей семьи - {summ} см'

    return father_height, total_height