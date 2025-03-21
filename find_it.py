from collections import Counter


def find_it(seq):
    counter = Counter(seq)
    for num in counter:
        if counter[num] % 2 != 0:
            return num


# def find_it(seq):
#     counter = {}
#     for num in seq:
#         counter[num] = counter.get(num, 0) + 1
#
#     for num in counter:
#         if counter[num] % 2 != 0:
#             return num
#

# for num in seq:
#     if seq.count(num) % 2 != 0:
#         return num

    # for i in seq:
    #     if seq.count(i)%2!=0:
    #         return i

# return [x for x in seq if seq.count(x) % 2][0]