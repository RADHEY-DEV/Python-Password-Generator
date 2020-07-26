# conditions are : atleast one uppercase, should have numbers, should have special characters and must be 8 character minimum 

import random


upper_char = ['A','B','C','D','E','F','G']
lower_char = ['a','b','c','d','e']
num = ['1','2','3','4','5']
special_char = ['@', '#', '^','&','!']

passw = random.choice(upper_char) + random.choice(lower_char) + random.choice(num) + random.choice(special_char) + random.choice(upper_char) + random.choice(lower_char) + random.choice(num) + random.choice(special_char)

print(passw)