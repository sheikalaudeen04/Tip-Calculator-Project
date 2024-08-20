print("Welcome to the tip calculator!")
total_bill=int(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
splitt=int(input("How many people to split the bill?"))
tip_percentage=(total_bill)*(tip/100)
final_bill=total_bill+tip_percentage
each_person_pay=round(final_bill/splitt,2)
print(f"Each person should pay: ${each_person_pay}")
