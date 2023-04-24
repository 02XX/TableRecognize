from UI.window import Ui_TableRecognize
from PySide6.QtWidgets import QMainWindow, QApplication,QTableWidgetItem,QFileDialog,QHeaderView
from PySide6.QtCore import QThread,Signal,Qt
from PySide6.QtGui import QKeyEvent
from dotenv import load_dotenv
import baiduTable,settings,os,baiduTableResponse,exception
load_dotenv()

class tableRecognize(QThread):
    recognizeDone = Signal(dict)
    def __init__(self, parent) -> None:
        self.api_key = None
        self.secret_key = None
        self.imagePath = None
        super().__init__(parent)
    def run(self) -> None:
        print("开始识别")
        r = baiduTable.baiduTableRecognize(self.api_key,self.secret_key,"image",self.imagePath)
        self.recognizeDone.emit(r)
        print("识别结束")
        return super().run()





class windows(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        #初始化
        self.ui = Ui_TableRecognize()
        self.ui.setupUi(self)
        self.settings = settings.settings(self,Qt.WindowType.Sheet)
        self.recognizeThread = tableRecognize(self)
        ## 菜单栏
        modeMenu = self.menuBar().addMenu("模式")
        modeMenu.addAction("图片")
        modeMenu.addAction("网址")
        modeMenu.addAction("PDF")
        settingsAction = self.menuBar().addAction("设置")
        #参数
        self.baidu_api_key = os.getenv("baidu_api_key")
        self.baidu_secret_key = os.getenv("baidu_secert_key")

        self.imagePath = None

        #槽函数
        self.recognizeThread.recognizeDone.connect(self.showTable)
        self.ui.startRecognize.clicked.connect(self.getBaiduTableRecognize)

        self.ui.image_file_button.clicked.connect(self.getImagePath)

        self.settings.settingsDone.connect(self.set)
        #菜单栏槽函数
        settingsAction.triggered.connect(self.showSettings)
        
    #显示设置界面
    def showSettings(self):
        self.settings.show()   

    #设置
    def set(self,settingParams):
        self.baidu_api_key = settingParams[0]
        self.baidu_secret_key = settingParams[1]

    def getImagePath(self):
        fileDialog = QFileDialog(self)
        path = fileDialog.getOpenFileName(self,caption="选择图片",filter="Images(*.png* .jpg* .jpeg);;All Files(*)")
        self.imagePath = path[0]
        self.ui.image_file.setText(path[0])

    #获取识别结果
    def getBaiduTableRecognize(self):
        if not self.baidu_api_key or not self.baidu_secret_key:
            raise ValueError("Please enter the key.")
        if not self.imagePath:
            raise ValueError("Please choose the image file path")
        self.recognizeThread.api_key = self.baidu_api_key
        self.recognizeThread.secret_key = self.baidu_secret_key
        self.recognizeThread.imagePath = self.imagePath
        self.recognizeThread.start()
        
    #展示表格
    def showTable(self,r):
        table = baiduTableResponse.formatTable(r)
        row = len(table)
        col = len(table[0])
        self.ui.tableWidget.setRowCount(row)
        self.ui.tableWidget.setColumnCount(col)
        #表格自适应窗口大小
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i in range(row):
            for j in range(col):
                self.ui.tableWidget.setItem(i,j,QTableWidgetItem(table[i][j]))
        # self.ui.tableWidget.resizeColumnsToContents()
        # self.ui.tableWidget.resizeRowsToContents()
    def copy(self):
        """
        复制多个选中单元格的内容到剪切板

        :return:
        """
        items = self.ui.tableWidget.selectedItems()
        if not items:
            return
        select_data = [[item.row(), item.column(), item.text()] for item in items]
        row_data = [item[0] for item in select_data]
        col_data = [item[1] for item in select_data]
        row_min, row_max = min(row_data), max(row_data)
        col_min, col_max = min(col_data), max(col_data)
        data = [[""] * (col_max - col_min + 1) for _ in range(row_max - row_min + 1)]
        for item in select_data:
            row, col, text = item
            data[row - row_min][col - col_min] = text
        QApplication.clipboard().setText("\n".join(["\t".join(item) for item in data]))

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if Qt.KeyboardModifier.ControlModifier and Qt.Key.Key_C:
            self.copy()
        return super().keyPressEvent(event)





if __name__ == "__main__":
    app = QApplication()
    window = windows()
    window.show()
    app.exec()