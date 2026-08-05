#Library Management System using object-oriented programming principles in Python. 
#This system should manage books and patrons (library users),allowing for basic operations such as adding new books, registering patrons,
# borrowing books, and returning books.
class Library:
    def __init__(self):
        self.books = {}  
        self.patrons = {}  
    def add_book(self, book_id, title, author):    
        if book_id not in self.books:
            self.books[book_id]= {'title': title, 'author': author, 'available': True}
            print(f"Book '{title}' added successfully.")
        else:
            print(f"Book ID {book_id} already exists.")
    def register_patron(self, patron_id, name):
        if patron_id not in self.patrons:
            self.patrons[patron_id] = {'name': name, 'borrowed_books': []}
            print(f"Patron '{name}' registered successfully.")
        else:
            print(f"Patron ID {patron_id} already exists.")
    def borrow_book(self, patron_id, book_id):
        if patron_id in self.patrons and book_id in self.books:
            if self.books[book_id]['available']:
                self.books[book_id]['available'] = False
                self.patrons[patron_id]['borrowed_books'].append(book_id)
                print(f"Patron '{self.patrons[patron_id]['name']}' borrowed book '{self.books[book_id]['title']}'.")
            else:
                print(f"Book '{self.books[book_id]['title']}' is currently not available.")
        else:
            print("Invalid patron ID or book ID.")
    def return_book(self, patron_id, book_id):
        if patron_id in self.patrons and book_id in self.books:
            if book_id in self.patrons[patron_id]['borrowed_books']:
                self.books[book_id]['available'] = True
                self.patrons[patron_id]['borrowed_books'].remove(book_id)
                print(f"Patron '{self.patrons[patron_id]['name']}' returned book '{self.books[book_id]['title']}'.")
            else:
                print(f"Patron '{self.patrons[patron_id]['name']}' did not borrow book '{self.books[book_id]['title']}'.")
        else:
            print("Invalid patron ID or book ID.")
l = Library()

while True:
    choice = input("\n1. Add Book\n2. Register Patron\n3. Borrow Book\n4. Return Book\n5. Exit\n Enter your choice: ")
    if choice == '1':
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        l.add_book(book_id, title, author)
    elif choice == '2':
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")
        l.register_patron(patron_id, name)
    elif choice == '3':
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")
        l.borrow_book(patron_id, book_id)
    elif choice == '4':
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")
        l.return_book(patron_id, book_id)
    elif choice == '5':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")