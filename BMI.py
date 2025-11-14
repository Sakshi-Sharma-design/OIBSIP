height = float(input("Enter height in inches: "))
weight = float(input("Enter weight in pounds: "))

def BMI(height, weight):
    bmi = (weight / (height ** 2)) * 703
    print("Your BMI is:", bmi)

    
    if bmi < 16:
        print("Severely underweight")
    elif bmi >= 16 and bmi < 18.5:
        print("Underweight")
    elif bmi >= 18.5 and bmi < 25:
        print("Normal weight")
    elif bmi >= 25 and bmi < 30:
        print("Overweight")
    else:
        print("Obese")

BMI(height, weight)

