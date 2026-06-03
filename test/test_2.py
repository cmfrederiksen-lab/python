# This program calculates the Body Mass Index (BMI) of a user based on their weight and height input.

# Prompt the user to enter their weight in kilograms
weight = float(input("Indtast din vægt i kg: "))

# Prompt the user to enter their height in meters
height = float(input("Indtast din højde i m: "))

# Calculate the BMI using the formula: weight (kg) / (height (m))^2
bmi = weight / (height ** 2)

# Print the calculated BMI rounded to two decimal places
print(f"Dit BMI er: {bmi:.2f}")

