'''
Write a Python program to reverse a tuple.
'''
tpl=1,2,3
l=list(tpl)
l.reverse()
tpl=tuple(l)
print(tpl)