import random


def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 'snake':
        if you == 'water':
            return False
        elif you == 'gun':
            return True
    elif comp == 'Water':
        if you == 'gun':
            return False
        elif you == 'snake':
            return True
    elif comp == 'gun':
        if you == 'snake':
            return False
        elif you == 'Snake':
            return True


print("Computer's Turn: Snake, Water (or) Gun: ")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'snake'
elif randNo == 2:
    comp = 'water'
else:
    comp = 'gun'

you = input("Enter snake, water (or) gun: ")
a = gamewin(comp, you)

print(f"Computer Took {comp}")
print(f"You Took {you}")

if a == None:
    print("Tie!!!")
elif a:
    print("You Won!!!")
else:
    print("You Lost!!!")
