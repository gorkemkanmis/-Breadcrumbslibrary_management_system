class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.books = []
        self.file = open(self.file_name, "a+")
        self.file.seek(0)
        self.books = self.file.readlines()

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        if not lines:
            print("There are no books to display in the list.")
            return
        for line in lines:
            book_info = line.split(',')
            print(f" {book_info[0]}, {book_info[1]}")

    def add_book(self):
        book_title = input("Enter the book title: ")
        book_author = input("Enter the book author: ")
        book_release_year = input("Enter the first release year: ")
        book_pages = input("Enter the number of pages: ")
        book_info = f"{book_title}, {book_author}, {book_release_year}, {book_pages}\n"
        self.books.append(book_info)
        self.file.write(book_info)

        print("Book added successfully.")

    def remove_book(self):
        book_title = input("Enter book title to remove: ")
        with open(self.file_name, 'r+') as file:
            lines = file.readlines()
            updated_lines = []
            for line in lines:
                book_info = line.strip().split(',')
                if book_info[0] != book_title:
                    updated_lines.append(line)
            file.seek(0)
            file.truncate()
            file.writelines(updated_lines)

        if book_title in [book_info[0] for book_info in self.books]:
            self.books = [book_info for book_info in self.books if book_info[0] != book_title]
            self.file.seek(0)
            self.file.truncate()
            for book in self.books:
                self.file.write(book)

            print("Book removed successfully.")
        else:
            print("Book not found.")

lib = Library()


while True:
    print("\n*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")