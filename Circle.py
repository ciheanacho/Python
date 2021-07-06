#Chinasa (Chi-Chi) Iheanacho

from math import pi
name=input("What is the customer's name?")
print(name)
address=input("What is the customer's address?")
print(address)
num_strg = input("What is the radius of the room?")
num = int(num_strg)
print(num)
area = num**2 * pi
floorcost = area * 2
installcost = area * 1.5
total = floorcost + installcost
# print(area)

print("Estimate for {}:{}" .format(name, address))
print("Total area of the room is {:.1f} square ft." .format(area))
print("The estimated cost of flooring is ${:.0f}.".format(floorcost))
print("The estimated installation cost is ${:.2f}.".format(installcost))
print("The total estimated cost is ${:.2f}." . format(total))