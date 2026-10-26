# Library Management System (Python Mini Project)

A simple, menu-driven Library Management System built for the command line using basic Python concepts. This project is created without any external libraries, relying purely on Python dictionaries, loops, conditional statements, and functions.

## Features

1. **Login System**: Basic authentication with a maximum of 3 login attempts before the system exits.
2. **View Books**: Displays all books in the library along with their author and current status (`Available` or `Issued`).
3. **Add a Book**: Allows the librarian to add a new book by entering its title and author (checks for duplicates first).
4. **Issue a Book**: Marks an available book as issued and records the name of the person borrowing it.
5. **Return a Book**: Updates the status of an issued book back to available.
6. **View Issued Books**: Lists only the books that are currently borrowed and shows who issued them.

## Default Login Credentials

To access the main menu, use one of the following predefined accounts when prompted:

* **Username:** `admin` | **Password:** `admin123`
* **Username:** `librarian` | **Password:** `lib123`

## Initial Books in the System

* **Python Basics** by Test *(Available)*
* **Data Science** by Test1 *(Issued to Rahul)*

## How to Run the Project

1. Make sure you have Python installed on your computer.
2. Save the code in a file named `project.py`.
3. Open your terminal or command prompt in the folder where `project.py` is saved.
4. Run the following command:
   ```bash
   python project.py
   ```
5. Enter the login credentials and use numbers `1` through `6` to navigate the menu.

## Concepts Used

* **Dictionaries**: Used to store user credentials and nested book details (`author`, `available`, `issued_to`).
* **Functions**: Separate functions created for each menu operation to keep the code organized.
* **While Loops & If-Else Statements**: Used to handle the 3-attempt login check and keep the main menu running until the user chooses to exit.
* **User Input Handling**: Uses `input()` and `.strip()` to take and clean user inputs.