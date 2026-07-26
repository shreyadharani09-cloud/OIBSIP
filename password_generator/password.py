import random
import string

print("--------------- PASSWORD GENERATOR ---------------")

while True:

    while True:

            length = int(input("Enter password length (8-50): "))

            if 8 <= length <= 50:
                break
            else:
                print("Error: Password length must be between 8 and 50.")

    while True:

        upper = input("Include Uppercase letters? (y/n): ")
        lower = input("Include Lowercase letters? (y/n): ")
        number = input("Include Numbers? (y/n): ")
        symbol = input("Include Symbols? (y/n): ")

        characters = ""
        types = 0

        if upper.lower() == "y":
            characters += string.ascii_uppercase
            types += 1

        if lower.lower() == "y":
            characters += string.ascii_lowercase
            types += 1

        if number.lower() == "y":
            characters += string.digits
            types += 1

        if symbol.lower() == "y":
            characters += string.punctuation
            types += 1

        if types >= 2:
            break
        else:
            print("Error: Please select at least 2 character types.")


    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)


    again = input("\nDo you want to generate another password? (y/n): ")

    if again.lower() != "y":
        print("Thank you for using Password Generator!")
        break