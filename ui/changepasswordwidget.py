from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from .loginscreenform import LoginScreenForm
from settings.settings import Settings

class ChangePasswordWidget(QtWidgets.QVBoxLayout):
    settings= Settings()
    def __init__(self, child):
        super(ChangePasswordWidget, self).__init__()
        self.font=QtGui.QFont(
                    self.settings.FONT_TYPE,
                    self.settings.FONT_SIZE["medium"],
                    self.settings.FONT_WEIGHT)
        #--------------------------------------------------------------------------------
        # widgets declaration
        #--------------------------------------------------------------------------------
        lgscrn=LoginScreenForm()
        
        self.child= child
        self.pid=self.child.pid if str(type(self.child))!=str(type(lgscrn)) else None
        self.title= self.child.title.text() if self.pid else None
        self.label_title= QtWidgets.QLabel()
        self.label_title.setText("Change Password.")
        self.label_title.setFont(self.font)
        self.label_title.setAlignment(Qt.AlignCenter)
        # self.PASSWORD_KEY=self.child.PASSWORD_KEY

        self.username= self.child.username.text() if str(type(child))!=str(type(lgscrn)) else None
        
        self.username_label=QtWidgets.QLabel("Username")
        self.username_label.setFont(self.font)
        self.username_input=QtWidgets.QLineEdit()
        self.username_input.setFont(self.font)

        self.old_password_label=QtWidgets.QLabel("Old password")
        self.old_password_label.setFont(self.font)
        self.old_password_input=QtWidgets.QLineEdit()
        self.old_password_input.setFont(self.font)
        self.old_password_input.setDisabled(True)
        self.old_password_input.setEchoMode(QtWidgets.QLineEdit.Normal)


        self.secrete_phrase_label=QtWidgets.QLabel("Secret Phrase")
        self.secrete_phrase_label.setFont(self.font)
        self.secrete_phrase_input=QtWidgets.QLineEdit()
        self.secrete_phrase_input.setFont(self.font)

        
        self.password=None

        self.site= self.child.site.text() if str(type(child))!=str(type(lgscrn)) else None

        self.new_password_label=QtWidgets.QLabel("New password")
        self.new_password_label.setFont(self.font)
        self.new_password_input=QtWidgets.QLineEdit()
        self.new_password_input.setFont(self.font)
        self.new_password_input.setPlaceholderText("New password")
        self.new_password_input.setPlaceholderText("New password")

        self.save_btn=QtWidgets.QPushButton("save")
        self.save_btn.setFont(self.font)

        self.back_btn= QtWidgets.QPushButton()
        self.back_btn.setText("Back")
        self.back_btn.setFont(self.font)

        self.btn_layout= QtWidgets.QHBoxLayout()
        self.form=QtWidgets.QFormLayout()
        #--------------------------------------------------------------------------------
        # Adding widgets to layout
        #--------------------------------------------------------------------------------
        
        self.form.addRow(self.username_label, self.username_input)
        self.form.addRow(self.secrete_phrase_label, self.secrete_phrase_input)
        self.form.addRow(self.old_password_label,self.old_password_input)
        self.form.addRow(self.new_password_label,self.new_password_input)
        self.addWidget(self.label_title)
        self.addLayout(self.form)
        self.btn_layout.addWidget(self.back_btn)
        self.btn_layout.addWidget(self.save_btn)
        
        self.addLayout(self.btn_layout)
        self.addWidget(QtWidgets.QLabel())
 
#  Impano Manzi Enock