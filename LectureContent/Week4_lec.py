# activity 1

def even_numbers(list):
    even_number = [num for num in list if num % 2 == 0]
    print(even_numbers)
    return even_numbers

list = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,30,31]
even_numbers(list)

# activity 2
list = [2,3,10,14,20,21,25,13,15]
result = [x**2 for x in list if x**2 > 150]
print(result)

# activity 3
numbers = [0,1,1,2,5,6,8,2,4,6,8]
even_numbers = sorted({num for num in numbers if num % 2 == 0})
print(even_numbers)