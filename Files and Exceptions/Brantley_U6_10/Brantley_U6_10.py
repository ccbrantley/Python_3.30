#Golf Scores
def main():
    print('Springfork Amateur Golf Club')
    menu_user_input = int(input('Enter 1 to append data:  \nEnter 2 to view data:\n'))
    while menu_user_input == 1:
        append_data()
        main()
    while menu_user_input == 2:
        view_data()
        main()
        
def append_data():
    again = 'y'
    while again == 'y':
        golf_file = open('golf.txt', 'a')
        player_name = str(input("Enter Player's Name: "))
        golf_file.write(player_name + '\n')
        golf_score = input("Enter {}'s golf score:".format(player_name))
        golf_file.write(golf_score + '\n')
        again = str(input('y to continue n to exit'))
    golf_file.close()
    
def view_data():
    golf_file = open('golf.txt', 'r')
    line = golf_file.readline()
    while line != '':
        print('Player: ', line, sep='')
        line = golf_file.readline()
        print('Score: ', line, sep='')
        line = golf_file.readline()
        
main()
