

# try:
#     a= int(input('Enter Number 1: '))
#     b= int(input('Enter Number 2: '))
#     result=a/b
#     print(result)

# except ZeroDivisionError:
#     print('No no no! No zero is allowed as Number 2!')

# except ValueError:
#     print("Hehe! Number Hoita hoba!!")

# except:
#     print('Ki jani hoisa....')
    
# file=open('test.txt', 'r') 
# data=file.read()
# print(data)
# file.close()
with open("../hello.txt", 'r') as file:
    data=file.read()
    file.close()
    print(data)