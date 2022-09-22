# imports
import sys
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QGridLayout,
    QPushButton
)


ERROR = 'Error'


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setFixedSize(500, 500)
        self.general_layout = QVBoxLayout()

        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)

        self._create_display()
        self._create_buttons()

    def _create_display(self):
        """ Calculator display. """
        self.display = QLineEdit()
        self.display.setFixedHeight(150)
        self.display.setAlignment(Qt.AlignLeft)
        self.display.setReadOnly(True)
        self.display.setFont(QFont('Arial', 32))

        self.general_layout.addWidget(self.display)

    def _create_buttons(self):
        self.buttons = {}
        buttons_layout = QGridLayout()

        buttons = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            'C': (0, 4),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '(': (1, 4),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            ')': (2, 4),
            '0': (3, 0),
            '00': (3, 1),
            '.': (3, 2),
            '+': (3, 3),
            '=': (3, 5),
        }

        for button_text, position in buttons.items():

            self.buttons[button_text] = QPushButton(button_text)
            self.buttons[button_text].setFixedSize(80, 80)
            self.buttons[button_text].setFont(QFont('Arial', 18))
            buttons_layout.addWidget(
                self.buttons[button_text], position[0], position[1]
            )

        self.general_layout.addLayout(buttons_layout)

    def set_display_text(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def display_text(self):
        return self.display.text()

    def clear_display(self):
        self.set_display_text('')


class CalculatorController:
    def __init__(self, window, function):
        self._window = window
        self._evaluate = function

        self._connect_signals()

    def _build_expression(self, symbol):
        if self._window.display_text() == ERROR:
            self._window.clear_display()

        expression = self._window.display_text() + symbol
        self._window.set_display_text(expression)

    def _connect_signals(self):
        for button_text, button in self._window.buttons.items():

            if button_text not in {'=', 'C'}:
                button.clicked.connect(
                    partial(self._build_expression, button_text)
                )
        self._window.buttons['='].clicked.connect(self._calculate_result)
        self._window.display.returnPressed.connect(self._calculate_result)
        self._window.buttons['C'].clicked.connect(self._window.clear_display)

    def _calculate_result(self):
        result = self._evaluate(expression=self._window.display_text())
        self._window.set_display_text(result)


def evaluate_expression(expression):
    try:
        result = str(eval(expression))

    except (TypeError, ValueError):
        result = ERROR

    return result


def main():
    calculator = QApplication(sys.argv)
    window = Calculator()
    window.show()
    CalculatorController(window=window, function=evaluate_expression)
    sys.exit(calculator.exec_())


if __name__ == '__main__':
    main()