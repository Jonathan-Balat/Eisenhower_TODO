from PySide2.QtCore import QSize
# from PySide2.QtGui import
from gui_library.MainWindow_Class import MainWindowClass
from Menu_Class.Menu_Class import MenuClass
from gui_library.Frame_Class import FrameClass
from PySide2.QtWidgets import QApplication

"""
    References:
        - https://www.pythonguis.com/pyside2-tutorial/
"""


class GUIMain(MainWindowClass):

    TOOL_TIP_DURATION = 5000

    DISP_MENU_W = 0.1
    DISP_DASH_H = 0.15

    def __init__(self, app_session, screen=0):
        if isinstance(app_session, QApplication):
            super(GUIMain, self).__init__(app_session, screen)

            # TODO: Refactor under each module, MENU, DASHBOARD, MAIN
            self.menu = MenuClass(self)

            self.f_dashboard = FrameClass(self,
                                          (0, 0, 0, 0),
                                          "QFrame {background-color: rgba(128,128,60,255);}")

            self.f_main = FrameClass(self,
                                     (0, 0, 0, 0),
                                     "QFrame {background-color: rgba(128,0,0,255);}")

            # Override Widget event function with new assignment
            # self.resizeEvent = self.resizeEvent

            self.show()

        else:
            print("[ERROR]: Application session does not exist!")

    def resizeEvent(self, event):
        self.menu.resizeEvent(None)

        self.f_dashboard.move(self.menu.width(), 0)
        self.f_dashboard.setMinimumSize(self.width() - self.menu.width(), 100)
        self.f_dashboard.setMaximumSize(self.width() - self.menu.width(), int(self.height()*GUIMain.DISP_DASH_H))
        self.f_dashboard.resize(self.width(), self.height())

        # self.f_dashboard.setGeometry(self.menu.width(), 0,
        #                              self.width() - self.menu.width(),
        #                              int(self.height()*GUIMain.DISP_DASH_H))

        self.f_main.setGeometry(self.menu.width(), self.f_dashboard.height(),
                                self.width() - self.menu.width(),
                                int(self.height() - self.f_dashboard.height()))


if "__main__" == __name__:
    app = QApplication([])
    main = GUIMain(app, 0)

    # Start the event loop.
    app.exec_()
