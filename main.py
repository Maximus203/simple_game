import random

while True:
    nombre = random.randint(0, 100)

    n = int(input("Donnez un nombre entre 1 et 100: "))
    while n != nombre:
        if n < nombre:
            n = int(input("C'est plus ! "))
        elif n > nombre:
            n = int(input("C'est moins ! "))
        else:
            continue

    print("Bravo !!!")