#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def garden_meadow(garden, meadow):
    garden_set = set(garden)
    meadow_set = set(meadow)

    all_flowers = garden_set.union(meadow_set)

    garden_and_meadow = garden_set.intersection(meadow_set)

    only_garden = garden_set.difference(meadow_set)

    only_meadow = meadow_set.difference(garden_set)

    return all_flowers, garden_and_meadow, only_garden, only_meadow
