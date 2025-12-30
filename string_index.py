a='this is string'
#work with specific character
print(a[0].upper())
#print any character using index
print(a[0])
#last character printing long process
print(a[len(a)-1])
#last character printing short process
print(a[-1])
#Let's check immutability of string

b='Rahim'
b[1]='o'
print(b[1])