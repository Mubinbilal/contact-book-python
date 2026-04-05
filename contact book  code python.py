import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)

    print("✅ Contact added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    print("\n📒 Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")

# Search contact
def search_contact():
    keyword = input("Enter name to search: ").lower()
    contacts = load_contacts()

    found = False
    for contact in contacts:
        if keyword in contact["name"].lower():
            print(f"Found: {contact['name']} | {contact['phone']} | {contact['email']}")
            found = True

    if not found:
        print("❌ Contact not found.")

# Delete contact
def delete_contact():
    contacts = load_contacts()
    view_contacts()

    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            save_contacts(contacts)
            print(f"🗑️ Deleted: {removed['name']}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    while True:
        print("\n====== CONTACT BOOK ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()