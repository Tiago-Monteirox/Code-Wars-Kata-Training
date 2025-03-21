def find_average(numbers):
    if numbers == []:
        return 0
    else:
        return sum(numbers) / len(numbers)
        
# return sum(array) / len(array) if array else 0

#  mean=0
#   if len(array)== 0:
#     return mean
#   sum=0
#   for i in array:
#     sum= sum+i
#   mean= sum/(len(array))
#   return mean