contact_list = []

def find_contact(name):
    for contact_name in contact_list:
        if contact_name["name"].lower() == name.lower():
            return contact_name
    else:
        return None

def valid_phone(phone):
    return phone.isdigit() and len(phone) == 11

def valid_email(email):
    return "@" in email and "." in email

while True:
    print("\n1. Add contact 2.View all contacts 3.Search 4.Delete 5.Update phone/email 6.Exit")
    print()
    choice = input("Select option: ")

    if choice == "1":
        name = input("Contact name: ")
        if find_contact(name):
            print("Contact already exist.")
        else:
            phone = input("Phone (11 digits): ")
            if not valid_phone(phone):
                print('Invalid phone.')
            else:
                email = input("Input email: ")
                if not valid_email(email):
                    print('Invalid email.')
                else:
                    contact_list.append({"name": name, "phone": phone, "email": email})
                    print(f"{name} added to the contact.")
    elif choice == "2":
        print(f"\nContacts ({len(contact_list)} total): ")
        for contact in contact_list:
            print(f" {contact['name']: <10}: {contact['phone']: <10}, {contact['email']: <10}")

    elif choice == "3":
        cont = find_contact(input("Search: "))
        if cont:
            print(cont)
        else:
            print("Not found.")
    
    elif choice == "4":
        cont = find_contact(input("Delete: "))
        if cont:
            contact_list.remove(cont)
            print(f"{cont} deleted.")
        else:
            print(f"{cont} not found to delete.")

    elif choice == "5":
        cont = find_contact(input("Name to update: "))
        if not cont:
            print("Not found.")
        else:
            cont_up = input("Update (name/email/phone): ").lower()
            if cont_up == "phone":
                valid = input("New phone number: ")
                if valid_phone(valid):
                    cont["phone"] = valid
                else:
                    print("Invalid.")
            elif cont_up == "name":
                new_name = input("Enter new name: ").strip()
                if find_contact(new_name):
                    print("Alread Exist.")
                else:
                    cont["name"] = new_name
                    print(f"Name updated to {new_name}")
            elif cont_up == "email":
                valid = input("New email: ")
                if valid_email(valid):
                    cont["email"] = valid
                else:
                    print("Invalid.")
    elif choice == "6":
        break

    else:
        again = input("Back to the contact book? Y/N: ")
        again = again.strip().lower()

        if again == "n":
                break