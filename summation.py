def summation(num):
    result = 0
    count = 1

    while count <= num:
        result += count
        count += 1

    return result

# def summation(num):
#     return sum(xrange(num + 1))

# def summation(num):
#     return sum(range(1,num+1))

# def summation(num):
#     return sum(range(num + 1))

    # total = 0
    # for i in range(0, num+1):
    #     total = total + i
    # return total