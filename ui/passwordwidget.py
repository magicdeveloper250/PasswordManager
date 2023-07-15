from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from settings.settings import Settings
class PasswordWidget(QtWidgets.QListWidgetItem):
    title="your password"
    settings= Settings()
    def __init__(self,no,username,site,created,password,PASSWORD_KEY):
        super(PasswordWidget, self).__init__()
        self.setFont(QtGui.QFont(self.settings.FONT_TYPE, 
                               self.settings.FONT_SIZE["small"]))
        #--------------------------------------------------------------------------------
        # widgets declaration
        #--------------------------------------------------------------------------------
        
        self.pid=no
        self.password=password
        self.site=site
        self.username=username
        self.created=created
        self.PASSWORD_KEY=PASSWORD_KEY
        self.title=f"{self.site}'s password"
        #--------------------------------------------------------------------------------
        # Adding widgets to layout
        #--------------------------------------------------------------------------------

        self.setText(f"   {self.pid}\t{self.trim_word(self.site)}\t{self.trim_word(self.username)}\t{self.created}   ")
        self.setToolTip(self.title)
         
        #self.addWidget(self.password,0,2)
        #self.addWidget(self.site,0,3)
        #self.addWidget(self.change,0,4)
        #self.addWidget(self.delete,0,5)
    def trim_word(self,word:str):
        if len(word)>20:
            word =word.replace(word[20:],"")
            return word
             
        else:
            count= 20-len(word)
            word=word + " "*count

            return word
def trim_word(word:str):
        if len(word)>24:
            word =word.replace(word[24:],"")
            return word
             
        else:
            count= 20-len(word)
            word=word + " "*count

            return word
def test():
    name="impanommmffkjfjfhjhjghgfhgfhhgjh"
    print(name[11:])
    new = trim_word(name)
    print(new)
    print(len(new))

if __name__=="__main__":
    test()

# Impano Manzi Enock