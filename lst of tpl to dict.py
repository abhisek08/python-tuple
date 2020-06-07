'''
Write a Python program to convert a list of tuples into a dictionary.
'''
l=[(1,'a'),(2,'b')]
dict={}
for i,j in l:
    dict[j]=i
print(dict)
