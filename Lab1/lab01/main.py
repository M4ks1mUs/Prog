from distance_00 import calculate_distances
from circle_01 import calculate_circle
from operations_02 import calculate_expression
from favorite_movies_03 import extract_movies
from my_family_04 import get_family_info
from zoo_05 import manage_zoo
from songs_list_06 import calculate_songs_duration
from secret_07 import decode_message
from garden_08 import garden_meadow
from shopping_09 import create_sweets_dict
from store_10 import calculate_store_inventory

def main():
    print('Задание 0')
    print(calculate_distances(sites = {'Moscow': (550, 370),
                                    'London': (510, 510),
                                    'Paris': (480, 480),}))
    print('Задание 1')
    print(calculate_circle(42, (23, 34), (30, 30)))
    print('Задание 2')
    print(calculate_expression())
    print('Задание 3')
    print(extract_movies())
    print('Задание 4')
    print(get_family_info())
    print('Задание 5')
    print(manage_zoo())
    print('Задание 6')
    print(calculate_songs_duration())
    print('Задание 7')
    print(decode_message())
    print('Задание 8')
    print(garden_meadow(('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', ), 
                        ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )))
    print('Задание 9')
    print(create_sweets_dict())
    print('Задание 10')
    print(calculate_store_inventory())

if __name__ == '__main__':
    main()
