height =input("enter your height in m:")
weight = input("enter your weight in kg:")

new_height = float(height)
new_weight = int(weight)

BMI = new_weight/(new_height*new_height)
round_BMI = round(BMI,2)
print(round_BMI)
