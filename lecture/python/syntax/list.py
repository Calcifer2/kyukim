#!python
s = [1, 'four', 9, 16, 25]
print(s)
print(len(s))
#data modify
s[1] = 4
print(s)
#delete element
del s[2]
print(s)
s.insert(0,'kyu')
print(s)