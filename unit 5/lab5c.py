import random

while True:

    print("\n----- DICE SIMULATOR -----")
    print("1. Roll Dice")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        dice = random.randint(1, 6)

        print("\nRolling the dice...")
        print("Dice Result:", dice)

    elif choice == 2:

        print("Exiting Dice Simulator...")
        break

    else:
        print("Invalid choice!")