#Project overview:
#You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. 
#Your job is to go through the lists of data that have been collected in the past couple of weeks.
#You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.
#You have been provided with three lists:
# - hairstyles: the names of the cuts offered at Carly’s Clippers.
# - prices: the price of each hairstyle in the hairstyles list.
# - last_week: the number of purchases for each hairstyle type in the last week.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Create variable to sum up all prices
total_price = 0
#Loop through prices to add each to the total
for price in prices:
  total_price += price
print(total_price)

#Create variable to get average price
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

#Create new price list to discount each by 5
new_prices = [price - 5 for price in prices]
print(new_prices)

#Create variable to get total revenue
total_revenue = 0
#Use for loop to create variable that goes from 0 to len(hairstyles)
for i in range(len(hairstyles)):
  #Add the product of prices[i] & last_week[i] to total_revenue
  total_revenue += (prices[i] * last_week[i])
print("Total Revenue: " + str(total_revenue))

#Find average daily revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

#Create list with cuts that are under 30 - cuts_under_30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]
print(cuts_under_30)
