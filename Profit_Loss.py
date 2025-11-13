cost_price = float(input("Enter the actual price of the item that is being sold : "))
sell_price = float(input("Enter the price of the item that it is being sold at : "))

if sell_price>cost_price:
 profit = sell_price - cost_price
 print("You made ",profit, "money")
else:
 print("You made no profit!")