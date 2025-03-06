from add_book import add_book
from view_books import view_books
from delete_book import delete_book
from search_book import search_book

def main_menu():
    """
    Show the main menu and process user selections.
    """
    while True:
        print("\n📚 Welcome to the Bookstore Management System 📚")
        print("1. Add a New Book")
        print("2. View All Books")
        print("3. Find a Book by ISBN")
        print("4. Remove a Book")
        print("5. Exit")

        user_choice = input("Select an option (1-5): ")

        if user_choice == '1':
            add_book()
        elif user_choice == '2':
            view_books()
        elif user_choice == '3':
            search_book()
        elif user_choice == '4':
            delete_book()
        elif user_choice == '5':
            print("Closing the system. Have a great day!")
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()
