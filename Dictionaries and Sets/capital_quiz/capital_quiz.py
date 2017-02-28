#Christopher Brantley
#capital quiz
global score_up
global score_down
score_up = 0
score_down = 0
def main():
    read_sort_data()
    display_output()
    
def read_sort_data():
    global state_cap
    state_cap = {}
    line_pair = []
    file = open('state_capital.txt', 'r')
    line = file.readline()
    while line != '':
        line_strip = line.rstrip('\n')
        line_pair = line_strip.split('|')
        state = line_pair[0]
        capital = line_pair[1]
        state_cap[state] = capital
        line = file.readline()

    
def quiz():
    quiz = state_cap.popitem()
    state = quiz[0]
    capital = quiz[1]
    return state, capital
    
def display_output():
    global score_up
    global score_down

    guess = False
    state, capital = quiz()
    while guess == False:
        user_guess = input('Enter the capital for: {} '.format(state))
        if user_guess == capital:
           score_up += 1
           print('You answered correctly.')
           guess = True
        else:
            score_down += 1
            print('You answered incorrectly.')
    print('Total Correct: ', score_up, '\nTotal Incorrect: ', score_down, sep ='')
    display_output()
    
        
        

    
    
    

main()
