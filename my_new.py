import random

secret_number = random.randint(1,100)

print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)
while True:
    user_number=int(input("Enter number to guess magician's number : "))
    if user_number != secret_number:
        print("Ha ha! You're stuck in my loop!")
        user_number = int(input("Enter number to guess magician's number : "))
else:

    print("you got it")




