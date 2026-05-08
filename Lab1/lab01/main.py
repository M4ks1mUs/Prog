from circle import calculate_circle
from distance import calculate_distances
from favorite_movies import extract_movies
from garden import garden_meadow
from my_family import get_family_info
from operations import calculate_expression
from secret import decode_message
from shopping import create_sweets_dict
from songs_list import calculate_songs_duration
from store import calculate_store_inventory
from zoo import manage_zoo

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
