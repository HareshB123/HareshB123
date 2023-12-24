import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QInputDialog
import PyQt5.QtGui as qg
from PyQt5.QtGui import QIcon


class LoginPage(QWidget):
    # def open(self):
    #     self.window = QWidget.QMainWindow()
    #     self.ui = Ui_MainWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    def __init__(self):
        super().__init__()

        self.setWindowTitle('personal asssistant')

        self.setGeometry(300, 200, 400, 200)

        # Initialize user credentials (for demo purposes)
        self.user_credentials = {'user1': 'password1', 'user2': 'password2'}

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_entry = QLineEdit(self)

        self.password_label = QLabel("Password:")
        self.password_entry = QLineEdit(self)
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login)

        self.forgot_password_button = QPushButton("Forgot Password?", self)
        self.forgot_password_button.clicked.connect(self.forgot_password)

        self.sign_up_button = QPushButton("Sign Up", self)
        self.sign_up_button.clicked.connect(self.sign_up)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.login_button)
        layout.addWidget(self.forgot_password_button)
        layout.addWidget(self.sign_up_button)

        self.setLayout(layout)
    # def opener(self):
    #     self.login_button.clicked:lambda:

    def login(self):
        entered_username = self.username_entry.text()
        entered_password = self.password_entry.text()

        # Check if the entered username exists and the password is correct (for demo purposes)
        if entered_username in self.user_credentials and self.user_credentials[entered_username] == entered_password:
            
            QMessageBox.information(self, "Login Successful", "Welcome, {}".format(entered_username))
            
            Ui_MainWindow()
            
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def forgot_password(self):
        QMessageBox.information(self, "Forgot Password", "Password reset functionality not implemented in this demo.")

    def sign_up(self):
        new_username, ok = QInputDialog.getText(self, 'Sign Up', 'Enter a new username:')
        if ok and new_username:
            # Check if the username already exists
            if new_username in self.user_credentials:
                QMessageBox.warning(self, "Sign Up Failed", "Username already exists. Try a different username.")
                
            else:
                new_password, ok = QInputDialog.getText(self, 'Sign Up', 'Enter a password for {}:'.format(new_username))
                if ok and new_password:
                    # Store the new user credentials
                    self.user_credentials[new_username] = new_password
                    QMessageBox.information(self, "Sign Up Successful", "Account created for {}".format(new_username))
                else:
                    QMessageBox.warning(self, "Sign Up Failed", "Invalid password or user canceled.")
        else:
            QMessageBox.warning(self, "Sign Up Failed", "Invalid username or user canceled.")
    
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec_())
