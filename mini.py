item_name=[]
prices=[]
quantities=[]
total_cost=0
while True:
    name=input("Enter the name of the Item(q to quite):")
    if name.lower()=="q":
        break
    else:
        price=float(input("Enter the price:"))
        quantity=int(input("Enter The Quantity:"))
        
        item_name.append(name)
        prices.append(price)
        quantities.append(quantity)
print("-----RECEPIT-----")
print(f"{'ITEM':<15}{'PRICE':<10}{'QTY':<6}{'SUBTOTAL':<10}")
for name,price,quantity in zip(item_name,prices,quantities):
    sub_total=price*quantity
    total_cost+=sub_total
    print(f"{name:<15}{price:<10}{quantity:<6}{sub_total:<10}")
print("---------------------------")
print(f"The Total Cost={total_cost}")
