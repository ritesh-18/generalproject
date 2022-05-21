import random
repeat = True
while repeat:
    print(random.randint(1, 6))
    another_roll = input("want to roll again? (y/n): ")
    if another_roll.lower()=="y":
        continue
    else:
        break
        
