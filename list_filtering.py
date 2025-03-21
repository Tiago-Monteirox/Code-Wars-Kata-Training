# x = (1, 2, 'a', 'b')
#
#
# def filter_list(l):
#     if type(l) == int:
#         return True
#     else:
#         return False

def filter_list(l):
    new_l = []
    for n in l:
        if type(n) == int:
            new_l.append(n)
    return new_l

# return [x for x in l if type(x) is not str]