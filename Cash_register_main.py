
import Inventory_price
import Cash_register_functions



user_input = input("what items are you purchasing: \n")
price = Cash_register_functions.price_of_item(user_input)

Customer_rev=input("how much do you want to provide? \n")
int_Customer_rev = int(Customer_rev)

if int_Customer_rev > price:
    print(f" your change will be {Cash_register_functions.change(int_Customer_rev,price)}")
else:
    print("Thank you have a great day")
