from operator import mul


def invert(list, *args):
    nova_lista = []
    for number in list:
        if number > 0:
            number = -abs(number)
        elif number < 0:
            number = abs(number)

        nova_lista.append(number)

    return nova_lista


print(invert([1, -2, 3, -4, 5]))

# def invert(lst):
#     return [ x * -1 for x in lst ]

# def invert(lst):
#     lst2=[]
#     for num in lst:
#         lst2.append(num*-1)
#     return lst2

# def invert(lst):
#     return [-x for x in lst]