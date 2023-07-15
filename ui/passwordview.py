from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from settings.settings import Settings
import cryptocode
from .passwordwidget import PasswordWidget


#--------------------------------------------------
class PasswordView(QtWidgets.QVBoxLayout):
    settings= Settings()
    def __init__(self, child):
        super(PasswordView, self).__init__()
        self.font= QtGui.QFont(
            self.settings.FONT_TYPE,
            self.settings.FONT_SIZE["small"],
            self.settings.FONT_WEIGHT
        )
        change_screen=  None
        self.child= child
        self.pid= self.child.pid
        self.title= QtWidgets.QLabel()
        self.title.setText(self.child.title)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(self.font)
        self.password_form=QtWidgets.QHBoxLayout()
        self.password_form.setAlignment(Qt.AlignCenter)
        self.password_label= QtWidgets.QLabel("Password: ")
        self.password_label.setFont( self.font)
        self.password=QtWidgets.QLineEdit()
        self.PASSWORD_KEY=self.child.PASSWORD_KEY
        decrypted_password= cryptocode.decrypt(self.child.password,self.PASSWORD_KEY )
        if type(self.child)!= PasswordWidget:
            decrypted_password= self.child.old_password_input.text() 


        self.password.setText(decrypted_password)
        self.password.setDisabled(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setFont(self.font)
        self.copy_btn=QtWidgets.QPushButton("copy")
        self.copy_btn.setFont(self.font)
        self.show_btn=QtWidgets.QPushButton("Show")
        self.show_btn.setFont(self.font)
        self.password_form.addWidget(self.password_label)
        self.password_form.addWidget(self.password)
        self.password_form.addWidget(self.show_btn)
        self.password_form.addWidget(self.copy_btn)
         
        self.site= QtWidgets.QLabel(self.child.site)
        self.site.setFont(self.font)
         
        self.username= QtWidgets.QLabel(self.child.username)
        self.username.setFont(self.font)
        self.password_form2=QtWidgets.QVBoxLayout()
        self.password_form2.setAlignment(Qt.AlignCenter)
         
        self.password_form2.addWidget(self.site)
         
        self.password_form2.addWidget(self.username)
        self.buttons_layout= QtWidgets.QHBoxLayout()
        self.back_btn= QtWidgets.QPushButton("Back")
        self.back_btn.setFont(self.font)
        self.back_btn.setAutoFillBackground(True)
        self.back_btn.setCursor(Qt.CursorShape.OpenHandCursor)
        
        # self.change_btn=QtWidgets.QPushButton("Change")
        # self.change_btn.setFont(self.font)
        self.delete_btn=QtWidgets.QPushButton("Delete")
        self.delete_btn.setFont(self.font)

        self.status_bar= QtWidgets.QStatusBar()
        self.status_bar.setFixedHeight(25)
        self.status_bar.setFont(QtGui.QFont("Arial",12,600,True))

        self.buttons_layout.addWidget(self.back_btn)
        # self.buttons_layout.addWidget(self.change_btn)
        self.buttons_layout.addWidget(self.delete_btn)
        #--------------------------------------------------------------------------------#
        #                       Add widgets to layout                                    #                                                        #
        #--------------------------------------------------------------------------------#
        self.addWidget(self.title)
        self.addLayout(self.password_form)
        self.addLayout(self.password_form2)
        self.addLayout(self.buttons_layout)
        self.addWidget(self.status_bar)
        self.copy_btn.clicked.connect(self.copy_password)
        self.show_btn.clicked.connect(self.toggle)
        #--------------------------------------------------------------------------------#
        #                               methods                                          #                                                                 #
        #--------------------------------------------------------------------------------#
    def copy_password(self):
        clipboard=QtWidgets.QApplication.clipboard()
        clipboard.setText(self.password.text())
        self.status_bar.showMessage("Password Copied", 5000)
    def show_password(self):
        self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
    def hide_password(self):
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    def toggle(self):
        if self.show_btn.text().__eq__("Show"):
            self.show_password()
            self.show_btn.setText("Hide")
        else:
            self.hide_password()
            self.show_btn.setText("Show")

# Impano Manzi Enock
