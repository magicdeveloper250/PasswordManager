from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from settings.settings import Settings
from passwordgenerator import password
class CreateShowScreenForm(QtWidgets.QVBoxLayout):
    title="create new password"
    settings= Settings()
    def __init__(self):
        super(CreateShowScreenForm, self).__init__()
        self.font=QtGui.QFont(
                    self.settings.FONT_TYPE,
                    self.settings.FONT_SIZE["medium"],
                    self.settings.FONT_WEIGHT)
        self.small_font=QtGui.QFont(
                    self.settings.FONT_TYPE,
                    self.settings.FONT_SIZE["small"],
                    self.settings.FONT_WEIGHT)
        #--------------------------------------------------------------------------------
        # widgets declaration
        #--------------------------------------------------------------------------------
        self.labels_layout=QtWidgets.QHBoxLayout()
        self.email_label=QtWidgets.QLabel("Username")
        self.email_label.setFont(self.small_font)
        self.site_label=QtWidgets.QLabel("site")
        self.site_label.setFont(self.small_font)
        self.labels_layout.addWidget(self.email_label)
        self.labels_layout.addWidget(self.site_label)

        self.inputs_layout= QtWidgets.QHBoxLayout()
        self.username_email_input=QtWidgets.QLineEdit()
        self.username_email_input.setPlaceholderText("Username or email")
        self.username_email_input.setFont(self.small_font)
        self.site_input=QtWidgets.QLineEdit()
        self.site_input.setFont(self.small_font)
        self.site_input.setPlaceholderText("www.site.com")
        self.inputs_layout.addWidget(self.username_email_input)
        self.inputs_layout.addWidget(self.site_input)

        self.generate_button=QtWidgets.QPushButton("Generate password")
        self.generate_button.setFont(self.font)
        self.generated_layout=QtWidgets.QHBoxLayout()
        self.generated_password= QtWidgets.QLabel()
        self.generated_password.setFixedHeight(35)
        self.generated_password.setFont(QtGui.QFont(
                    self.settings.FONT_TYPE,
                    12,
                    self.settings.FONT_WEIGHT))
        self.save_button=QtWidgets.QPushButton("Save")
        self.save_button.setFixedWidth(40)
        self.save_button.setFont(self.small_font)
        self.generated_layout.addWidget(self.generated_password)
        self.generated_layout.addWidget(self.save_button)

        self.password_show_layout= QtWidgets.QListWidget()
         

        

        #--------------------------------------------------------------------------------
        # Adding widgets to layout
        #--------------------------------------------------------------------------------

        self.addLayout(self.labels_layout)
        self.addLayout(self.inputs_layout)
        self.addWidget(self.generate_button)
        self.addLayout(self.generated_layout)
        self.addWidget(self.password_show_layout)
        #-------------------------------------------------------------------------------
     
# Impano Manzi Enock