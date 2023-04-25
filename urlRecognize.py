from UI.urlRecognize import Ui_urlRecognize
from PySide6.QtWidgets import QWidget,QApplication,QTableWidgetItem,QHeaderView
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt
from thread import baiduTableRecognizeThread,urlRecognizeGetImage
import TableFormat,os
class urlRecognize(QWidget):
    def __init__(self, parent) -> None:
        #初始化
        super().__init__(parent)
        self.ui = Ui_urlRecognize()
        self.ui.setupUi(self)
        
        #参数
        self.baidu_api_key = os.getenv("baidu_api_key")
        self.baidu_secret_key = os.getenv("baidu_secret_key")
        self.url = None
        #槽函数
        self.ui.startRecognize.clicked.connect(self.getBaiduTableRecognize)
        # self.recognizeThread.recognizeDone.connect(self.showTable)
        self.ui.urlPath.textChanged.connect(self.getUrlImage)
        # self.getImage.getImageDone.connect(self.showImage)
        #父槽函数
        parent.baiduKeySettingsDone.connect(self.settingKey)
    #设置Key
    def settingKey(self,settingParams):
        self.baidu_api_key = settingParams[0]
        self.baidu_secret_key = settingParams[1]

    def getUrlImage(self):
        self.getImage = urlRecognizeGetImage(self,self.url)
        self.getImage.getImageDone.connect(self.showImage)
        print("执行getUrlImage线程")
        self.getImage.url = self.ui.urlPath.text()
        self.getImage.start()
    def showImage(self,image):
        self.ui.image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.image.setPixmap(image)

    def getBaiduTableRecognize(self):
        self.recognizeThread = baiduTableRecognizeThread(self,"url")
        self.recognizeThread.recognizeDone.connect(self.showTable)
        if not self.baidu_api_key or not self.baidu_secret_key:
            raise ValueError("Please enter the key.")

        self.recognizeThread.api_key = self.baidu_api_key
        self.recognizeThread.secret_key = self.baidu_secret_key
        self.recognizeThread.arg = self.ui.urlPath.text()
        self.recognizeThread.start()
    #展示表格
    def showTable(self,r):
        table = TableFormat.baiduTableFormat(r)
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
# if __name__ == "__main__":
#     app = QApplication()
#     window = urlRecognize(None)
#     window.show()
#     app.exec()