def is_palindrom(list):
    if list == list[::-1]:
        return True
    else:
        return False

def is_palindrom_rec(list):
    if len(list) <= 1:
        return True
    if list[0] != list[-1]:
        return False
    return is_palindrom_rec(list[1: -1])

def get_x(i):
    if i <= 3:
        return 1
    x_1 = 1
    x_2 = 1
    x_3 = 1
    for n in range(4, i+1):
        x_i = x_3 + x_1
        x_1 = x_2
        x_2 = x_3
        x_3 = x_i
    return x_i

def get_x_rec(i):
    if i <= 3:
        return 1
    return get_x_rec(i-1) + get_x_rec(i-3)

print(is_palindrom([1,2,3,2,1]))
print(is_palindrom_rec([1,2,3,2]))
print(get_x(3))
print(get_x_rec(12))