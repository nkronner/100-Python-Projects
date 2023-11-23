# Yas

""" thenumber = input("Enter a number, Any number! ")
secondnumber = input("Enter one more number! Any number! ")
new_number = float(thenumber)
new_secondnumber = float(secondnumber)
numbersdivided = new_number / new_secondnumber
print(f"{new_number} divided by {new_secondnumber} is: {numbersdivided} ")

crazy = str(numbersdivided(len(numbersdivided))) """

# Enhanced code with try and except via GPT4
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Main program starts here
thenumber = get_float_input("Enter a number: ")
secondnumber = get_float_input("Enter one more number: ")

try:
    numbersdivided = thenumber / secondnumber
    print(f"{thenumber} divided by {secondnumber} is: {numbersdivided}")
    crazy = len(str(numbersdivided))
    print(f"The number of characters in {numbersdivided} is: {crazy}")
except ZeroDivisionError:
    print("Cannot divide by zero.")

