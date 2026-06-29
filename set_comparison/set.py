raw_input_a = input("Enter your item for group A (comma-seperatd): ")
raw_input_b = input("Enter your item for group B (comma-seperatd): ")
seta = set((item.strip().lower() for item in raw_input_a.split(",")))
setb = set((item.strip().lower() for item in raw_input_b.split(",")))

while True:
    print("\n1.Union 2.Intersection 3. Dif(A-B) 4.Dif(B-A) 5.sym-dif 6.Check 7.Exit")
    choice = input("Choose option: ")
    if choice == "1":
        print(f"Union: {sorted(seta | setb)}")
    elif choice == "2":
        print(f"Intersection is: {sorted(seta & setb)}")
    elif choice == "3":
        print(f"A-B: {sorted(seta - setb)}")
    elif choice == "4":
        print(f"B-A: {sorted(setb - seta)}")
    elif choice == "5":
        print(f"symdif: {sorted(seta ^ setb)}")
    elif choice == "6":
        item = input("Which item you want to check: ").lower().strip()
        print(f"In set A: {item in seta} | In set B: {item in setb}")
    elif choice == "7":
        break

