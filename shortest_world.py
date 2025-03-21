def find_short(s):
    lista = s.split()
    lenght = int("inf")
    for world in lista:
        if (len(world) < lenght):
            lenght = len(world)

    return lenght

# return min(len(x) for x in s.split())
# return min(map(len, s.split(' ')))
