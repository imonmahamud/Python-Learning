print("Welcome to Pyhton world 🐍")

#input function

name=input("Enter your name : ")
print('Your name is ', name)

# Taking user input and solve a simple calculation

num1= input('Enter first number : ')
num2= input('Enter Second number : ')

num1=int(num1)
num2=int(num2)

print('Total is : ',num1+num2)

# #string indexing
greeting='Hello World'

print(greeting[3:5])

# Taking two numbers from user and swap them..

num1=int(input('Enter first number : '))
num2=int(input('Enter second number : '))
print('Your Enter Numbers was', num1 , num2)
temp=num1
num1=num2
num2=temp
print('After swap your numbers is ', num1 , num2)