#Project overview:
#You work at Len’s Slice, a new pizza joint in the neighborhood.
#You are going to use your knowledge of Python lists to organize some of your sales data.
#
# Your code below:

#Create list of pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#Create list of pizza slice costs
prices = [2, 6, 1, 3, 2, 7, 2]

#Count number of $2 slices in price list
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#Find length of the toppings list
num_pizzas = len(toppings)
print(num_pizzas)

#Print string 'We sell [num_pizzas] different kinds of pizza!'
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#Create 2D list of pizza toppings and prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

#Sort pizza_and_prices in ascending
pizza_and_prices.sort()
print(pizza_and_prices)

#Store first element of pizza_and_prices in a new variable
cheapest_pizza = pizza_and_prices[1]
print(cheapest_pizza)

#Store last element of pizza_and_prices in a new variable
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

#Remove the most expensive/very last topping - 'anchovies'
pizza_and_prices.pop()
print(pizza_and_prices)

#Add new topping to list - 'peppers'
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

#Slice pizza_and_prices list and store 3 lowest cost in new list
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
