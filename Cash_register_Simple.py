
import Inventory_price

#A cash register allows the user to type in the product and it returns the prices
#In this exercise I'll be importing the inventory module
#example it's most simpliest form
# slice_of_cake = 2.50
# cookie = 3.00
# print(slice_of_cake + cookie)

#test to see how I'll call the function
#print(Inventory_price.inventory['cake'])

#When a user inputs a particular inventory, the price of the inventory should
#be printed out
# item=input("")
# if item == "cake":
#     print (Inventory_price.inventory['cake'])
#
# #When a user gets multiple item, add the price of both items
# item=input("")
# item1=input("")
# Total=Inventory_price.inventory['cake']+(Inventory_price.inventory['coffee'])
# print(Total)
# if item == "cake" and item1=="coffee":
#     print(Total)
#
# #If the money that the user gave is higher than the total subtract the total fr
# #the amount gave
# customer_cash=input("?")
# some=float(customer_cash)
# if some > Total:
#     print (float(customer_cash - Total))

#Adding inventory

#Inventory_price.inventory.update({"cookie":1.00})
item = input("")
price =input("")
Inventory_price.inventory[item] = int(price)
print(Inventory_price.inventory)
