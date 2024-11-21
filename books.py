import json # library for using json format
import os   # library to read and write to file results 
import uuid # library to generate random ID

class Book:
    def __init__(self, id, title, author, year, status):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

class BookManager:
    def __init__(self, filename):
        self.filename = filename
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.books = [ Book(book['id'], book['title'], book['author'], book['year'], book['status']) for book in data]
        else:
            self.books = []

    def save_books(self):
        data = [{'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year, 'status': book.status} for book in self.books]
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def add_book(self):
        id = str(uuid.uuid4())
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter book year: ")
        status = "Avaliable"

        self.books.append(Book(id, title, author, year, status))
        self.save_books()
        print(f"Book '{title}' added successfully! ID: {id}")

    def delete_book(self):
        id = input("Enter Book ID to delete: ")

        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                self.save_books()
                print(f"Book '{id}' deleted successfully!")
                return

        print(f"Book '{id}' not found.")

    def view_books(self):
        print("\nList of Books:")
        for book in self.books:
            print(f"ID: {book.id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Year: {book.year}")
            print(f"Status: {book.status}\n")

    def search_book(self):
        query = input("Enter search query: ")
        results = [book for book in self.books if query.lower() in (book.title + book.author + book.year).lower()]

        if results:
            print("\nSearch Results:")
            for book in results:
                print(f"ID: {book.id}")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Year: {book.year}")
                print(f"Status: {book.status}\n")
        else:
            print("No results found.")

    def change_status(self):
        id = input("Enter book ID to update status: ")
        status = input("Enter new status: ")

        for book in self.books:
            if book.id == id:
                book.status = status
                self.save_books()
                print(f"Book '{id}' status updated to '{status}'!")
                return

        print(f"Book '{id}' not found.")

def main():
    filename = "books.json"
    manager = BookManager(filename)
    
    os.system('clear')

    while True:
        print("\nOptions:")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. View Books")
        print("4. Search Books")
        print("5. Change Book Status")
        print("6. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_book()
        elif choice == "2":
            manager.delete_book()
        elif choice == "3":
            manager.view_books()
        elif choice == "4":
            manager.search_book()
        elif choice == "5":
            manager.change_status()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
