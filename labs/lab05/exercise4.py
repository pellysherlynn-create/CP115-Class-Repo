item_name = input("ITEM_NAME:")
price = input("PRICE:")
quantity = 3
tax_rate = 6/100
price = float(price)

subtotal = price * quantity
tax_amount = subtotal * tax_rate
total_amount = subtotal + tax_amount

print(f"SUBTOTAL: {subtotal}")
print(f"TAX_AMOUNT: {tax_amount}")
print(f"TOTAL_AMOUNT: {total_amount}")