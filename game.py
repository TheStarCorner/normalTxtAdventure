# Note Maybe Add more later


def main():
    print ("Welcome to The Game!")
    part1()


def part1():
    entered_name = input("Enter your name: ")
    print(f"Your name is {entered_name}")
    print()
    print("Eggs - 1, Cereal - 2")
    firstChoice = input("It is time for breakfast. What will you eat? (TYPE IN EITHER 1 FOR EGGS OR 2 FOR CEREAL):")
    if firstChoice == "1":
        print("You really must like eggs!")
    elif firstChoice == "2":
        print(f"Let's hope you have milk, {entered_name}")

    print("That's it for now!")


if __name__ == "__main__":
    main()