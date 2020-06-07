'''
Write a Python program to count the elements in a list until an element is a tuple.
'''
l=[1,2,3,4,(1,2)]
c=0
for i in l:
    if isinstance(i,tuple):
        break
    c+=1
print(c)
