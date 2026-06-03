
weight_kg = float(input("Indtast din vægt i kg: "))
height_cm = float(input("Indtast din højde i m: "))

height_m = height_cm / 100

bmi = weight_kg / (height_m ** 2)
print(f"Dit BMI er: {bmi:.2f}")

