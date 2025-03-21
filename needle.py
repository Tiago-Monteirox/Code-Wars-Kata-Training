def find_needle(haystack):
    position = (haystack.index('needle'))
    return f'found the needle at position {position}'




# def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')

# return 'found the needle at position {}'.format(haystack.index('needle'))




print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))