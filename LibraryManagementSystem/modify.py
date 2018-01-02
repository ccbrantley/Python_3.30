def modify_author(cursor):
#Necessary Rows  = name_last, name_first, country
#Ordered Unique Rows = author_id(auto), name_last, name_first, country
    current_first = raw_input("Current Author First Name: ")
    current_last = raw_input("Current Author Last Name: ")
    name_first = raw_input("New Author First Name: ")
    name_last = raw_input("New Author Last Name: ")
    country = raw_input("New Country: ")
    cursor.execute("update authors set name_first = %s, name_last = %s, country = %s where name_first = %s and name_last= %s",\
                   (name_first, name_last, country, current_first, current_last))
def modify_user(cursor):
#Necessary Rows = name_first, name_last, phone
#Ordered Unique Rows = UserID(auto), name_first, name_last, phone
    current_phone = raw_input("Current Phone: ")
    name_first = raw_input("New User First Name: ")
    name_last = raw_input("New User Last Name: ")
    phone = raw_input("New Phone: ")
    cursor.execute("update users set name_first = %s, name_last = %s, phone = %s where phone = %s",\
                   (name_first, name_last, phone, current_phone))
    
def modify_book(cursor):
#Necessary Rows = isbn, title, year_pub
#Ordered Unique Rows = isbn, title, author_id, publisher_id, year_pub, description
   current_isbn = raw_input("Current ISBN: ")
   isbn = raw_input("New ISBN: ")
   title = raw_input("New Title: ")
   year_pub = raw_input("New Year Published: ")
   ## set title = %s, set year_pub = %s  , title, year_pub, 
   cursor.execute("update books set isbn = %s, title = %s, year_pub = %s where isbn = %s", (isbn, title, year_pub, current_isbn))
