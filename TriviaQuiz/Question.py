import random
class Question:
    
    def __init__(self, question, correctAnswer, possible1Answer, possible2Answer, possible3Answer):
        self.__question = question
        self.__correctAnswer = correctAnswer
        self.__possible1Answer = possible1Answer
        self.__possible2Answer = possible2Answer
        self.__possible3Answer = possible3Answer

        
    def set_question(self, question):
        self.__question = question
    def set_correctAnswer(self, correctAnswer):
        self.__correctAnswer = correctAnswer
    def set_possible1Answer(self, possible1Answer):
        self.__possible1Answer = possible1Answer
    def set_possible2Answer(self, possible2Answer):
        self.__possible2Answer = possible2Answer
    def set_possible3Answer(self, possible3Answer):
        self.__possible3Answer = possible3Answer

        
    def get_question(self):
        return self.__question
    def get_correctAnswer(self):
        return self.__correctAnswer
    def get_possible1Answer(self):
        return self.__possible1Answer
    def get_possible2Answer(self):
        return self.__possible2Answer
    def get_possible3Answer(self):
        return self.__possible3Answer
    def get_randomOrder(self):
        questions = [self.__correctAnswer, self.__possible1Answer,
                     self.__possible2Answer, self.__possible3Answer]
        random.shuffle(questions)
        return questions[0], questions[1], questions[2], questions[3]

    def check_answer(self, guess):
        if (self.get_correctAnswer() == guess):
            return True
        else:
            return False
    
