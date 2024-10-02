height=float(input("enter your height:"))
weight=float(input("enter your weight:"))
bmi =weight/height**2
if bmi<18.2:
    print(f"your BMI is {bmi} your are underweight")
elif bmi<25:
    print(f"your BMI is {bmi}  and your are a normal weight")
elif bmi<30:
    print(f"your BMI is {bmi} and your overweight")
elif bmi<35:
    print(f"your BMI is {bmi} and your obese")
else:
    print(f"your BMI is {bmi} and your clinically obese")
