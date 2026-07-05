inventory = [
(101, "Notebook", 2.50, 20),
(102, "Pen Set", 4.99, 3),
(103, "USB Cable", 8.00, 12),
(104, "Mouse Pad", 6.50, 2),
(105, "Stapler", 9.99, 15),
]

while True:
    print("\n1.View Inventory 2.Search 3.Low Stock 4.Value 5.Restock 6.Exit")
    print()
    choice = input("What you want to check: ")

    if choice == "1":
        print(f"\n{'ID':>5} {'Name':<20} ${'Price':>8} {'Qty':>5}")
        print("-"*50)
        for p in inventory:
            print(f"{p[0]:>5} {p[1]:>20} ${p[2]:>8} {p[3]:>5}")
    
    elif choice == "2":
        product_name = input("Search name :").lower()
        found = [p for p in inventory if product_name in p[1].lower()]
        if found:
            for p in found:
                print(f"{p[0]} | {p[1]} | ${p[2]:.2f} | Qty:{p[3]}")
                if p[3] < 5:
                        print(f"{p[1]} has low stock")
                else:
                        print(f"{p[1]} well stock.")
        else:
            print(f"{product_name} was not found.")

    elif choice =="3":
        low = [p for p in inventory if p[3]<5]
        if low:
            for p in low:
                print(f" {p[1]}: only {p[3]} left")
        else:
            print("All item well stocked.")

    elif choice == "4":
        total = sum(p[2] * p[3] for p in inventory)
        print(f"Total Inventory value: ${total:.2f}")
    
    elif choice == "5":
        try:
            pid = int(input("Enter product id to restock: "))
            qty = int(input("How many to add: "))

            for i,p in enumerate(inventory):
                if p[0] == pid:
                    inventory[i] = (p[0], p[1], p[2], p[3]+qty)
                    print(f"Updated! {p[1]} is now restocked and now {p[3]+qty} in stock.")
                    break
                else:
                    print("Product id not found.")
        except ValueError:
            print("Please enter a valid numbers.")

    elif choice == "6":
        break
    
    else:
        print("Invalid Option!")
    
    again = input("Back to the option? y/n: ")
    again = again.strip().lower()

    if again == "n":
        print("To check the inventory again run py Shop_inventory.py")
        break
