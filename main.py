import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon

from ui import Ui_MainWindow
from solver import Resolver


class ExpertSystem(QtWidgets.QMainWindow):
    """ Класс экспертной системы, реализующий интерфейс на основе PyQt"""
    def __init__(self):
        super(ExpertSystem, self).__init__()
        self.currentState = 0
        self.ui = Ui_MainWindow()
        self.solver = Resolver() # Решатель
        self.ui.setupUi(self)
        self.init_UI()


    def init_UI(self):
        """Инициализация UI"""
        _translate = QtCore.QCoreApplication.translate
        self.createButtons(0)
        self.setWindowIcon(QIcon("vegetable.png"))
        self.ui.groupBox.setTitle(_translate("MainWindow", "Выбирете ответ:"))
        self.ui.pushButton_5.setText(_translate("MainWindow", "Сброс"))
        self.ui.pushButton_5.clicked.connect(self.checkReset)
        self.setWindowTitle("ЭС ГеоМонКонсульт")


    def createButton(self, name, value, y):
        """ Создание кнопки ответа """
        pushButton = QtWidgets.QPushButton(self.ui.groupBox)
        pushButton.setGeometry(QtCore.QRect(40, y, 401, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        pushButton.setFont(font)
        pushButton.setStyleSheet("background-color: rgb(255, 194, 8);")
        pushButton.setObjectName(name)
        pushButton.setText(value)
        nextState = self.solver.nextQuestion(self.currenState, value)
        pushButton.clicked.connect(lambda: self.createButtons(nextState, value))
        pushButton.show()


    def createButtons(self, state, answer="К какому типу пользователей вы относитесь?"):
        """ Создание кнопок ответов """
        self.solver.setExplanation(self.currentState, answer)
        if state == 0:
            """ Если состояние начальное - обнуляем элемент объяснений """
            self.solver.explanation = ""
        if self.solver.dictFinish[state] == 1:
            """ Если состояние конечное - вывод результатов """
            self.showResultInfo(state)
            return

        self.currenState = state
        question = self.solver.dictStates[self.currenState]
        dictAnswers = self.solver.dictAnswer[self.currenState]
        _translate = QtCore.QCoreApplication.translate
        self.ui.label.setText(_translate("MainWindow", question.upper()))
        y = -20
        self._removeButtonsChoice()
        for k, v in dictAnswers.items():
            nameBtn = f"{self.currenState}" + f"{v}"
            y += 60
            self.createButton(nameBtn, k, y)


    def _removeButtonsChoice(self):
        """ Удаление кнопок ответов"""
        for button in self.ui.groupBox.findChildren(QtWidgets.QPushButton):
            # удаление кнопок для обновления новых
            button.deleteLater()


    def checkReset(self):
        """ Сбросить состояние вывода """
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Окно предупреждения!")
        dlg.setText("Вы уверены что хотите сбросить состояние работы системы?")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Yes:
            self.createButtons(0)


    def showResultInfo(self, state):
        """ Отображение окна результатов """
        self._removeButtonsChoice()
        result = self.solver.dictStates[state]
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Результаты вывода")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Help)
        dlg.setText(result)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            pass
        elif button == QMessageBox.StandardButton.Help:
            # вывод объяснения
            helpText = self.solver.explanation
            dlg.setWindowTitle("Объяснениия вывода:")
            dlg.setText(helpText)
            button = dlg.exec()

        self.createButtons(0)




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = ExpertSystem()
    application.show()
    sys.exit(app.exec())