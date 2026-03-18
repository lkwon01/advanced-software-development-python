#21 create two variables, name = your name and age = your age. user print to dispay: My name is _ and I am _ years old.
name = "Laura Collins"
age = 25
print(f"My name is {name} and I am {age} years old.")
#22 Let num = 17 and divisor = 5. compute the remainer using % and print:
num = 17
divisor = 5 
remainder = num % divisor
print(f"{num} devided by {divisor} has remainder {remainder}.")
#23 Create two variables: x = 10 and y = 20. Swap their values using a third variable and print variables before swapping and after swapping. 
x = 10
y = 20  
print(f"Before swapping: x = {x}, y = {y}")
temp = x
x = y       
y = temp
print(f"After swapping: x = {x}, y = {y}")
#24 suppose hours = 40 and rate = 15. calculate the weekley salary (salary = hoours * rate). print the result.
hours = 40
rate = 15       
salary = hours * rate
print(f"Weekly salary is: ${salary}")
#25 Write a python program that asks the user for a score. if the scroe is 60 or higher, print "pass." otherwise, print "fail".
score = int(input("Enter your score: "))
if score >= 60:
    print("pass.")
else:
    print("fail.")
#26 Write a Python program that asks for three side lengths. if any side is 0 or negative -> printn "invalid". if all three sides are equal ->"Equilateral". If exactly two sides are equal -> "Isosceles". Otherwise -> "Scalene".
side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("invalid")
elif side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles")
else:
    print("Scalene")
#27 Wirte a program that prints the numbers from 1 to 10 using a loop. 
for i in range(1, 11):
    print(i)
#28 Write a program that prints all even numbers between 1 and 20 using a for loop. 
for i in range(1, 21):
    if i % 2 == 0:
        print(i) 
#29 print numbers from 20 down to 1 in reverse order using a loop.   
for i in range(20, 0, -1):
    print(i)    
#30 Ask the user for a number n. Use a loop to calculate the sum of numbers from 1 to n. 
n = int(input("Enter a number n: "))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print(f"The sum of numbers from 1 to {n} is: {total_sum}")