# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.

item1_name, item1_price, item1_qty = "Coffee", 3.50, 2
item2_name, item2_price, item2_qty = "Muffin", 2.10, 3
item3_name, item3_price, item3_qty = "Water", 1.05, 4

item1_tot = item1_price * item1_qty
item2_tot = item2_price * item2_qty
item3_tot = item3_price * item3_qty

subtotal = item1_tot + item2_tot + item3_tot
tax = subtotal * 0.06
final_total = subtotal + tax

receipt = (
    "========== RECEIPT ==========\n"
    f"Item\tPrice\tQty\tTotal\n"
    f"{item1_name}\t${item1_price:.2f}\t{item1_qty}\t${item1_tot:.2f}\n"
    f"{item2_name}\t${item2_price:.2f}\t{item2_qty}\t${item2_tot:.2f}\n"
    f"{item3_name}\t${item3_price:.2f}\t{item3_qty}\t${item3_tot:.2f}\n"
    "------------------------------\n"
    f"Subtotal\t\t${subtotal:.2f}\n"
    f"Tax (6%)\t\t${tax:.2f}\n"
    f"Total\t\t\t${final_total:.2f}\n"
    "============================"
)

print(receipt)
