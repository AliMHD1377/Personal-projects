# به نام خدا

class ContactBook:
   
    def __init__(self):
        """
        Initialize contact book object with an empty dictionary.
        """
        self.contacts: dict = {}

    def add_contact(self, name: str, phone: str, email: str, address: str):
        if name not in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print("✅ مخاطب با موفقیت اضافه شد.")
        else:
            print("❌ مخاطبی با این نام قبلاً ثبت شده است.")

    def view_contacts(self):
        """
        نمایش مخاطبین
        """
        if not self.contacts:
            print("\n⚠️  مخاطبی یافت نشد\n")
            return

        print("\n" + "═" * 40)
        print("         📋  لیست مخاطبین")
        print("═" * 40)

        for i, (name, info) in enumerate(self.contacts.items(), start=1):
            print(f"""
    [{i}] 👤  {name}
    ──────────────────────────────────────
        📞  Phone   : {info['phone']}
        📧  Email   : {info['email']}
        🏠  Address : {info['address'] or '—'}
    """)

        print("═" * 40)
        print(f"  Total: {len(self.contacts)} contact(s)")
        print("═" * 40 + "\n")

    def delete_contact(self, name: str):
        if name in self.contacts:
            del self.contacts[name]
            print("🗑️  مخاطب حذف شد.")
        else:
            print("⚠️  مخاطبی با این نام پیدا نشد.")

    def edit_contact(self, name: str, phone: str = None, email: str = None, address: str = None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print("✅ اطلاعات مخاطب با موفقیت به‌روزرسانی شد.")
            return
        print("⚠️  مخاطبی با این نام پیدا نشد.")


def print_menu() -> None:
    menu = """
╔══════════════════════════════════════╗
║      📒  CONTACT BOOK APPLICATION    ║
╠══════════════════════════════════════╣
║   [1]  ➕  Add contact               ║
║   [2]  ✏️  Edit contact              ║
║   [3]  📋  View contacts             ║
║   [4]  🗑️  Delete contact            ║
║   [5]  🚪   Quit                     ║
╚══════════════════════════════════════╝
"""
    print(menu)


if __name__ == "__main__":
    book = ContactBook()

    while True:
        print_menu()
        user_choice = input("\nPlease choose an option: ")

        if user_choice == '1':
            name = input("\nEnter Contact name: ")
            phone = input("Enter Contact phone: ")
            email = input("Enter Contact email: ")
            address = input("Enter Contact address: ")
            book.add_contact(name, phone, email, address)

        elif user_choice == '2':
            name = input("\nEnter name of the contact to edit: ")
            phone = input("Enter new/updated phone number or press Enter to keep unchanged: ")
            email = input("Enter new/updated email or press Enter to keep unchanged: ")
            address = input("Enter new/updated address or press Enter to keep unchanged: ")
            book.edit_contact(name, phone or None, email or None, address or None)

        elif user_choice == '3':
            book.view_contacts()

        elif user_choice == '4':
            name = input("\nEnter name of contact to delete: ")
            book.delete_contact(name)

        elif user_choice == '5':
            print("\nThank You for using Contact Book Application. Goodbye!👋")
            break

        else:
            print("\nInvalid choice! Please try again.❌")
