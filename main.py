# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @coderagam001 / @codewithagam
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

# Print a Welcome message
print("Welcome To Python Tip Calculator!")

# Get the inputs from the user
bill = float(input("What was the total bill? "))
tip = int(input("How much tip should be given? 10, 12, or 15? "))
people = int(input("Number of people to split the bill? "))

# Calculate the bill with the tip and bill per person
bill_with_tip = (tip / 100 * bill + bill)
bill_per_person = (bill_with_tip / people)

# Round off the amount to 2 digits and print the vaule
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: {final_amount}")