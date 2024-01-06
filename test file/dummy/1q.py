# import sys
# from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont
# class TextDisplayWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Text Display Window')

#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)

#         layout = QVBoxLayout(central_widget)

#         # Create a QLabel and set its text
#         label = QLabel('Hello, PyQt5!', self)
        
#         # You can also set additional properties, such as alignment and font
#         label.setAlignment(Qt.AlignCenter)
#         label.setFont(QFont('Arial', 16))

#         # Add the QLabel to the layout
#         layout.addWidget(label)

# def main():
#     app = QApplication(sys.argv)
#     window = TextDisplayWindow()
#     window.setGeometry(100, 100, 400, 200)  # Set the window size (x, y, width, height)
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QColor

class ColorChangingButton(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.button = QPushButton('Click me to change color', self)
        self.button.clicked.connect(self.changeColor)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def changeColor(self):
        # Change the button color when clicked
        self.button.setStyleSheet('background-color: red;')

        # Set a QTimer to reset the color after a certain delay (e.g., 500 milliseconds)
        self.timer = self.startTimer(500)

    def timerEvent(self, event):
        # Reset the button color when the timer event is triggered
        self.button.setStyleSheet('')
        self.killTimer(self.timer)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorChangingButton()
    window.show()
    sys.exit(app.exec_())
