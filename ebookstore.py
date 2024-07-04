import sqlite3

# Create the connection to database
def create_connection():
    conn = sqlite3.connect('ebookstore.db')
    return conn

# Create the book table database
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS book(
                id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)
''')
    conn.commit()

# Populate table with the data given
# Create books variable to store data given
# Use executemany to populate ebookstore.db
def populate_table(conn):
    cursor = conn.cursor()
    books = [
        (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
        (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
    ]
    cursor.executemany('''
                    INSERT OR IGNORE INTO book (id, title, author, qty)
                    VALUES (?,?,?,?)                             
    ''', books)
    conn.commit()

# Add a book to the database
def add_book(conn):
    cursor = conn.cursor()
    id = int(input("\nEnter book id: "))
    title = input("\nEnter book title: ")
    author = input("\nEnter book author: ")
    qty = int(input("\nEnter book quantity: "))
    cursor.execute('''
                INSERT INTO book(id, title, author, qty) VALUES (?,?,?,?)
    ''',(id, title, author, qty))
    conn.commit()
    print("\nBook added successfully!")

# Update book information on the database
def update_book(conn):
    cursor = conn.cursor()
    id = int(input("\nEnter id of the book you want to update: "))
    title = input("\nEnter new title: ")
    author = input("\nEnter new author: ")
    qty = input("\nEnter new quantity: ")
    cursor.execute('''
                UPDATE book SET title = ?, author = ?, qty = ?
                WHERE id = ?
    ''', (title, author, qty, id))
    conn.commit()

# Delete a book from the database
def delete_book(conn):
    cursor = conn.cursor()
    id = int(input("Enter id of the book you want to delete: "))
    cursor.execute('''
                DELETE FROM book WHERE id = ?
    ''', (id,))
    conn.commit()
    print("\nBook has been deleted!")

# Search for a book in the database with wildcard character %
# Learned about this while searching how to do search for data in database
def search_books(conn):
    cursor = conn.cursor()
    search_term = input("Enter the title of the book you want to search for: ")
    cursor.execute ('''
                SELECT * FROM book WHERE title LIKE ?
    ''', ('%' + search_term + '%',))
    rows = cursor.fetchall()
    print("\nSearch Results:\n")
    for row in rows:
        print(row)

# List all books in store
# Use {0}: {1} for .format function
# Use row[1], row[2] to get column 2 and column 3
def list_books(conn):
    cursor = conn.cursor()
    cursor.execute('''
                SELECT * FROM book
    ''')
    rows = cursor.fetchall()
    for row in rows:
        print("{0}: {1}".format(row[1], row[2]))

# Main function of the program
def main():
    conn = create_connection()
    create_table(conn)
    populate_table(conn)

    # Menu section
    while True:
        print("\nMenu:")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("5. List all books")
        print("0. Exit")

        choice = input("Enter your choice: ")

        # Call functions based on user choice
        if choice == '1':
            add_book(conn)
        elif choice == '2':
            update_book(conn)
        elif choice == '3':
            delete_book(conn)
        elif choice == '4':
            search_books(conn)
        elif choice == '5':
            list_books(conn)
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")
    
    conn.close()

if __name__ == "__main__":
    main()