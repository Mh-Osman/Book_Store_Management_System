import csv

def load_books():
    """
    Retrieve book records from the 'books.csv' file.
    Returns a list of books, or an empty list if the file is missing.
    """
    try:
        with open('books.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            return list(csv_reader)  # Convert the reader object to a list
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist

def save_books(books):
    """
    Store book details in the 'books.csv' file.
    """
    with open('books.csv', mode='w', newline='') as file:
        headers = ['Title', 'Author', 'ISBN', 'Genre', 'Price', 'Quantity', 'Publisher', 'Year of Publication']
        csv_writer = csv.DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()  # Write column headers
        csv_writer.writerows(books)  # Write the book data
