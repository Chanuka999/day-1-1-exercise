print("Welcome to the tip Calculater")
bill = float(input("What was the total bii? $"))
percentage = int(input("what persentage tip would you like to give?10,12 or 15?"))
people = int(input("How many people to split the bill?"))


amount = bill * percentage/100
full_amount = bill + amount
final_amount = full_amount/people
full=round(final_amount,2)
print(f"Each person shoud pay: ${full}")
