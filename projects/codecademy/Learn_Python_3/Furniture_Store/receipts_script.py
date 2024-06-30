#Receipts for Lovely Loveseats
#Project overview:
#We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street.
#With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.
#In this project, we will be storing the names and prices of a furniture store’s catalog in variables. 
#You will then process the total price and item list of customers, printing them to the output terminal.
#Program will:
#Help speed up the process of creating receipts for customers.
#Store names and proces of a furniture store's catalog in variables.
#Process the total price and item list of customers, printing them to the output terminal.

#Create Lovely Loveseat description & price variables
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

#Create Stylist Settee description & price variables
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

#Create Luxurious Lamp description & price variables
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

#Set sales tax variable
sales_tax = .088

#Set Customer One total and item list
customer_one_total = 0
customer_one_itemization = ""

#Customer One purchases 1 Lovely Loveseat, add the item to the total and list
customer_one_total += lovely_loveseat_price
customer_one_itemization = lovely_loveseat_description

#Customer One also purchases 1 Luxurious Lamp, add the item to the total and list
customer_one_total += luxurious_lamp_price
customer_one_itemization += " " + luxurious_lamp_description

#Add sales tax to Customer One total
customer_one_tax = customer_one_total * sales_tax

#Add total tax to Customer One total
customer_one_total += customer_one_tax

#Print receipt listing all items and total for Customer One
print("Customer One Items:" + " " + customer_one_itemization)
print("Customer One Total:" + " " + str(customer_one_total))
