def to_jaden_case(string):
    string = string.split()
    new_l = []
    for s in string:
        new_l.append(s[:1].upper() + s[1:])
    return " ".join(new_l)

print(to_jaden_case("eu sou um homem"))