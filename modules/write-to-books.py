from pprint import pprint
def writeData():
    books_count = int(input("Enter the number of books: "))
    with open("books.txt", "w") as file:
        for i in range(books_count):
            book_name = input("Enter the book name: ")
            book_author = input("Enter the book author: ")
            book_pages = input("Enter the book pages: ")
            file.write(book_name + "\n")
            file.write(book_author + "\n")
            file.write(book_pages + "\n")
    print('Created books.txt')

# writeData()

def changePage():
    book_name = input('Enter book name: ')
    with open('books.txt', 'r') as file:
        books_lines = file.readlines()
        books_lines = [book.strip() for book in books_lines]
    pprint(books_lines)
    if not book_name in books_lines:
        print(f"No book_name found !!!")
        exit()

    pprint(books_lines)
    index_to_change = 0

    for index, line in enumerate(books_lines):
        if book_name == line:
            index_to_change = index + 2

    for index, _ in enumerate(books_lines):
        if index_to_change == index:
            pages = input('insert pages: ' )
            books_lines[index] = pages
    pprint(books_lines)

    with open('books.txt', 'w') as file:
        content = ''.join([f"{book}\n" for book in books_lines])
        file.write(content)

changePage()
