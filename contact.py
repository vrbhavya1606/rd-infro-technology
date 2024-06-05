class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, query):
        search_results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                search_results.append(contact)
        return search_results

    def update_contact(self, name_or_phone):
        for contact in self.contacts:
            if name_or_phone.lower() == contact.name.lower() or name_or_phone == contact.phone:
                print("Enter updated details:")
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                address = input("Address: ")
                contact.name = name
                contact.phone = phone
                contact.email = email
                contact.address = address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name_or_phone):
        for contact in self.contacts:
            if name_or_phone.lower() == contact.name.lower() or name_or_phone == contact.phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_manager = ContactManager()
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_manager.add_contact(new_contact)

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            search_results = contact_manager.search_contact(query)
            if search_results:
                print("Search Results:")
                for contact in search_results:
                    print(f"Name: {contact.name}, Phone: {contact.phone}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name_or_phone = input("Enter name or phone number of contact to update: ")
            contact_manager.update_contact(name_or_phone)

        elif choice == '5':
            name_or_phone = input("Enter name or phone number of contact to delete: ")
            contact_manager.delete_contact(name_or_phone)

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
 main()
