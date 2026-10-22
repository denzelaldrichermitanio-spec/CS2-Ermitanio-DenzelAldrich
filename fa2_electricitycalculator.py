# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ")
if name == "":
    print("This field is required. Please enter a name.")
    while name == "":
        name = input("Enter customer name: ")
        if name == "":
            print("This field is required. Please enter a name.")
        
previous = float(input("Enter previous meter reading: "))\

if previous < 0:
    print("The previous meter reading must be at least 0.")
    while previous < 0:
        previous = float(input("Enter previous meter reading: "))
        if previous < 0:
            print("The previous meter reading must be at least 0.")

current = float(input("Enter current meter reading: "))
if current < previous:
    print("The current meter reading must at least be the value of the prvious reading.")
    while current < previous:
        current = float(input("Enter current meter reading: "))
        if current < previous:
            print("The current meter reading must at least be the value of the prvious reading.")

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))
