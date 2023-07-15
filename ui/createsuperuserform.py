import PyQt5
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from settings.settings import Settings

class CreateSuperuserForm(QtWidgets.QVBoxLayout):
    settings= Settings()
    def __init__(self):
        super(CreateSuperuserForm, self).__init__()
        self.font= QtGui.QFont(
                    self.settings.FONT_TYPE,
                    self.settings.FONT_SIZE["medium"],
                    self.settings.FONT_WEIGHT)
        self.small_font=QtGui.QFont(
                    self.settings.FONT_TYPE,
                    self.settings.FONT_SIZE["small"],
                    self.settings.FONT_WEIGHT)
        self.title=QtWidgets.QLabel("Welcome to Password Manager\n Register to continue")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(self.font)
        self.addWidget(self.title)

        self.advice=QtWidgets.QLabel()
        self.advice.setText(
            "Please select strong password which will help to open your password vault."
        )
        self.advice.setFont(self.small_font)
        self.advice.setAlignment(Qt.AlignCenter)
        self.addWidget(self.advice)

        self.register_form=QtWidgets.QFormLayout()
        self.username_label=QtWidgets.QLabel("Username")
        self.username_label.setFont(self.small_font)
        self.username_input=QtWidgets.QLineEdit()
        self.username_input.setFont(self.small_font)
        self.register_form.addRow(self.username_label,self.username_input)

        self.password_label= QtWidgets.QLabel("Password")
        self.password_label.setFont(self.small_font)
        self.password_input=QtWidgets.QLineEdit()
        self.password_input.setFont(self.small_font)
        self.register_form.addRow(self.password_label, self.password_input)
        self.secret_advice=QtWidgets.QLabel()
        self.secret_advice.setText(
            "Select also strong secret phrase which will help you to change your super password."
        )
        
        self.secret_advice.setAlignment(Qt.AlignCenter)
        self.secret_advice.setFont(self.small_font)
        self.addWidget(self.secret_advice)
        self.secrete_phrase_label=QtWidgets.QLabel("Secret Phrase")
        self.secrete_phrase_label.setFont(self.small_font)
        self.secrete_phrase_input=QtWidgets.QLineEdit()
        self.secrete_phrase_input.setFont(self.small_font)
        self.register_form.addRow(self.secrete_phrase_label,self.secrete_phrase_input)
        self.addLayout(self.register_form)
        self.save_button= QtWidgets.QPushButton("Register and Continue")
        self.save_button.setFont(self.small_font)
        self.addWidget(self.save_button)
        self.addWidget(QtWidgets.QLabel())

# Impano Manzi Enock
