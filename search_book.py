from book_data import load_books

def search_book():
    """
    Find a book using its ISBN and display its details.
    """
    books = load_books()
    isbn_to_find = input("Enter the ISBN of the book you are looking for: ")

    # Look for the book by ISBN
    for book in books:
        if book['ISBN'] == isbn_to_find:
            print("\n📚 Book Details 📚")
            print(f"Title: {book['Title']}")
            print(f"Author: {book['Author']}")
            print(f"ISBN: {book['ISBN']}")
            print(f"Genre: {book['Genre']}")
            print(f"Price: ${book['Price']}")
            print(f"Available Copies: {book['Quantity']}")
            print(f"Publisher: {book['Publisher']}")
            print(f"Published Year: {book['Year of Publication']}")
            return

    print("⚠️ Error: No book found with the provided ISBN.")
