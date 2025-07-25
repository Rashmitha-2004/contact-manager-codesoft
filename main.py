contacts = {}

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Name: ").strip()
    if name in contacts:
        print("This contact already exists.")
        return
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts available.")
        return
    for name, info in contacts.items():
        print(f"{name} - {info['phone']}")

def search_contact():
    print("\n--- Search Contact ---")
    query = input("Enter name or phone to search: ").strip().lower()
    found = False
    for name, info in contacts.items():
        if query in name.lower() or query in info['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return

    print("Leave field empty to keep current value.")
    phone = input(f"New phone (current: {contacts[name]['phone']}): ").strip()
    email = input(f"New email (current: {contacts[name]['email']}): ").strip()
    address = input(f"New address (current: {contacts[name]['address']}): ").strip()

    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address

    print(f"Contact '{name}' updated successfully!")

def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
        if confirm == 'y':
            del contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print("Contact not found.")

def main_menu():
    while True:
        print("\n==== Contact Manager ====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1–6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()
