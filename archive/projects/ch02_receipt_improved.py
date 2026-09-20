# Prints a personalized receipt. Each price is stored once, in a variable.

customer = input("Customer name: ")

notebook_price = 3.50
pens_price = 2.25
stickers_price = 1.75

total = notebook_price + pens_price + stickers_price

print()
print("===== CORNER STORE =====")
print("Customer:", customer)
print()
print("Notebook          ", notebook_price)
print("Pens (pack of 4)  ", pens_price)
print("Stickers          ", stickers_price)
print("------------------------")
print("Total             ", total)
