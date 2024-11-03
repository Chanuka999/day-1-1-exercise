height = float(input("Enter your height in m:"))
weight = float(input("Enter your weight in kg:"))

BMI = round(weight/(height*height))


print(BMI)
if BMI <18.5:
    print(f"Your BMI is {BMI},You are slightly underweight")
elif  BMI <25:
    print(f"Your BMI is {BMI},You are slightly normal weight")
elif BMI < 30:
     print(f"Your BMI is {BMI},You are slightly over weight")
elif  BMI < 35:
     print(f"Your BMI is {BMI},You are slightly obese")    
else:
     print(f"Your BMI is {BMI},You are slightly clinecaly obese")
 
