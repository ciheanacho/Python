''' In this exercise, we are working with a travel agency to plan the most cost effective trip for your clients.
They have a choice of 4 cities to choose from. Their rates for flight, hotel, and car rental and below.
The objective is to describe to communicate the best choice of travel given their budget and time frame
'''

import math
Venice=[200,20,200,'Venice']
Tokyo = [250,30,120,'Tokyo']
Bali = [370,15,80,'Bali']
Bangkok = [450,10,70,'Bangkok']
Cities = [Venice, Tokyo, Bali, Bangkok]

#To determine the cost of a trip to a particular place:
def trip_cost(flight, hotel, car, num_days = 0):
    return flight + (hotel*num_days) +(car*math.ceil(num_days/7))
#Test function to calculate the cheapest duration of the trip:
def duration(days):
    costs = []
    for city in Cities:
        cost = trip_cost(city[0],city[1],city[2],days)
        costs.append((cost,city[3]))
    min_cost = min(costs)
    return(min_cost)
#Variables to test the previous Test Function:
seven = duration(7)
print(seven)
four = duration(4)
print(four)
ten = duration(10)
print(ten)
fourteen = duration(14)
print(fourteen)
#Print statements to communcicate to the user:
print("The cheapest place to stay for four days is {}. It will cost you ${}". format(four[1], four[0]))
print("The cheapest place to stay for seven days is {}. It will cost you ${}". format(seven[1], seven[0]))
print("The cheapest place to stay for ten days is {}. It will cost you ${}". format(ten[1], ten[0]))
print("The cheapest place to stay for fourteen days is {}. It will cost you ${}". format(fourteen[1], fourteen[0]))
#Test function to return the information to user:
def duration_2(days):
    costs = []
    for city in Cities:
        cost = trip_cost(city[0], city[1], city[2], days)
        costs.append((cost, city[3]))
    min_cost = min(costs)
    return print("The cheapest place to stay for {} days is {}. It will cost you ${}". format(days, min_cost[1], min_cost[0]))
#Implimenting user input:
days = eval(input("How many days do you want to stay?"))
duration_2(days)

def vacation_budget(budget, less_days = False):
    days = 1
    cost = 0
    while cost < budget:
        cost_before = cost
        try:
            costs_before = costs.copy()
        except:
            costs_before = {}
        costs = {}
        for city in Cities:
            cost = trip_cost(city[0], city[1], city[2], days)
            costs[cost] = city[3]
        if less_days:
            cost = max(list(costs.keys()))
            if cost > budget:
                return costs_before[cost_before], days -1
            elif cost == budget:
                return costs_before[cost_before], days
        else:
            cost = min(list(costs.keys()))
            if cost > budget:
                return costs_before[cost_before], days -1
            elif cost == budget:
                return costs_before[cost_before], days
        days += 1

budget = eval(input("How much money would you like to spend in dollars?"))
time = input("Do you want to maximize your stay?")

if time == "yes" or "Yes":
    time = False
elif time == "no" or "No":
    time == True
else:
    print("Please return a valid selection")
vacation_choice = vacation_budget(budget,time)




'''min_city = vacation_budget(1000)
print(min_city)
max_city = vacation_budget(1000, less_days= True)
print(max_city)'''
print("With the budget of {}, you can stay in {} for {} days".format(budget, vacation_choice[0],vacation_choice[1]))












