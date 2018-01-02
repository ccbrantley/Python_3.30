import mysql.connector as mariadb
import add
import remove
import modify
def main():
    mariadb_connection = mariadb.connect(user='', password='', database='')
    cursor = mariadb_connection.cursor()
    x = 0;
    # Add, remove, modify,
    # -2 Break Loop, -1 Pause RunTime, 0 Default Menu
    while x != -2:
        if (x == 0):
            print("-----------------------------------------")
            print("|Library Management System|\n|        For Employee Use        |\n|           Version 1.00             |")
            print("-----------------------------------------\n")
            print("1. Add Book       | 2. Add User\n3. Remove Book | 4. Remove User\n5. Modify Book  | 6. Modify User")
            print("7. Add Author    | 8. Modify Author\n9. Remove Author   |  10. Quit")
            x = -1
        x = input("...")
        #Add Book
        if (x == 1):
            add.add_book(cursor)
            mariadb_connection.commit()
        #Add User
        if (x==2):
            add.add_user(cursor)
            mariadb_connection.commit()
        #Remove Book
        if (x == 3):
            remove.remove_book(cursor)
            mariadb_connection.commit()
        #Remove User
        if(x==4):
            remove.remove_user(cursor)
            mariadb_connection.commit()
        #Modify Book
        if(x==5):
            modify.modify_book(cursor)
            mariadb_connection.commit()
        #Modify User
        if(x==6):
            modify.modify_user(cursor)
            mariadb_connection.commit()
        #Add Author
        if (x==7):
            add.add_author(cursor)
            mariadb_connection.commit()
        #Modify Author
        if(x==8):
            modify.modify_author(cursor)
            mariadb_connection.commit()
        #Remove Author
        if (x==9):
            remove.remove_author(cursor)
            mariadb_connection.commit()
        if (x==10):
            x = -2
            
main()
