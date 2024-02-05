books = ["To kill a Mockingbird", "The Lord of The Rings", "Animal Farm", "The Art of War", "What Men Live By", "Crime and Punishment"]
author = ["Harper Lee", "J.R.R. Tolkien", "George Orwell", "Sun Tzu", "Lev Tolstoy", "Fyodor Dostoyevski"]

def view(books, author):
    print("We have currently", len(books), "books in our library.")
    for i in range(len(books)):
        print(i+1, ". Book: by", author[i], "=", books[i])

def add(books, author):
    author1 = input("Please enter the name of the author: ")
    author.append(author1)
    book1 = input("Please enter the name of the book: ")
    books.append(book1)
    print("Thanks for adding book to our library.")
    print("Book added:", book1, "by", author1)

def searchBook(books, author, query):
    found = False
    for i in range(len(books)):
        if query in books[i] or query in author[i]:
            print("Book: by", author[i], "=", books[i])
            found = True
    if not found:
        print("No matching books or authors found.")

def remove(books, author):
    i = int(input("Please enter the number of the book you want to delete from library's system: "))
    books.pop(i-1)
    author.pop(i-1)

choice2 = ''
while choice2 != 'N' and choice2 != 'n':
    print("Welcome to library X.")
    print("Please choose your operation:")
    print("1. View the books of library.")
    print("2. Add a book to the library.")
    print("3. Remove a book from the library.")
    print("4. Search a book by author or book name from library.")
    choice = int(input())
    if choice == 1:
        view(books, author)
    elif choice == 2:
        add(books, author)
    elif choice == 3:
        remove(books, author)
    elif choice == 4:
        query = input("Enter the book or author name to search: ")
        searchBook(books, author, query)
    choice2 = input("Do you want to do anything else? 'Y'/'N'")



