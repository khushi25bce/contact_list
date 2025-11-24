import json
import os

DATA_FILE = "contacts.json"


def load_contacts():
    """Load contacts from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_contacts(contacts):
    """Save contacts to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip()

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!\n")


def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n--- Contact List ---")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']} - {c.get('email','')}")
    print()


def search_contact():
    contacts = load_contacts()
    name = input("Enter name to search: ").strip().lower()

    found = [c for c in contacts if name in c["name"].lower()]

    if not found:
        print("No matching contacts.\n")
        return

    print("\n--- Search Results ---")
    for c in found:
        print(f"{c['name']} - {c['phone']} - {c.get('email','')}")
    print()


def delete_contact():
    contacts = load_contacts()
    view_contacts()
    try:
        index = int(input("Enter contact number to delete: "))
        if 1 <= index <= len(contacts):
            deleted = contacts.pop(index - 1)
            save_contacts(contacts)
            print(f"Deleted contact: {deleted['name']}\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    while True:
        print("=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
