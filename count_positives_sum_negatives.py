# from itertools import count


# def count_positives_sum_negatives(arr):
#     new_array = []
#     for n in arr:
#         if n > 0:
#             count(arr)
#             new_array.append(x)
#         elif n < 0:
#             Sum = sum(arr)
#             new_array.append(Sum)
#         else:
#             return []
#     return new_array

#    pos = sum(1 for x in arr if x > 0)
#     neg = sum(x for x in arr if x < 0)
#     return [pos, neg] if len(arr) else []

#   output = []
#   if arr:
#     output.append(sum([1 for x in arr if x > 0]))
#     output.append(sum([x for x in arr if x < 0]))
#   return output

# if not arr: return []
#     pos = 0
#     neg = 0
#     for x in arr:
#       if x > 0:
#           pos += 1
#       if x < 0:
#           neg += x
#     return [pos, neg]

def count_positives_sum_negatives(arr):
    return [len([i for i in arr if i > 0]), sum([i for i in arr if i < 0])] if len(arr) != 0 else []




