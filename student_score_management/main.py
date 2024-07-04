from PyQt5.Qt import QApplication
import sys
from pages.LoginPage import LoginPage
from PyQt5 import QtCore
def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # 初始化整个QT应用类，sys.argv是python启动外部传参
    app = QApplication(sys.argv)
    login_page = LoginPage()
    # # 阻塞当前路线，并启动pyqt应用
    app.exec_()


if __name__ == "__main__":
    main()
