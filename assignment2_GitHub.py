"""
01/16/2020
This program  prompts the user for a enter three pieces of information mpg, gas price, and current fuel in tank.
The program prints the calculations how much it costs to travel 100 miles and how many miles the user can drive with the
amount of gas that is currently in her tank.
"""
#My Program
MILES = 100
mpg = int(input ("Enter mpg:"))
price = float(input ("Enter price:"))
current_fuel = float(input ("Enter current tank capacity"))

total_cost = (MILES/mpg) * price
total_miles = (current_fuel * mpg)

print ("mpg = %5d, gas_price = %5.3f, current_fuel= %5d" % (mpg, price, current_fuel))
print ("Based on the fuel in the tank this car can drive %5d miles"% (total_miles))
print ("Based on the current price of fuel it will cost $%5.2f"% (total_cost))

#My Output, this is the actual output generated by the program above.
"""

/Users//PycharmProjects/assignment2/venv/bin/python /Users//PycharmProjects/assignment2/Assignment2.py
Enter mpg:25
Enter price:4.099
Enter current tank capacity5
mpg =    25, gas_price = 4.099, current_fuel=     5
Based on the fuel in the tank this car can drive   125 miles
Based on the current price of fuel it will cost $16.40

Process finished with exit code 0

/Users//PycharmProjects/assignment2/venv/bin/python /Users//PycharmProjects/assignment2/Assignment2.py
Enter mpg:40
Enter price:3.799
Enter current tank capacity10
mpg =    40, gas_price = 3.799, current_fuel=    10
Based on the fuel in the tank this car can drive   400 miles
Based on the current price of fuel it will cost $ 9.50

Process finished with exit code 0

"""