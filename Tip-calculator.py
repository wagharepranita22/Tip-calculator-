print("Welcome to tip calculator  ")
t1_bill=float(input("Please enter your Total bill"))
tip=float(input("What percentage to tip you want to give 10% ,12% and 20% "))
t2_bill=(t1_bill/100)*tip
t3=t1_bill+t2_bill
t4=round(t3)
split=int(input("How many people to split the bill ?"))
t5=t4/split
print("Your final bill : ",t5)