seat={"regular":150,
      "premium":300,
      "vip":500}
ftotal=0
cart=[]
print("-----AVAILABLE SEATS-----")
for key ,value in seat.items():
    print(f"{key:10}:${value:.2f}")
print("--------------------------")
while True:
    ticket=input("Enter The prefered seat(q to quit): ")
    if ticket.lower()=="q":
        break
    
    elif seat.get(ticket) is not None:
        quantity=int(input("Enter the number of seats: "))
        cart.append((ticket,quantity))
    
        
for ticket,quantity in cart:
    price=seat.get(ticket)
    total=price*quantity
    ftotal+=total
    print(f"{ticket}:{quantity}")
print()
print(f"The Total AMOUNT IS:${ftotal:.2f}")
    
        
