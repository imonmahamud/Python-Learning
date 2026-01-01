a=['a','b','c',1,'d',2,'e']

for i in a:
    if type(i)== type(3):
        continue
    else:
        print(i)