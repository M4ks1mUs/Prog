#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def extract_movies():
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

    first = my_favorite_movies[0:10]
    last = my_favorite_movies[42:57]
    second = my_favorite_movies[12:25]
    second_from_end = my_favorite_movies[27:33]
    
    return first, last, second, second_from_end