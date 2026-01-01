
a={'rahim':12,'karim':14,'fahim': 78, 1:[1,2,3,4,5], 2: {3,4,5}}

# print(type(a))
# for i in a:
#     #print(i)

# print(".......")
# for i in a.values():
#     #print(i)

# print(a.keys(), a.values())

for k,v in a.items():
    print(f'Key Name: {k}, values: {v}')


a=[1,2,3]
b=['Mango','Banana','Apple']

print(dict(zip(a,b)))

#comprehension

nums=list(range(0,11))

result={i: "even" if i%2==0 else "odd" for i in nums}
print(result)