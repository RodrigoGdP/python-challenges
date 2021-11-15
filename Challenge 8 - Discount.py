def calcdis(price, discount):
     disc = price * (discount/100)
     total = price - disc
     return total

price = int(input("\n\nEnter the price.\n\n"))
discount = int(input("\n\nEnter the discount percentage.\n\n"))
print(f"\nTotal: {price} - {discount}% = {calcdis(price, discount)}")