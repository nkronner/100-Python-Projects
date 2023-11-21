# Project 2 - Tip Calculator

print("Tip Calculator")
total = float(input("What was the total of the bill?\n "))
totalpeople = int(input("How many people to split the bill?\n"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

tip_percentage = tip_percentage / 100

total_per_person = (total + (total * tip_percentage)) / totalpeople

print("Each person should pay: $" + str(round(total_per_person, 2)))

