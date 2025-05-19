from random import randint

limit = 10000000
sum = 0 
for i in range(limit):
    dice_throw = 6
    while dice_throw == 6:
        dice_throw = randint(1,6)
        sum += dice_throw

expected_value = sum/limit
print(f"The expected value is {expected_value}")