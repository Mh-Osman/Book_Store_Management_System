from book_data import load_books

def view_books():
    """
    Display the list of all available books.
    """
    books = load_books()
    
    if not books:
        print("📚 No books available in the system.")
        return

    print("\n📖 Available Books 📖\n")
    for book in books:
        print(f"🔹 Title: {book['Title']}\n"
              f"   Author: {book['Author']}\n"
              f"   ISBN: {book['ISBN']}\n"
              f"   Genre: {book['Genre']}\n"
              f"   Price: ${book['Price']}\n"
              f"   Copies: {book['Quantity']}\n"
              f"   Publisher: {book['Publisher']}\n"
              f"   Year: {book['Year of Publication']}\n")
        print("-" * 50)  # Adds a separator between books

