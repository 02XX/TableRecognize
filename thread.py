from PySide6.QtCore import QThread,Signal
from PySide6.QtGui import QPixmap,QImage
from baiduTableRecognize import baiduTableRecognize
import requests,exception
class baiduTableRecognizeThread(QThread):
    recognizeDone = Signal(dict)
    def __init__(self, parent,mode) -> None:
        self.api_key = None
        self.secret_key = None
        self.arg = None
        self.mode = mode
        super().__init__(parent)
    def run(self) -> None:
        print("开始识别")
        r = baiduTableRecognize(self.api_key,self.secret_key,self.mode,self.arg)
        self.recognizeDone.emit(r)
        self.wait()
        print("识别结束")
        return super().run()
    
class urlRecognizeGetImage(QThread):
    getImageDone = Signal(QPixmap)
    def __init__(self, parent,url) -> None:
        super().__init__(parent)
        self.url = url
    def run(self) -> None:
        print("开始获取url图片")
        response = requests.get(self.url)
        if response.status_code != 200:
            raise exception.NetworkError("network error")
        if response:
            img = QImage.fromData(response.content)
            pixmap = QPixmap.fromImage(img)
            self.getImageDone.emit(pixmap)
            print("获取url图片成功")
        else:
            raise exception.UnknownError("unKnown Error. occurred in url RecognizeGetImage")
        return super().run()
    
