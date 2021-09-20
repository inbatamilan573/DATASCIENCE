import random
k=random.randint(1, 10)
user =int( input("Guess Number between 1 to 10:"))
if user == k:
    print("\nPlayers Win Computer Lose")
elif user > 10:
    print("\n Out of Range...")
else:
    print("\nPlayer Lose Computer Win")
    print("Random number is: ",k)