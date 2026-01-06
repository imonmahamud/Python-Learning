import functools
# # def breakfast(a):{
# #     print(a),
# #     print('Making Toast'),
# #     print('Applying Butter'),
# #     print('Making Tea')
# # }
    
# # breakfast('10 kg misty')

# #calculate original price with vat...

# # def calculate_price(price):
# #     return price+((price/100)*15)

# # exact_price=calculate_price
# # mbile_price=exact_price(5000)
# # print(mbile_price)


# calculate_price=lambda price: price+((price/100)*15)
# calculate_square=lambda a: a*a 
# print(calculate_square(2))
# addition=lambda a,b: a+b
# print(addition(10,15))
# def store_decorator(func):
#     def wrapper(pet_name):
#         print('Welcome to pet store')
#         func(pet_name)
#         print('Thank you! Bye!')


#     return wrapper



# @store_decorator
# def buy_pet(pet_name):
#     print(f'You bought,{pet_name}')

# buy_pet('Mithu')


# fruits=['Apple','Cherry','Orange']

# it_obj=iter(fruits)

# print(next(it_obj))
# def odd():
#     n=1
#     while n<3:
#         yield n
#         n+=1

# for num in odd():
#     print(num)

# mx=max([1,2,3,4])
# print(f'Max value is {mx}. and {mx}*3={mx*3}')
# multiply_two_number=lambda a,b: a*b
# result=multiply_two_number(2,3)
# print(multiply_two_number(2,3))
# uncountable_number_addition=lambda *args: sum(args)
# result=uncountable_number_addition(1,2,3,4,5,6,7,8,9,10)
# print(result)

# def my_func(**kwargs):
#     print(f'My name is {kwargs['f_name']} {kwargs['l_name']}. I am {kwargs['age']} years old. I got {kwargs['score']} in English. My native town is {kwargs['address']}')

# my_func(f_name='Mahamud Hasan', l_name='Emon', age=29, score=4.25,address='Dhaka')

# students=[('Rahim',79),('Karim',75),('Abul',85)]
# sorted_students=sorted(students, key=lambda x: x[1])
# print(sorted_students)

""" nums=[1,2,3,4,5]
sq_nums=list(map(lambda x : x*x,nums))
print(sq_nums)

even=list(filter(lambda x : x%2== 0,nums))
print(even)

sum=functools.reduce(lambda x,y: x+y,nums)
print(sum) """

n='global'

def outer():
    n='enclosing'
    
    def inner():
        nonlocal n
        n='local'
        print(n)
    
    inner()
    print(n)

outer()
print(n)