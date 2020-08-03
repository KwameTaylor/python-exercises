#Excerise 1
day_of_week = input('Enter the day of the week: ')
if day_of_week == 'Monday':
    print('The day of the week is Monday.')
else:
    print('The day of the week is not Monday.')

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']
day_of_week = input('Enter the day of the week: ')
if day_of_week in weekday:
    print('That day of the week is a weekday.')
elif day_of_week in weekend:
    print('The day of the week is a weekend.')

num_hours = 33.00
hourly_rate = 12.50
next_weeks_pay = num_hours * hourly_rate
if num_hours > 40:
    num_hours += (num_hours - 40) * 1.5
    weekly_pay = num_hours * hourly_rate
    print(weekly_pay)
else:
    weekly_pay = num_hours * hourly_rate
    print(weekly_pay)

#Exercise 2
#part a
i = 5
while i <= 15:
    print(i)
    i += 1

i = 0
while i <= 100:
    print(i)
    i += 2

i = 100
while i >= -10:
    print(i)
    i -= 5

i = 2
while i < 1000000:
    print(i)
    i = i * i

i = 100
while i >= 5:
    print(i)
    i -= 5

#part b
num = int(input('Enter a whole number: '))
for n in range (1, 11):
    print(str(num) + ' x ' + str(n) + ' = ' + str(num * n))

for n in range(1, 10):
    print(n * str(n))

#part c
num = 0
if (isdigit(num)) and (num >= 1 or num <= 50):
    print('Number to skip is: ' + num)
    break
else num = input('Enter an odd number between 1 and 50: ')
    continue
for n in range(1, 51):
    if n % 2 == 0:
        continue
    else
        n == num:
        print('Yikes! Skipping number: ' + num)
        continue
    print('Here is an odd number: {}'.format(n))
# Note to self: Have questions on this problem.

#trying part c again
num = input('Enter an odd number between 1 and 50: ')
if (num.isdigit()) and (int(num) >= 1 or int(num) <= 50):
    if int(num) % 2 == 0:
    break
    elif int(num) % 2 != 0:
        print('Number to skip is: ' + num)
else:
    num = input('Enter an odd number between 1 and 50: ')
for n in range(1, 51):
    if n == int(num):
        print('Yikes! Skipping number: ' + num)
        continue
    if n % 2 != 0:
        print('Here is an odd number: {}'.format(n))

#part d
pos_num = int(input('Enter a positive number: '))
while pos_num < 0 or not isdigit(pos_num):
    pos_num = int(input('Enter a positive number: '))
for n in range (0, pos_num + 1):
    print(n)
    n += 1

#part e
pos_num = int(input('Enter a positive integer: '))
while pos_num < 0 or not isdigit(pos_num):
    pos_num = int(input('Enter a positive integer: '))
for n in range (1, pos_num + 1):
    print(pos_num - n)
    n += 1

#Exercise 3
for fizzbuzz in range(100):  
    if fizzbuzz % 15 == 0:  
        print("FizzBuzz")                                          
        continue
    elif fizzbuzz % 3 == 0:      
        print("Fizz")                                          
        continue
    elif fizzbuzz % 5 == 0:          
        print("Buzz")                                      
        continue
    print(fizzbuzz)

#Excercise 4
#Ask in class how to do this one. Not sure how to make the table, maybe with just all strings?

running = True
while running:
    num = int(input("What number would you like to go up to?: "))
    print()
    for x in range(1, num + 1):
        print(x, x ** 2, x ** 3)

    question = input("Would you like to do another table? Yes or No?: ")
    if question == 'No':
        break
    else:
        continue