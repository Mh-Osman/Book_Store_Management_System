from book_data import load_books, save_books

def add_book():
    """
    Registers a new book in the inventory.
    """
    books = load_books()  # Retrieve the existing book collection

    # Gather book details from the user
    title = input("Book Title: ")
    author = input("Author Name: ")
    isbn = input("ISBN Number: ")
    genre = input("Book Genre: ")
    price = float(input("Price: "))
    quantity = int(input("Stock Quantity: "))
    publisher = input("Publisher: ")
    publication_year = input("Publication Year: ")

    # Ensure the book isn't already listed by checking the ISBN
    if any(book['ISBN'] == isbn for book in books):
        print("Error: A book with this ISBN is already in the system.")
        return

    # Construct a dictionary with the book's information
    book_entry = {
        'Title': title,
        'Author': author,
        'ISBN': isbn,
        'Genre': genre,
        'Price': price,
        'Quantity': quantity,
        'Publisher': publisher,
        'Year of Publication': publication_year
    }

    # Add the new book and update the storage
    books.append(book_entry)
    save_books(books)
    print("Book successfully added!")
