print("========== BMI CALCULATOR ==========")
while True:
    try:
        weight = float(input("Enter your weight (kg): "))

        if weight > 0:
            break
        else:
            print("Weight must be greater than 0.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

while True:
    try:
        height = float(input("Enter your height (m): "))

        if height > 0:
            break
        else:
            print("Height must be greater than 0.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

bmi = weight / (height * height)

print("\nYour BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")

elif bmi < 25:
    print("Category: Normal")

elif bmi < 30:
    print("Category: Overweight")

else:
    print("Category: Obese")