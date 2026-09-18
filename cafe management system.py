print(" Cafe Management System ")
menu={'pizza':110,'veg puff':40,'egg puff':50,'burger':80,'Ginger tea':20,'coffee':40,'green tea':50,'lassi':40}
print("Welcome to Sai's Restaurant")
choice=input("choose your choice(beverages/snack items):")
if choice=="beverages":
    print("ITEM : PRICE\n"
      "ginger tea : 20\n"
      " coffee : 40\n"
      "green tea : 50\n"
      "lassi : 40\n")
elif choice=="snack items":
    print("ITEM : PRICE\n"
          "pizza : 120\n"
          "veg puff: 40\n"
          "egg puff : 50\n"
          "burger : 80\n")
else: 
    print("only choose from the menu")

total_amount=0
order_1=input("choose your item to order:").lower()
if order_1 in menu:
    print("your order has been placed")
    total_amount=total_amount+ menu[order_1]
else:
    print("This item is not available.please choose other item from the menu")
while True:
    next_order= input("Do you want to try other food item (yes/no):").lower()
    if next_order=="no":
        break
    elif next_order=="yes":
        order=input("choose your item to order:").lower()
        if order in menu:
            print("your order has been placed")
            total_amount=total_amount+menu[order]
        else:
            print("This item is not available.please choose other item from the menu")
print(f" your Bill to pay:{total_amount}\n Thank you \n visit again")

