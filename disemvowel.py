
# def disemvowel(str2handle):
#     vowel_character = ["a", "A", "e", "E", "o", "O", "i", "I", "u", "U"]
#     str2return = ""
#     i = 0
#     n = len(str2handle)
#     while i < n:
#         if not str2handle[i] in vowel_character:
#             str2return += str2handle[i]
#         i += 1
#     return str2return

def disemvowel(string_):

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for letter in string_:
        if letter in vowels:
            string_ = string_.replace(letter, '')
    return string_
        
# return "".join(c for c in string if c.lower() not in "aeiou")


#    for i in "aeiouAEIOU":
#         s = s.replace(i,'')
#     return s


#    s = ""
#     for c in string:
#         if c.lower() not in "aeiou":
#             s += c
#     return s