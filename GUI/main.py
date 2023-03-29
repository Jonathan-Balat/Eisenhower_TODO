# from PySide2.QtCore import
# from PySide2.QtGui import
from gui_library.MainWindow_Class import MainWindowClass
from gui_library.Frame_Class import FrameClass
from PySide2.QtWidgets import QApplication, QFrame
"""
    References:
        - https://www.pythonguis.com/pyside2-tutorial/
"""


class GUIMain:

    def __init__(self, app_session, screen=0):
        if isinstance(app_session, QApplication):
            self.main_window = MainWindowClass(app_session, screen)

            # Refactor under each module, MENU, DASHBOARD, MAIN
            self.f_menu = FrameClass(self.main_window,
                                     (0, 0, 0, 0),
                                     "QFrame {background-color: rgba(128,60,128,255);}")

            self.f_dashboard = FrameClass(self.main_window,
                                          (0, 0, 0, 0),
                                          "QFrame {background-color: rgba(128,128,60,255);}")

            self.f_main = FrameClass(self.main_window,
                                     (0, 0, 0, 0),
                                     "QFrame {background-color: rgba(128,0,0,255);}")
            # Call once to resize widgets accordingly
            self.resizeEvent(None)

            # Override Widget event function with new assignment
            self.main_window.resizeEvent = self.resizeEvent

            self.main_window.show()
        else:
            print("[ERROR]: Application session does not exist!")

    def resizeEvent(self, event):
        self.f_menu.setGeometry(0, 0,
                                int(self.main_window.width()*0.1),
                                int(self.main_window.height()))

        self.f_dashboard.setGeometry(self.f_menu.width(), 0,
                                     self.main_window.width() - self.f_menu.width(),
                                     int(self.main_window.height()*0.1))

        self.f_main.setGeometry(self.f_menu.width(), self.f_dashboard.height(),
                                self.main_window.width() - self.f_menu.width(),
                                int(self.main_window.height() - self.f_dashboard.height()))



if "__main__" == __name__:
    app = QApplication([])
    main = GUIMain(app, 1)

    # Start the event loop.
    app.exec_()
