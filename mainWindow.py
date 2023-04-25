from UI.window import Ui_TableRecognize
from PySide6.QtWidgets import QMainWindow, QApplication,QStackedWidget
from PySide6.QtCore import Signal,Qt
from imageRecongnize import imageRecognize
from urlRecognize import urlRecognize
from dotenv import load_dotenv
import settings,os
load_dotenv()


class windows(QMainWindow):
    baiduKeySettingsDone = Signal(list)
    def __init__(self,parent) -> None:
        super().__init__(parent)
        #初始化

        self.ui = Ui_TableRecognize()
        self.ui.setupUi(self)
        self.settings = settings.settings(self,Qt.WindowType.Sheet)

        self.setWindowTitle("表格识别")


        self.stackedWidget = QStackedWidget()
        #index 0
        self.stackedWidget.addWidget(imageRecognize(self))
        #index 1
        self.stackedWidget.addWidget(urlRecognize(self))
        
        self.ui.verticalLayout.addWidget(self.stackedWidget)
        ## 菜单栏
        modeMenu = self.menuBar().addMenu("模式")
        self.imageAction = modeMenu.addAction("图片")
        self.urlAction = modeMenu.addAction("网址")
        self.pdfAction = modeMenu.addAction("PDF")
        self.settingsAction = self.menuBar().addAction("设置")


        #槽函数
        self.settings.settingsDone.connect(self.set)
        #菜单栏槽函数
        self.settingsAction.triggered.connect(self.showSettings)
        self.imageAction.triggered.connect(self.showImageAction)
        self.urlAction.triggered.connect(self.showUrlAction)
    #显示设置界面
    def showSettings(self):
        self.settings.show()

    #设置
    def set(self,settingParams):
        #百度表格识别key
        self.baiduKeySettingsDone.emit(settingParams)
    def showImageAction(self):
        self.stackedWidget.setCurrentIndex(0) #index 0 image recognize
    def showUrlAction(self):
        self.stackedWidget.setCurrentIndex(1) #index 1 url recognize

if __name__ == "__main__":
    app = QApplication()
    window = windows(None)
    window.show()
    app.exec()