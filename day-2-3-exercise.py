age =input("What is your current age")
age_remaining = 90-int(age)
days = int(age_remaining)*365
week= int(age_remaining)*52
month = int(age_remaining)*12
print(f"you have {days}days, {week} weeks, {month} months left")
