# from PySide2.QtCore import
# from PySide2.QtGui import
from gui_library.MainWindow import MainWindowClass
from PySide2.QtWidgets import QApplication
from time import time
"""
    References:
        - https://www.pythonguis.com/pyside2-tutorial/
"""


class GUIMain:

    def __init__(self, app_session, screen=0):
        self.main_window = MainWindowClass(app_session, screen)

        self.main_window.show()


if "__main__" == __name__:
    app = QApplication([])
    main = GUIMain(app, 1)

    # Start the event loop.
    app.exec_()
