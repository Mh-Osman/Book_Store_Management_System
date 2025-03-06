from book_data import load_books, save_books

def delete_book():
    """
    Remove a book from the system using its ISBN.
    """
    books = load_books()
    isbn_to_remove = input("Enter the ISBN of the book you want to remove: ")

    # Locate the book in the records
    for book in books:
        if book['ISBN'] == isbn_to_remove:
            print(f"Removing book: {book['Title']} by {book['Author']} (ISBN: {book['ISBN']})")
            books.remove(book)  # Delete the book from the list
            save_books(books)  # Update the book records
            print("The book has been successfully removed!")
            return

    print("Error: No book found with the given ISBN.")
