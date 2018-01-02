def remove_author(cursor):
    #Necessary Rows = name_first, name_last
    #Ordered Unique Rows = author_id(auto), name_last, name_first, country
    print("Remove Author...")
    name_first = raw_input("Author's First name: ")
    name_last = raw_input("Author's Last Name: ")
    cursor.execute("delete from authors where name_first = %s and name_last = %s", (name_first, name_last))

def remove_user(cursor):
    #Necessary input = name_first, phone
    #Ordered Unique Rows = UserID(auto), name_first, name_last, phone
    print("Remove User...")
    name_first = raw_input("User First Name: ")
    phone = raw_input("Phone: ")
    cursor.execute("delete from users where name_first = %s and phone = %s", (name_first, phone))
    
def remove_book(cursor):
    #Necessary input = isbn
    #Ordered Unique Rows = isbn, title, author_id, publisher_id, year_pub, description
    print("Remove Book...")
    isbn = raw_input("ISBN: ")
    cursor.execute("delete from books where isbn = %s", (isbn,))
