#Name: Laura Collins
#V-number:V00763363
#Date: 2026-02-21
#Utility Bill Calculator
#Calculates water usuage and billing amount based on customer code and meter readings. 
#Handles 9-digit meter wraparound and convers thenths-of-a-gallon readings to gallons.
#Applies tiered pricing for residential and commercial customers. 
#Formats the bill amount as $ using f-string with two fractional digits.

def calculate_bill(customer_code, gallons_used):
    if customer_code == 'r':
        base_charge = 5.00
        if gallons_used <= 50:
            bill_amount = base_charge + (0.0003 * gallons_used)
        else:
            bill_amount = base_charge + (0.0003 * 50) + (0.0007 * (gallons_used - 50))
    elif customer_code == 'c':
        base_charge = 100.00
        if gallons_used <= 100:
            bill_amount = base_charge + (0.0005 * gallons_used)
        else:
            bill_amount = base_charge + (0.0005 * 100) + (0.0007 * (gallons_used - 100))
    else:
        raise ValueError("Invalid customer code")
    return bill_amount      
while True:
    customer_code = input("Enter customer code (r for residential, c for commercial, or any other key to quit): ").lower()
    if customer_code not in ['r', 'c']:
        print("Exiting the program.")
        break
    beginning_reading = int(input("Enter beginning meter reading (positive integer): "))
    ending_reading = int(input("Enter ending meter reading (positive integer): "))
    
    if ending_reading < beginning_reading:
        gallons_used = (1000000000 - beginning_reading + ending_reading) / 10
    else:
        gallons_used = (ending_reading - beginning_reading) / 10
    
    bill_amount = calculate_bill(customer_code, gallons_used)
    
    print(f"Customer Code: {customer_code}")
    print(f"Beginning Meter Reading: {beginning_reading}")
    print(f"Ending Meter Reading: {ending_reading}")
    print(f"Gallons Used: {gallons_used:.1f}")
    print(f"Amount Billed: ${bill_amount:.2f}")





