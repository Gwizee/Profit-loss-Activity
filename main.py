buying_price = int(input("Enter the buying price of Lemons : "))
selling_price = int(input("Enter the selling pice of lemons : "))

if selling_price > buying_price :
    profit = selling_price - buying_price
    print("Profit :",profit)
else :
    print("No profit!!")