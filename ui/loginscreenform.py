from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from settings.settings import Settings
#--------------------------------------------------------------------
class LoginScreenForm(QtWidgets.QVBoxLayout):
    settings = Settings()
    def __init__(self):
        super(LoginScreenForm, self).__init__()
        self.font=QtGui.QFont(self.settings.FONT_TYPE,
                        self.settings.FONT_SIZE["small"],
                        self.settings.FONT_WEIGHT, 
                        False
                        )
        #--------------------------------------------------------------------------------
        # widgets declaration
        #--------------------------------------------------------------------------------

        self.header_text= QtWidgets.QLabel("PASSWORDS MANAGER\nLogin to continue")
        self.header_text.setAlignment(Qt.AlignCenter)
        self.header_text.setFont(
            QtGui.QFont(self.settings.FONT_TYPE,
                        self.settings.FONT_SIZE["large"],
                        self.settings.FONT_WEIGHT, 
                        False
                        ))
        self.username_label= QtWidgets.QLabel("USERNAME")
        self.username_label.setFont(self.font)
        self.username_label.setIndent(4)
        self.username_input=QtWidgets.QLineEdit()
        self.username_input.setFont(self.font)
        self.password_label=QtWidgets.QLabel("PASSWORD")
        self.password_label.setFont(self.font)
        self.password_label.setIndent(4)
        self.password_input=QtWidgets.QLineEdit()
        self.username_input.setFont(self.font)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setMaxLength(10)
        self.log_button=QtWidgets.QPushButton("Login")
        self.log_button.setFont(self.font)
        self.frgt_button=QtWidgets.QPushButton("Change super \n password")
        self.frgt_button.setFont(self.font)
        self.label=QtWidgets.QLabel("PASSWORD")
        self.form= QtWidgets.QFormLayout()
        self.form.setAlignment(Qt.AlignCenter)
        #--------------------------------------------------------------------------------
        # Adding widgets to layout
        #--------------------------------------------------------------------------------

        self.addWidget(self.header_text, )
        self.form.addRow(self.username_label,self.username_input)
        self.form.addRow(self.password_label,self.password_input)
        self.form.addRow(self.log_button,self.frgt_button)
        self.addLayout(self.form)
        self.addWidget(QtWidgets.QLabel())

# Impano Manzi Enock