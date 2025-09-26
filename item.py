items=['PAO','footlong','coffe']
sum_qty=0
sum_amount=0
for item in items :
    #print(f"Get-->{item}")
    price = float(input(f"Price of {item}:"))
    qty = float(input(f"Quantity of {item}:"))
    amount = price*qty
    print(f"all {item} = {amount:,.2f} baht\n")
    sum_amount=amount+sum_amount
    sum_qty=qty+sum_qty
print(f"sumamount = {sum_amount},.2f baht / sum Quatity = {sum_qty}")
print("Get all")
