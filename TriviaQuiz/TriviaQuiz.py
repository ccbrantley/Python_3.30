#CBrantley
#CSC249
import Question
import random

def main():
    trivia1 = Question.Question('When referring to a computer monitor, what does the acronym LCD stand for?',\
                        'Liquid Crystal Display ', 'Laser Clear Display ', 'Local Column Decoder ',\
                        'Lattice Code Decoder ')
    trivia2 = Question.Question('When talking about computer memory, what does the acronym ROM stand for?',\
                                'Read-only Memory', 'Read-often Memory', 'Reading-on Memory', 'Read-open Memory')
    trivia3 = Question.Question('In 1975 an engineer created the first electronic camera while working for what company?',\
                                'Kodak', 'Pioneer', 'Fujifilms', 'Panasonic')
    trivia4 = Question.Question('Nintendo is a consumer electronics and video game company founded in what country?',\
                                'Japan', 'China', 'Taiwan', 'Philippines')
    trivia5 = Question.Question('In a photo editing program, what do the letters RGB stand for?',\
                                'Red, Green & Blue', 'Red, Green & Bronze', 'Rad, Green & Blue', 'Rear-ground booth')
    trivia6 = Question.Question('HTML and CSS are computer languages used to create what?',\
                                'Websites', 'Applications', 'DataBases', 'Operating Systems')
    trivia7 = Question.Question('The first person shooter video game Doom was first released in what year?',\
                                '1993', '2003', '1976', '1999')
    trivia8 = Question.Question('In what year was the first Apple computer released?',\
                                '1976', '1974', '1968', '1954')
    trivia9 = Question.Question('In what year did Nintendo release its first game console in North America?',\
                                '1985', '1987', '1991', '1979')
    trivia10 = Question.Question('Steve Jobs, Steve Wozniak, and Ronald Wayne founded what company in 1976?',\
                                 'Apple', 'Windows', 'IBM', 'Lenovo')
    triviaQuestions = [trivia1, trivia2, trivia3, trivia4, trivia5, trivia6, trivia7, trivia8, trivia9, trivia10]
    random.shuffle(triviaQuestions)
    timesRan = 1;
    player1score = 0;
    player2score = 0;
    for value in (triviaQuestions):
        if timesRan < 6:
            print('Player 1\'s Turn\n')
        else:
            print('Player 2\'s Turn')
        print('Player 1\'s Score ', player1score)
        print('Player 2\'s Score ', player2score, '\n')
        print('Question ', timesRan)
        print(value.get_question())
        question_list = value.get_randomOrder()
        print('')
        for  space in range(len(question_list)):
            print('(',chr(65 + space),')', ' ', question_list[space])
        print('')
        answer = input("Answer: ").upper()
        while not(len(answer) == 1 and (68 >= ord(answer) >= 65)):
            print('\nInvalid Input.')
            answer = input("Answer: ").upper()

        isCorrect = value.check_answer(question_list[(ord(answer)-65)])
        timesRan+=1
        if isCorrect == True:
            print('Correct!')
            if timesRan < 6:
                player1score+=1
            else:
                player2score+=1
        else:
            print('...Incorrect...')
            print('"',value.get_question(),'"')
            print('Correct Answer:', value.get_correctAnswer())
        wait = input("\nEnter to continue.\n")
    print('All out of questions...')
    print('Player 1\'s Score: ', player1score)
    print('Player 2\'s Score: ', player2score)
    if player1score > player2score:
        print('Player 1 is the Winner!')
    if player2score > player1score:
        print('Player 2 is the Winner!')
    if player1score == player2score:
        print('The game ended with a tie!')
    print('Program Closing.')                               
main()
