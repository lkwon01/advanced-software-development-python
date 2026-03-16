grade = 85
width = 9
if grade >= 60:
    print("Congratulations! You passed the exam.")  
else:    print("Sorry, you failed the exam. Better luck next time.")   

product = 3
while product <= 50:
    product = product * 3
    print(product)  

star = "*"
for i in range(5):
    print(star * (i + 1)) 

for character in 'Programming':
    if character == 'a':
        break
    print(character, sep=', ')
print (10, 20, 30, sep=' - ') 

star = "*"

total = 0
for number in [2, -3, 0, 17, 9]:
    total += number 
print("The total is:", total)
for counter in range(10):
    #if counter % 2 == 0:
        #print(counter, "is even.")
    #else:
        #print(counter, "is odd.")
    print(counter, end=' ')

total = 0
for number in [1, 2, 3, 4, 5]:
    total += number
print("The total is:", total)

# Christmas Tree
star = "*"
for i in range(4):
    star = '*' * (2 * i + 1)
    print(star.center(width))
print("***".center(width))






