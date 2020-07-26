# random dice and OTP generation


import random

#From predefined list
dice_number = ["One","Two","Three","Four","Five","Six"]


# Dice
print(random.choice(dice_number))

# OTP
print(random.randint(1000,9999))

print(random.random())