# Day 2 project- Restaurant total bill by each people calculator



print("Welcome to the tip calculator.")
bill = float(input("what was the total bill. $"))
tip= int(input("What persentage tip would you like to give?10,12 or 15?"))
people = int(input("how many peoples to split the bill. "))
total_bill = round(bill + bill*12/100,2)
each_person_bill = round(total_bill/people,2)
print(f"Total bill is ${total_bill} and each person should pay ${each_person_bill}")