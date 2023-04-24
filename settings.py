from UI.settings import Ui_settings
from PySide6.QtWidgets import QWidget,QMessageBox
from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon

class settings(QWidget):
    settingsDone = Signal(list)
    def __init__(self, parent, f) -> None:
        super().__init__(parent, f)
        self.ui = Ui_settings()
        self.ui.setupUi(self)

        self.ui.apply.clicked.connect(self.onApply)
        self.ui.confirm.clicked.connect(self.onConfirm)
    
    def onConfirm(self):
        self.close()
        
    def onApply(self):
        self.settingsDone.emit([self.ui.baidu_api_key.text(),self.ui.baidu_secret_key.text()])
        reply = QMessageBox(self)
        reply.setWindowTitle("Message")
        reply.setText("应用成功")
        reply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        reply.setDefaultButton(QMessageBox.No)
        reply.setWindowIcon(QIcon()) # remove the icon
        reply.show()