#1. """Pass or Fail 
score = input("Enter your score: ")
score = int(score)
if score >= 60:
    print("Pass")
else:
    print("Fail")
#2 Even or Odd
number = input("Enter a number: ")
number = int(number)
if number % 2 == 0:
    print("Even")       
else:    print("Odd")    
#3 Temperature Check
temperature = input("Enter the temperature in Celsius: ")
temperature = float(temperature)    
if temperature >= 90:
    print("Hot")
elif temperature >= 60 and temperature < 90:
    print("Mild")
else:    print("Cold")  
#4 Movie Ticket Price
age = input("Enter your age: ")
age = int(age)  
if age < 3:
    print("$0")
elif age >= 3 and age < 12:
    print("$8")
elif age >= 65:
    print("$10")
else:    print("$12")
#5 Absolute Value
number = input("Enter a number: ")
number = float(number)  
if number < 0:
    print(-number)  
else:    print(number)
#6 Login Check
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin" and password == "1234":
    print("Login successful")   
else:    print("Access denied")
#7 Number Compare
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num1 = float(num1)
num2 = float(num2)
if num1 > num2:
    print("The first number is greater.")
elif num2 > num1:
    print("The second number is greater.")
else:
    print("The numbers are equal.") 
#8 Letter Grade
score = input("Enter your score: ")
score = int(score)
if score >= 90:
    print("A")  
elif score >= 80 and score < 90:
    print("B")  
elif score >= 70 and score < 80:
    print("C")  
elif score >= 60 and score < 70:
    print("D")  
else:    print("F")
#9 Shipping Calculator
price = input("Enter the price of the item: ")
price = float(price)    
if price >= 50:
    print("Free shipping!")
else:
    print("Shipping cost: $5")
#10 Triangle Type
side1 = input("Enter the length of the first side: ")
side2 = input("Enter the length of the second side: ")
side3 = input("Enter the length of the third side: ")
side1 = float(side1)
side2 = float(side2)
side3 = float(side3)
if side1 == 0 or side2 == 0 or side3 == 0:
   if side1 <0 or side2 <0 or side3 <0:
    print("Invalid")

elif side1 == side2 and side2 == side3:
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles")
else:
    print("Invalid")   