contacts = []

def add_contact():
    print("Add a New Contact:")
    name = input("Enter Store Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print(f"Contact '{name}' added successfully!\n")

def view_contact_list():
    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    search_term = input("Enter Name or Phone Number to Search: ")
    results = []

    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            results.append(contact)

    if results:
        print("\nSearch Results:")
        for i, result in enumerate(results, start=1):
            print(f"{i}. {result['name']} - {result['phone']}")
        print()
    else:
        print("No matching contacts found.\n")

def update_contact():
    view_contact_list()
    index = int(input("Enter the number of the contact to update: ")) - 1

    if 0 <= index < len(contacts):
        contact = contacts[index]
        print(f"\nUpdating Contact: {contact['name']}")
        contact['phone'] = input("Enter New Phone Number: ")
        contact['email'] = input("Enter New Email: ")
        contact['address'] = input("Enter New Address: ")
        print(f"Contact updated successfully!\n")
    else:
        print("Invalid contact number.\n")

def delete_contact():
    view_contact_list()
    index = int(input("Enter the number of the contact to delete: ")) - 1

    if 0 <= index < len(contacts):
        deleted_contact = contacts.pop(index)
        print(f"\nContact '{deleted_contact['name']}' deleted successfully!\n")
    else:
        print("Invalid contact number.\n")

def main():
    while True:
        print("Contact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()
