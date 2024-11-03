print("Welcome to python pizza Delevers")
size = input("What size pizza do you want? S, M, or L")
add_pepporani = input("Do you want pepporani? Y or N")
extra_chese = input("Do you want extra chese")

bill=0

if size== "S":
  bill +=15
elif size == "M":
  bill +=20
else:
  bill +=25

if add_pepporani == "Y":
  if size == "s":
    bill +=2
  else:
    bill +=3

if extra_chese == "Y":
  bill +=1

print(f"your final bill is {bill}")
