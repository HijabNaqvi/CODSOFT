# Contact Book

# Importing re for pattern matching to validate input
import re
class Contact_Book:
    def __init__(self):
        self.contacts = {}

    # add a new contact
    def add_contact(self, name, phone_number, email, address):
        if not self.validate_phone_number(phone_number):
            print("\n Invalid phone number format. Please try again.")
            return
        if not self.validate_email(email):
            print("\n Invalid email format. Please try again.")
            return
        self.contacts[name] = {"Phone Number": phone_number, "Email": email, "Address": address}
        print("Contact added successfully.")

    # validate phone number
    def validate_phone_number(self, phone_number):
        pattern = re.compile(r'^\+?\d{1,3}\d{9,15}$')
        return bool(pattern.match(phone_number))

    # validate email
    def validate_email(self, email):
        pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        return bool(pattern.match(email))

    # view contact list
    def view_contacts(self):
        print("\n--- Contact List ---")
        for name, contact in self.contacts.items():
            print("Name:", name)
            print("Phone Number:", contact["Phone Number"])
            print("Email:", contact["Email"])
            print("Address:", contact["Address"])
            print("--------------------")

    # search a contact
    def search_contact(self, query):
        results = [contact for name, contact in self.contacts.items() if query.lower() in name.lower() or query in contact["Phone Number"]]
        if results:
            print("\n--- Search Results ---")
            for contact in results:
                print("Name:", contact["Name"])
                print("Phone Number:", contact["Phone Number"])
                print("Email:", contact["Email"])
                print("Address:", contact["Address"])
                print("--------------------")
        else:
            print("\n No matching contacts found.")

    # update an existing contact
    def update_contact(self, name, phone_number, email, address):
        if not self.validate_phone_number(phone_number):
            print("\n Invalid phone number format. Please try again.")
            return
        if not self.validate_email(email):
            print("Invalid email format. Please try again.")
            return
        if name in self.contacts:
            self.contacts[name]["Phone Number"] = phone_number
            self.contacts[name]["Email"] = email
            self.contacts[name]["Address"] = address
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    # delete a contact
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def clear_screen(self):
        """Clear the screen."""
        print("\033[H\033[J", end="")

def main():
    contact_book = Contact_Book()

    while True:
        print("\n \t Contact Book Menu ")
        print("\nChoose an operation \n")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\n Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)

        elif choice == "4":
            name = input("Enter name of contact to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_book.update_contact(name, phone_number, email, address)

        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("\n Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

 