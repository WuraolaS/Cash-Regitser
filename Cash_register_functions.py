import Inventory_price
#When a user inputs a particular inventory, look through the inventory list and print out the price of what was inserted
#be printed out
# item=input("")
# if item == "cake":
#     print (Inventory_price.inventory['cake'])

#Takes the input of the user and prints out the price of the users input


#Retrieves the price of the item
def price_of_item(item_purchased):
    for product in Inventory_price.inventory:
    #if the product equal to cake print out the price
        if product == item_purchased:
    #prints out the value aka the price need to use return instead of print
            return Inventory_price.inventory[product]
        # else:
        #     print("We do not sell that product")

def change(user_cash,item_price):
    user_change = user_cash - price
    return user_change


#If a user purchase multiple items add the price of the item
#1.How do we get multiple items from the user
#Keep asking anymore until users answer is no
#Keep users input into a variable

#call the function with the user input as the parameter
#price_of_item(user_input)

user_input = input("what items are you purchasing: \n")
price = price_of_item(user_input)

Customer_rev=input("how much do you want to provide? \n")
int_Customer_rev = int(Customer_rev)

if int_Customer_rev > price:
    print(f" your change will be {change(int_Customer_rev,price)}")
else:
    print("Thank you have a great day")
