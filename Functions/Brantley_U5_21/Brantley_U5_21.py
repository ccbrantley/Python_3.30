import random
def main():
    
    cpu_choice = comp_choice()
    user_choice = input('Type your choice of Rock, Paper, or Scissor: ')
    print('The computer chose ',cpu_choice)
    winner(cpu_choice, user_choice)
    
def comp_choice():
    
    rps = random.randint(1,3)
    if rps == 1:
        return "Rock"
    elif rps == 2:
        return "Paper"
    elif rps == 3:
        return "Scissors"
    
def winner(cpu_choice, user_choice):

    if (cpu_choice == "Rock" and user_choice == 'Scissors') or (cpu_choice == 'Scissors' and user_choice == 'Rock'):
        print('The rock smashes the scissors.')
    elif (cpu_choice == 'Scissors' and user_choice == 'Paper') or (cpu_choice == 'Paper' and user_choice == 'Scissors'):
        print('Scissors cut paper.')
    elif (cpu_choice == 'Paper' and user_choice == 'Rock') or (cpu_choice == 'Rock' and user_choice == 'Paper'):
        print('Paper wraps rock.')
    elif cpu_choice == user_choice:
        print("It's a tie! Play again!")
        main()
    

main()
