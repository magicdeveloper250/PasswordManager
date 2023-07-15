from dbmanager.database import PasswordManager
from PyQt5 import QtWidgets,QtGui
from ui.changepasswordwidget import ChangePasswordWidget
from ui.createshowscreenform import CreateShowScreenForm
from ui.frame import Frame
from ui.loginscreenform import LoginScreenForm
from ui.passwordview import PasswordView
from ui.passwordwidget import PasswordWidget
from ui.window import Window
from ui.confirm import ConfirmDialog
from ui.createsuperuserform import CreateSuperuserForm
from passwordgenerator import password
from settings.settings import Settings
import sys
import cryptocode
import os

#------------------------------------------------------------------
basedir= os.path.dirname(__file__)
def main():
    #--------------------------------------------------------------
    # app properties declaration
    #--------------------------------------------------------------
    app= QtWidgets.QApplication(sys.argv)
    db=PasswordManager()
    window=Window()
    window.setWindowTitle("Passwords Manager by Impano Manzi Enock")
    window.setWindowIcon(QtGui.QIcon("icon.jpg"))
    #----------------------------------------------------------------
    # slots declarations
    #----------------------------------------------------------------
    def render_create_superuser_form():
        layout=CreateSuperuserForm()
        frame=Frame()
        frame.setLayout(layout)
        window.setCentralWidget(frame)
        window_size= QtWidgets.QDesktopWidget().screenGeometry()
        window.setFixedWidth(window_size.width()//2)
        window.setFixedHeight(window_size.height()//2)
        layout.save_button.clicked.connect(lambda:create_superuser(layout))
    def create_superuser(layout):
        username=layout.username_input.text()
        password=layout.password_input.text().encode()
        secrete_phrase=layout.secrete_phrase_input.text().encode()
        if (username and password) and secrete_phrase:
            try:
                PasswordManager().create_superuser(username, password, secrete_phrase)
                render_login_form()
            except Exception as e:
                QtWidgets.QMessageBox.critical(window, "Not registered", str(e))
        else:
            QtWidgets.QMessageBox.critical(window, "Incomplete", "Please, fill out all above fields.")


    def render_login_form():
        login_layout=LoginScreenForm()
        frame=Frame()
        frame.setLayout(login_layout)
        window.setCentralWidget(frame)
        window_size= QtWidgets.QDesktopWidget().screenGeometry()
        window.setFixedWidth(window_size.width()//3)
        window.setFixedHeight(window_size.height()//3)
        login_layout.log_button.clicked.connect(lambda:login(login_layout))
        login_layout.frgt_button.clicked.connect(lambda:goto_change_password(login_layout))



    def goto_login():
        try:
            registered=PasswordManager().user_registered()
        except:
            registered= Settings().REGISTERED

        if not registered:
            PasswordManager().create()
            render_create_superuser_form()
        else:
            render_login_form()
            
    #----------------------------------------------------------------
    def login(login_layout):
        username= login_layout.username_input.text()
        password= login_layout.password_input.text()
        if username and password:
            try:
                user_exist= PasswordManager().display_user(username, password)
                if user_exist:
                    goto_show_passwords()
                else:
                    QtWidgets.QMessageBox.information(window,"Not found", "User Not Found")
            except Exception as e:
                QtWidgets.QMessageBox.information(window,"Not found", "User Not Found")
        else:
            QtWidgets.QMessageBox.critical(window,"incomplete", "Please, fill out all fields.")

        
            
            
    #------------------------------------------------------------------
    def goto_show_passwords():
        frame=Frame()
        create_password_layout=CreateShowScreenForm()
        frame.setLayout(create_password_layout)
        window.setCentralWidget(frame)
        window_size=QtWidgets.QDesktopWidget().screenGeometry()
        window.setFixedWidth(window_size.width()//2)
        window.setFixedHeight(window_size.height()//2)
        display_password_list(create_password_layout.password_show_layout)
        create_password_layout.generate_button.clicked.connect(lambda:generate_password(create_password_layout))
        create_password_layout.save_button.clicked.connect(lambda:save_new_password(create_password_layout))
        create_password_layout.password_show_layout.itemDoubleClicked.connect(view_password)

    #------------------------------------------------------------------
    
    def display_password_list(layout):
        layout.clear()
        records=[record for record in db.display_password()]
        for record in records:
            pid=record[0]
            username=record[1]
            site=record[2]
            created=record[3]
            password=record[4]
            PASSWORD_KEY=username+site
            layout.addItem(PasswordWidget(pid, username, site, created,password, PASSWORD_KEY))
    #----------------------------------------------------------------------
    def generate_password(layout):
        if(layout.username_email_input.text() and layout.site_input.text()):
            complex_password=password.generate_complex_password()
            layout.generated_password.setText(complex_password)
        else:
            QtWidgets.QMessageBox.critical(window,"incomplete", "Please, fill out all above fields.")
        
    def save_new_password(create_password_layout):
        password= create_password_layout.generated_password.text()
        site= create_password_layout.site_input.text()
        username=create_password_layout.username_email_input.text()
        
        if (password and site) and username:
            PASSWORD_KEY=create_password_layout.username_email_input.text()+create_password_layout.site_input.text()
            encrypted_version=cryptocode.encrypt(password,PASSWORD_KEY)
            try:
                db.create_new_password(encrypted_version, site, username)
            except Exception as ex:
                QtWidgets.QMessageBox.critical(window, "Error", "{0}".format(ex))
            create_password_layout.generated_password.setText("")
            create_password_layout.site_input.setText("")
            create_password_layout.username_email_input.setText("")
            display_password_list(create_password_layout.password_show_layout)
        else:
            QtWidgets.QMessageBox.critical(window, "incomplete", "Please, Fill out all above fields")

         
    #-------------------------------------------------------------------
    def view_password(child):
        frame= Frame()
        layout= PasswordView(child)
        # layout.change_btn.clicked.connect(lambda:goto_change_password(layout))
        layout.back_btn.clicked.connect(back_to_previous_window)
        layout.delete_btn.clicked.connect(lambda:go_delete_password(layout.pid))
        window_size=QtWidgets.QDesktopWidget().screenGeometry()
        window.setFixedWidth(window_size.width()//2)
        window.setFixedHeight(window_size.height()//2)
        frame.setLayout(layout)
        window.setCentralWidget(frame)
    #------------------------------------------------------------------
    def goto_change_password(current):
        login=LoginScreenForm()
        if str(type(current))!=str(type(login)):
            login=LoginScreenForm()
            frame=Frame()
            layout= ChangePasswordWidget(current)
            layout.old_password_input.setText(current.password.text())
            layout.old_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
            layout.password=current.password.text()
            frame.setLayout(layout)
            window_size=QtWidgets.QDesktopWidget().screenGeometry()
            window.setFixedWidth(window_size.width()//2)
            window.setFixedHeight(window_size.height()//2)
            window.setCentralWidget(frame)
            layout.save_btn.clicked.connect(lambda:change_password(layout))
            layout.back_btn.clicked.connect(lambda:back_to_view_passwords(layout))
        
        else:
            
            frame=Frame()
            layout= ChangePasswordWidget(current)
            layout.old_password_input.setDisabled(False)
            layout.old_password_input.setEchoMode(QtWidgets.QLineEdit.Normal)
            frame.setLayout(layout)
            window.setCentralWidget(frame)
            layout.save_btn.clicked.connect(lambda:change_password(layout))
            layout.back_btn.clicked.connect(lambda:goto_login())
        
        
        
    #------------------------------------------------------------------

    def change_password(layout):
        change_password_layout=layout
        pid=change_password_layout.pid 
        username=change_password_layout.username_input.text()
        old_password= change_password_layout.old_password_input.text()
        new_password= change_password_layout.new_password_input.text()
        secrete_phrase= change_password_layout.secrete_phrase_input.text()

        
        if pid:
            try:
                if new_password:
                    change_password_layout.password= new_password
                    db.change_password(pid,new_password)
                    back_to_view_passwords(change_password_layout)
                    QtWidgets.QMessageBox.information(window, "changed", "Password changed\nSuccessfully.")
                else:
                    change_password_layout.password= old_password
                    QtWidgets.QMessageBox.critical(window, "incomplete", "incomplete inputs")  
            except:
                QtWidgets.QMessageBox.Warning(window,"Not changed.", "password not changed try again?")
        else:
            try:
                
                db.change_user_password(username,old_password, new_password, secrete_phrase)
                goto_login()
                QtWidgets.QMessageBox.information(window, "changed","Password changed." )
            except Exception as ex:
                QtWidgets.QMessageBox.warning(window, "Warning", str(ex))
    #-----------------------------------------------------------------
    def delete_password(dialog,pid):
        PasswordManager().delete_password(pid)
        dialog.hide()
        back_to_previous_window()

    def go_delete_password(pid):
        dialog= ConfirmDialog(window)
        dialog.confirm_btn.clicked.connect(lambda:delete_password(dialog,pid))
        dialog.reject_btn.clicked.connect(lambda:dialog.hide())
        dialog.open()
         
    #----------------------------------------------------------------

    def back_to_previous_window(): 
        goto_show_passwords()
    def back_to_view_passwords(child):
        view_password(child)

    #----------------------------------------------------------------


    #------------------------end of slots declarations---------------
 
    #-----------------------------------------------------------------
    # display window and exit block
    #-----------------------------------------------------------------
    goto_login()
    window.show()
    sys.exit(app.exec_())
    #-------exit block----------------------

#--------------------------------------------------------------------

if __name__=="__main__":
    main()

# Impano Manzi Enock