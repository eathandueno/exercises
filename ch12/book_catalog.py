def list_books(book_catalog):
    for title, book in book_catalog.items():
        print(f"Title: {title}, Author: {book['author']}, Pub year: {book['pubyear']}")

def show_book(book_catalog):
    title = input("Enter the title of the book: ")
    book = book_catalog.get(title)
    if book:
        print(f"Title: {title}, Author: {book['author']}, Pub year: {book['pubyear']}")
    else:
        print("Book not found in the catalog.")

def add_edit_book(book_catalog, command):
    title = input("Enter the title of the book: ")
    if command == "edit" and title not in book_catalog:
        print("Book not found in the catalog.")
        return
    author = input("Enter the author of the book: ")
    pubyear = input("Enter the publication year of the book: ")
    book_catalog[title] = {"author": author, "pubyear": pubyear}
    print(f"Book {'added' if command == 'add' else 'updated'} successfully.")

def delete_book(book_catalog):
    title = input("Enter the title of the book to delete: ")
    if title in book_catalog:
        del book_catalog[title]
        print("Book deleted successfully.")
    else:
        print("Book not found in the catalog.")

def main():
    book_catalog = {}  # replace with your actual catalog

    while True:
        command = input("Command: ")
        if command == "list":
            list_books(book_catalog)
        elif command == "show":
            show_book(book_catalog)
        elif command == "add":
            add_edit_book(book_catalog, "add")
        elif command == "edit":
            add_edit_book(book_catalog, "edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()