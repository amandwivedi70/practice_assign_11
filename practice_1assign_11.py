# 1. Write a python script to calculate sum of first N natural numbers
n = int(input('Enter number : '))

sum = 0

while n:
    sum += n
    n -= 1

print('Sum : ', sum)

# 2. Write a python script to calculate sum of squares of first N natural numbers

n = int(input('Enter number : '))
sum_of_square = 0

while n:
    sum_of_square += n**2
    n -= 1

print('Square : ', sum_of_square)

# 3. Write a python script to calculate sum of cubes of first N natural numbers
n = int(input('Enter number : '))
sum_of_cube = 0

while n:
    sum_of_cube += n**3
    n -= 1

print('Cube : ', sum_of_cube)

# 3. Write a python script to calculate sum of cubes of first N natural numbers
n = int(input('Enter number : '))
sum_of_cube = 0

while n:
    sum_of_cube += n**3
    n -= 1

print('Cube : ', sum_of_cube)

# 4. Write a python script to calculate sum of first N odd natural numbers
n = int(input('Enter number : '))
sum_of_n_odd = 0

while n:
    sum_of_n_odd += n*2-1
    n -= 1

print('Sum of first n: ', sum_of_n_odd)

# 5. Write a python script to calculate sum of first N even natural numbers
n = int(input('Enter number : '))
sum_of_n_even = 0

while n:
    sum_of_n_even += n*2
    n -= 1

print('Sum of first n even : ', sum_of_n_even)

# 6. Write a python script to calculate factorial of a given number
n = int(input('Enter number : '))
fact = 1

while n:
    fact *= n
    n -= 1

print('Factorial : ', fact)

# 7. Write a python script to count digits in a given number
num = int(input('Enter number : '))

digits = 0

while num:
    num = num // 10
    digits += 1

print('There are ', digits, ' digits in the given number')

# 8. Write a python script to calculate sum of digits of a given number
num = int(input('Enter number : '))

sum_of_digits = 0

while num:
    sum_of_digits += num % 10
    num //= 10

print('Sum of digits : ', sum_of_digits)

# 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
num = int(input('Enter number : '))
binary = ''

while num:
    binary += str(num % 2)
    num //= 2

i = len(binary)

while i:
    print(binary[i-1], end='')
    i -= 1