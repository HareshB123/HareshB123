import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QPushButton, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Multiple Windows Example')

        # Create a tab widget
        self.tab_widget = QTabWidget(self)

        # Create a central widget and set the tab widget as its layout
        central_widget = QWidget(self)
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.tab_widget)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        # Create a button to add new tabs
        add_tab_button = QPushButton('Add Tab', self)
        add_tab_button.clicked.connect(self.add_tab)

        # Create a layout for the central widget
        central_layout.addWidget(add_tab_button)

        # Show the main window
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def add_tab(self):
        # Create a new tab (window) and add it to the tab widget
        new_tab = QWidget(self)
        tab_index = self.tab_widget.addTab(new_tab, f'Tab {self.tab_widget.count() + 1}')
        self.tab_widget.setCurrentIndex(tab_index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
