#Project overview:
#Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers.
#Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.
#Sal’s Shippers has several different options for a customer to ship their package:
# - Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
# - Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
# - Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
#In this project, you’ll build a program that will:
#1. Take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

#Define weight variable & set to any number
weight = 41.5
##Cheapest for 4.8lb = Ground Shipping
##Cheapest for 41.5lb = Ground Shipping Premium

#Ground Shipping:
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

#Print cost of Ground Shipping
print("Cost Ground Shipping:", cost_ground)

#Ground Shipping Premium:
cost_ground_premium = 125.00

#Print cost of Ground Shipping Premium
print("Cost Ground Shipping Premium:", cost_ground_premium)

#Drone Shipping:
if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

#Print cost of Drone Shipping
print("Cost Drone Shipping:", cost_drone)
