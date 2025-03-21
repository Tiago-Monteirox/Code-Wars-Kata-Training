import math


def square_or_square_root(arr):
    new_array = []
    for n in arr:
        if math.sqrt(n) == int(math.sqrt(n)):
            i = int(math.sqrt(n))
            new_array.append(i)
        else:
            new_array.append(n**2)

    return new_array


print(square_or_square_root([4, 3, 9, 7, 2, 1 ]))

# def square_or_square_root(arr):
#     result = []
#     for x in arr:
#         root = x**0.5
#         if root.is_integer():
#             result.append(root)
#         else:
#             result.append(x*x)
#     return result

# return [int(sqrt(a)) if sqrt(a) % 1 == 0 else a ** 2 for a in arr]

