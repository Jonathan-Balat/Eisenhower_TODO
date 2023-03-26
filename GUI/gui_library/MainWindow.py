from PySide2.QtWidgets import QMainWindow

class MainWindowClass(QMainWindow):
    session = None

    def __init__(self, session, screen=0):
        super(MainWindowClass, self).__init__()
        MainWindowClass.session = session

        self.select_screen(screen)
        self.resize_window()

    @staticmethod
    def select_screen(screen: int = 0):
        """https://doc.qt.io/qtforpython-5/PySide2/QtGui/QScreen.html"""
        if 0 < screen < len(MainWindowClass.session.screens()):
            MainWindowClass.screen_selected = MainWindowClass.session.screens()[screen]
        else:
            MainWindowClass.screen_selected = MainWindowClass.session.screens()[0]

    def resize_window(self):
        x = MainWindowClass.screen_selected.availableGeometry().x()
        y = MainWindowClass.screen_selected.availableGeometry().y()
        w = MainWindowClass.screen_selected.availableGeometry().width()
        h = MainWindowClass.screen_selected.availableGeometry().height()

        self.move(x + w / 4, y + h / 4)

        self.setMinimumSize(w / 2, h / 2)
        self.setMaximumSize(w, h)
