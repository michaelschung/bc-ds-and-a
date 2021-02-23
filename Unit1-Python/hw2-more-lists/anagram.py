'''
3) Anagram (anagram.py)
Create two strings. Then, write code that determines whether or not the strings are anagrams of each other. Anagrams are words that contain the same letters, but in different combinations. Print either True or False at the end of your code.
• Examples: 'elbow' and 'below', 'night' and 'thing', 'stressed' and 'desserts', 'listen' and 'silent' are all anagram pairs.
'''

str1 = 'letter'
str2 = 'teller'

result = True

if len(str1) == len(str2):
    for letter in str1:
        if letter in str2:
            str2.remove(letter)
        else:
            result = False
else:
    result = False

print(result)
