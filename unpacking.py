'''
Write a Python program to unpack a tuple in several variables.
'''
tpl=(1,2,3,4)
for i in tpl:
    print(i)
tpl=1,2,3
x,y,z=tpl
print(x+y+z)