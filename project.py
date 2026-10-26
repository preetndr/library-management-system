print("Welcome to the Library Management System")

library = {
    "Python Basics": {"author": "Test", "available": True, "issued_to": ""},
    "Data Science": {"author": "Test1", "available": False, "issued_to": "Rahul"}
}

credentials = {"admin": "admin123", "librarian": "lib123"}

def display_books():
    print("\n--- Library Books ---")
    for title, details in library.items():
        if details["available"] == True:
            status = "Available"
        else:
            status = "Issued"
        print("Title:", title, "| Author:", details["author"], "| Status:", status)
    input("\nPress Enter to continue...")

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    if title in library:
        print("Book already exists in the library.")
    else:
        library[title] = {"author": author, "available": True, "issued_to": ""}
        print("Book added successfully.")
    input("\nPress Enter to continue...")

def issue_book():
    title = input("Enter book title to issue: ").strip()
    if title in library:
        if library[title]["available"] == True:
            name = input("Enter the name of the person issuing the book: ").strip()
            library[title]["available"] = False
            library[title]["issued_to"] = name
            print("Book issued successfully to", name)
        else:
            print("Book is already issued.")
    else:
        print("Book not found in the library.")
    input("\nPress Enter to continue...")

def return_book():
    title = input("Enter book title to return: ").strip()
    if title in library:
        if library[title]["available"] == False:
            library[title]["available"] = True
            library[title]["issued_to"] = ""
            print("Book returned successfully.")
        else:
            print("This book was not issued.")
    else:
        print("Book not found in the library.")
    input("\nPress Enter to continue...")

def view_issued_books():
    print("\n--- Issued Books ---")
    found = False
    for title, details in library.items():
        if details["available"] == False:
            print("Title:", title, "| Issued to:", details["issued_to"])
            found = True
    if found == False:
        print("No books are currently issued.")
    input("\nPress Enter to continue...")

attempts = 0
logged_in = False

while attempts < 3:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if username in credentials and credentials[username] == password:
        print("Login successful!")
        logged_in = True
        break
    else:
        attempts = attempts + 1
        print("Invalid credentials. Attempts left:", 3 - attempts)

if logged_in == False:
    print("Too many failed attempts. Exiting system.")

while logged_in == True:
    print("\n--- Main Menu ---")
    print("1. View Books")
    print("2. Add a Book")
    print("3. Issue a Book")
    print("4. Return a Book")
    print("5. View Issued Books")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        display_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        view_issued_books()
    elif choice == "6":
        print("Exiting Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")