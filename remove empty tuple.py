'''
Write a Python program to remove an empty tuple(s) from a list of tuples.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
'''
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
for t in L:
    if t:
        print(t)
#L = [t for t in L if t]
print(L)