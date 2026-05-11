#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def manage_zoo():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

    zoo.insert(1, 'bear')
    zoo_with_bear = zoo.copy()

    birds = ['rooster', 'ostrich', 'lark', ]
    zoo += birds
    zoo_with_birds = zoo.copy()

    zoo.remove('elephant')
    zoo_without_elephant = zoo.copy()
    
    lion_position = zoo.index('lion') + 1
    lark_position = zoo.index('lark') + 1
    
    return zoo_with_bear, zoo_with_birds, zoo_without_elephant, lion_position, lark_position