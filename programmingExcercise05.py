#1. Write a function check_sign(num) that prints whether the number is positive, negative, or zero. 
def check_sign(num):
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")    
check_sign(5)
#2. Write a functin min_of_two(a, b) that returns the smaller of the two numbers using branching. 
def min_of_two(a, b):
    while a>b:
        return b
    else:        
        return a
print(min_of_two(3, 7))
# 3. Write a function sum_n(n) that calculates the sum of numbers from 1 to n using a loop.
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
print(sum_n(5))  # Output: 15
#4 Write a function mutliplication_table(n) that prints the multiplication table of n from 1x n up to 10 x n.
def multiplication_table(n):
    for i in range(1, 11):
        print(i*n)
multiplication_table(5)
#5 Write a function reverse_number(num) that uses a loop to reverse the digits of an interfer. e.g. 1234 -> 4321.
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
print(reverse_number(1234))  # Output: 4321
#6. Write a function count_digits(num) that returns how many digits are in the number using a loop. e.g. 1234 -> 4.
def count_digits(num):
    digits=str(num)
    return len(digits)
print(count_digits(1234789))  
#7. Write a function is_armstrong(num) that checks if a 3-digit number is an Armstrong number. (An Armstrong number is equal to the sum of the cubes of its digits. e.g. 153 = 1^3 + 5^3 + 3^3)
def is_armstrong(num):
    if 100 <= num <= 999:
        digits = str(num)
        armstrong_sum = 0
        for digit in digits:
            armstrong_sum += int(digit) ** 3    
        return armstrong_sum == num
    else:
        raise ValueError("Input must be a 3-digit number.")
print(is_armstrong(153))  # Output: True
print(is_armstrong(123))  # Output: False
#8. Write a function sum_even(n) that calculates the sum of all even numbers from 1 to n. 
def sum_even(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total
print(sum_even(10))  # Output: 30
#9 Write a function print_grid(n) that prints a grid of letter-number paris nested loops. The rows should use the letters A through z. each row should contain numbers 1 through n. Each entry should be in the format <letter><number>.
def print_grid(n):
    for i in range(26):  # Loop through letters A-Z
        letter = chr(65 + i)  # Get the corresponding letter
        for j in range(1, n + 1):  # Loop through numbers 1 to n
            print(f"{letter}{j}", end=' ')
        print()  # New line after each row  
print_grid(7)