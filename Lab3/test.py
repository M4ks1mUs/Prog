from itertools import product
def z1():
    s1 = ['X', 'Z']
    s2 = ['A', 'B', 'C', 'D', 'E']
    cnt = 0
    for a1, a2, a3, a4 in product(s1, s1, s2, s2):
        cnt += 1
    print(cnt)

def z2():
    s = 49**10 + 7**30 - 49
    list = []
    while s > 0:
        list.append(s % 7)
        s //= 7
    print(list.count(6))

def z3():
    for x in range(312614, 312652):
        list = []
        for i in range(1, x + 1):
            if x % i == 0:
                list.append(i)
        if len(list) == 6:
            print(*sorted(list))

z1()
z2()
z3()