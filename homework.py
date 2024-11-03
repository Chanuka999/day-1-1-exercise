print("welcome to the rollercoster")
height = int(input("what is your height in cm?"))
bil=0
if height >= 120:
   print("You can ride the rollercoster")
   age= int(input("What is your age"))
   if age < 12:
    bil=5
    print("please pay $5.")
   elif age <= 18:
    bil=7
    print("please pay $7.")
   elif age >=45 and age <=55:
     print("every one is going to be ok.Have a free ride on us")
   else:  
    bil=12
    print("please pay $12.")

   wants_photo=  input("do you want to photo taken ?Y or N")
   if wants_photo == "Y":
     bil += 3

     print(f"total bill is {bil}")
else:
  print("Sorry,you have to grow taller before you can ride")
