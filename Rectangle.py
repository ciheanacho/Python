#Chinasa (Chi-Chi) Iheanacho
name=input("What is the customer's name?")
print(name)
address=input("What is the customer's address?")
print(address)
length_strg=input("What is the length of the room (in feet)?")
length=int(length_strg)
print(length)
width_strg=input("What is the width of the room (in feet)?")
width=int(width_strg)
print(width)

area = length* width
print(area)

floorcost = area *2
installcost= area *1.5
total = floorcost+installcost

print("Estimate for {}:{}" .format(name, address))
print("Total area of the room is {} square feet" .format(area))
print("The estimated cost of flooring is ${}." .format(floorcost))
print("The estimated installation cost is ${}." .format(installcost))
print("The estimated total cost is ${}." .format(total) )