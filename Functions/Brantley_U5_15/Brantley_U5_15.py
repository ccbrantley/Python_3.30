testScores = {'t1': 0, 't2': 0, 't3': 0, 't3': 0, 't4': 0, 't5': 0}
score_add = 0
testAvg = 0

def main():
    test_input()
    calc_avg()
    
def test_input():
    for test in testScores:
        score = int(input('Enter test score ' + ':'))
        testScores[test] = score
        print('A score of ', score,' results in a grade of: ', determine_grade(score))
        
        
def determine_grade(score):
    if (90 <= score <= 100):
        return 'A'
    elif (80 <= score <= 89):
        return 'B'
    elif (70 <= score <= 79):
        return 'C'
    elif (60 <= score <= 69):
        return 'D'
    else:
        return 'F'
def calc_avg():
    score_add = sum(testScores.values())
    testAvg = score_add / 5
    print('The test average is ',format(testAvg, ',.2f'))


main()
