books = []

# Function to add a new book
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = int(input("Enter the year of publication: "))
    books.append({'title': title, 'author': author, 'year': year})
    print(f"Book '{title}' added successfully.")

# Function to display all books
def display_books():
    if not books:
        print("No books in the library.")
    else:
        for book in books:
            print(f"{book['title']} by {book['author']}, Year: 
{book['year']}")

# Function to search for a book
def search_book():
    title = input("Enter the title of the book to search for: ")
    author = input("Enter the author of the book to search for: ")
    found = False
    for book in books:
        if book['title'].lower() == title.lower() and 
book['author'].lower() == author.lower():
            print("Found book '{book['title']}' by 
{book['author']}.")
            found = True
            break
    if not found:
        print("Book not found.")

# Function to delete a book
def delete_book():
    title = input("Enter the title of the book to delete: ")
    author = input("Enter the author of the book to delete: ")
    for index, book in enumerate(books):
        if book['title'].lower() == title.lower() and 
book['author'].lower() == author.lower():
            del books[index]
            print("Book '{book['title']}' deleted successfully.")
            return
    print("Book not found.")

# Main program loop
while True:
    print("\nLibrary Management System")
    print("1. Add a new book")
    print("2. Display all books")
    print("3. Search for a book")
    print("4. Delete a book")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        delete_book()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
