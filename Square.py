# #Chinasa (Chi-Chi) Iheanacho
# name=input("What is the customer's name?")
# print(name)
# address=input("What is the customer's address?")
# print(address)
# num_strg=input("What is the length of one wall?")
# num=int(num_strg)
# print(num)
# square= num ** 2
# floorcost= square * 2
# installcost= square * 1.5
# total= floorcost+ installcost
#
# print("Estimate for {}:{}." .format(name, address))
# print("Total area of the room is {} square feet.".format(square))
# print("The estimated cost of  flooring is ${}." .format(floorcost))
# print("The estimated cost of the installation is ${}." .format(installcost))
# print("The estimated total for flooring and installation is ${}" .format(total))

side = int(input('What is the side of one room?'))
room = side **2
print("Area of room: {} ft".format(room))
flooring = 2*room
print("Estimated cost of flooring is ${}".format(flooring))
install = 1.5*room
print("EStimated cost of installation is ${}".format(install))
total = flooring+install
print("Total estimates cost of renovation is ${}".format(total))

print('Total estimate is: ${}'.format(total))
