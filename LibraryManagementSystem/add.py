def add_author(cursor):
    print("Add Author...")
    #Necessary input = name_last, name_first
    #Ordered Unique Rows = author_id(auto), name_last, name_first, country
    name_first = raw_input("Author First Name: ")
    name_last = raw_input("Author Last Name: ")
    cursor.execute("insert into authors(name_last, name_first) values (%s, %s)", (name_last, name_first))  
    
def add_user(cursor):
    #Necessary input = name_first, name_last, phone
    #Ordered Unique Rows = UserID(auto), name_first, name_last, phone
    name_first = raw_input("User First Name: ")
    name_last = raw_input("User Last Name: ")
    phone = raw_input("User Phone: ")
    cursor.execute("insert into users(name_first, name_last, phone) values (%s, %s, %s)", (name_first, name_last, phone))
    
def add_book(cursor):
    print("Add Book...")
    #Necessary input = isbn, title, year_published
    #Ordered Unique Rows = isbn, title, author_id, publisher_id, year_pub, description
    name_first = raw_input("Author First Name: ")
    
    name_last = raw_input("Author Last Name: " )
    author_id = cursor.execute("select author_id from authors where name_first  = %s and name_last = %s", (name_first, name_last))
    for value in cursor:
        author_id = str(int(value[0]))
        print(author_id)
    isbn = raw_input("ISBN: ")
    title = raw_input("Title: ")
    year_pub =  raw_input("Year Published: ")
    cursor.execute("insert into books(isbn, title, author_id, year_pub) values (%s, %s, %s, %s)", (isbn, title, author_id, year_pub))
