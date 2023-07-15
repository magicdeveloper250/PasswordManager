from PyQt5 import QtWidgets
from PyQt5 import QtGui
from settings.settings import Settings
 

class ConfirmDialog(QtWidgets.QDialog):
    settings=Settings()
    def __init__(self, layout):
        super(ConfirmDialog, self).__init__(layout)
        self.font= QtGui.QFont(
            self.settings.FONT_TYPE,
            self.settings.FONT_SIZE["small"],
            self.settings.FONT_WEIGHT
        )
        self.confirm_layout=QtWidgets.QVBoxLayout()
        self.btn_layout=QtWidgets.QHBoxLayout()
        self.message=QtWidgets.QLabel()
        self.message.setText("Do you want to delete this password?")
        self.message.setFont(self.font)

        self.confirm_btn= QtWidgets.QPushButton()
        self.confirm_btn.setText("Yes")
        self.confirm_btn.setFont(self.font)

        self.reject_btn= QtWidgets.QPushButton()
        self.reject_btn.setText("No")
        self.reject_btn.setFont(self.font)
        
        

        # adding widget to layout
        self.confirm_layout.addWidget(self.message)
        self.btn_layout.addWidget(self.confirm_btn)
        self.btn_layout.addWidget(self.reject_btn)
        self.confirm_layout.addLayout(self.btn_layout)
        # setting our confirm-layout to main dialog layout
        self.setWindowTitle("Confirm deletion.")
        self.setLayout(self.confirm_layout)
    
        
        
    

# Impano Manzi Enock
    
