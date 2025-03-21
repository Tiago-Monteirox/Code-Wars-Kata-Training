# def square_digits(num):
#     words = list(str(num))
#     for word in words:
#         resultado = (int(word)**2, end="")
#         return resultado

def square_digits(num):
    num = str(num)
    result = ''
    for i in num:
        result += str(int(i)**2)
    return int(result)

#    return int(''.join(str(int(d)**2) for d in str(num)))
  
    
print(square_digits(120))