def gas_split():
    gas_bill = float(input("Enter gas bill: "))
    price_gallon = float(input("Price per gallon: "))
    people =  float(input("How many were on the trip: "))
    personal = float(input("Number of gallons you used personally: "))
    trip = float(input("How many gallons used on trip: "))

    gallons_bought = gas_bill / price_gallon
    others_bill = (trip * price_gallon) / people
    my_bill = others_bill + (personal * price_gallon)
    return my_bill, others_bill, gallons_bought

my_bill, others_bill, gallons_bought = gas_split()
print(f"We bought a total of {gallons_bought:.2f} gallons. My bill is ${my_bill:.2f}. You guys owe me ${others_bill:.2f}.")