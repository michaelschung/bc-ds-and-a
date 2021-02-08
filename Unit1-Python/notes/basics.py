# This is a comment

'''
This is a block comment
Anything you type between the opening and closing triple quotation marks
is part of this comment
'''

# Printing things
print('hello')
print(5)

# Declaring a variable
print('===Declaring variables===')
x = 5
y = 7
z = 5

# Mathematical operators
print('===Mathematical operators===')
print(3**2)
print(3 * 5)

# Comparison operators
print('===Comparison operators===')
print(x == y)
print(x > y)
print(x != y)
print(x is z)

lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 3, 4]

print(lst1 == lst2)
print(lst1 is lst2)

# Logical operators
print('===Logical operators===')
print((2 > 3) or (5 < 6))
print((2 > 3) and (5 < 6))

# Built-in functions
print('===Built-in functions===')
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(max(lst))
print(len('hello'))
print(len(lst))
print(type(x))

# Casting
print('===Casting===')
x_str = str(x)
print(x_str)
print(type(x_str))

a = True
a_str = str(a)
print(str(a))

print(a is True)
print(a_str is True)
