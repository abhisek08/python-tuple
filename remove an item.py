'''
Write a Python program to remove an item from a tuple.
'''
tpl=(1,2,3,4)
l=list(tpl)
l.remove(3)
tpl=tuple(l)
print(tpl)