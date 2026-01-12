# TASK: Create a simple library management system
# The system should allow users to:
# ask the user for an option
# 1. search a book
# 2. add a new book
# 3. remove a book
# 4. show all books
# 5. exit
# apply the chosen Operation
# keep running the program until user chooses exit
# prevent duplicate entries

books = ["Python Crash Course", "AI Basics",
          "Harry Potter", "Data Science 101",
          "Avengers Comic"]

print("=" * 50)
print("📚 LIBRARY MANAGEMENT SYSTEM 📚")
print("=" * 50)

while True:
    print("\n" + "-" * 40)
    print("MENU:")
    print("-" * 40)
    print("1. 🔍 Search a book")
    print("2. ➕ Add a new book")
    print("3. ❌ Remove a book")
    print("4. 📖 Show all books")
    print("5. 🚪 Exit")
    print("-" * 40)
    
    choice = input("Enter your choice (1-5): ")
    
    
    if choice == '1':
        s = input("Enter book name to search: ")
        for book in books:
            if book.lower() == s.lower():
                print("Book found:", s)
                break
            else:
                print("Book not found:", s)
    elif choice == '2':
        add = input("Enter book name to add: ")
        if add not in books:
            books.append(add)
            print("Book added:", add)
        else:
            print("Book already exists:", add)
    elif choice == '3':
        rem = input("Enter book name to remove: ")
        if rem in books:
            books.remove(rem)
            print("Book removed:", rem)
        else:
            print("Book not found:")             
    elif choice == '4':
        print("Books in library:")
        for book in books:
            print("-", book)
    elif choice == '5':
        print("Exiting the program.")
        break 