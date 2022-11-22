from typing import Optional

from data import DATA_STATES, DATA_FINISH, DATA_ANSWERS

class Resolver:
    """ Класс решателя """

    def __init__(self):
        self.explanation = ""
        # База знаний в виде словарей
        self.dictStates = DATA_STATES
        self.dictAnswer = DATA_ANSWERS
        self.dictFinish = DATA_FINISH

    def nextQuestion(self, currentState: int, answer: str) -> Optional[int]:
        """ Следующий вопрос """
        state = self.dictAnswer[currentState][answer]
        return state

    def setExplanation(self, state, answer):
        """ Обновить объяснения """
        self.explanation += f"{self.dictStates[state]}: {answer}\n"






