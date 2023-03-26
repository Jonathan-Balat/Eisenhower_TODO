from PySide2.QtWidgets import QMainWindow


class MainWindowClass(QMainWindow):
    session = None
    current_screen = None
    window_half_size = None

    def __init__(self, session, screen=0):
        super(MainWindowClass, self).__init__()
        MainWindowClass.session = session

        self.setMouseTracking(True)
        self.select_screen(screen)
        self.resize_window()

    #################### EVENTS ####################
    # FOr debugging only
    # def event(self, event):
    #     if event.type() == event.Type.Move:
    #         # print("DRAGGING")
    #         screen = MainWindowClass.session.screenAt(event.pos())
    #         if screen != MainWindowClass.current_screen:
    #             self.switch_screen(screen)
    #             self.resize_window()
    #     else:
    #         ...
    #     return True
    #         # print("Other event", event.type())

    @staticmethod
    def switch_screen(screen):
        if screen is not None:
            MainWindowClass.current_screen = screen

    @staticmethod
    def select_screen(screen: int = 0):
        """https://doc.qt.io/qtforpython-5/PySide2/QtGui/QScreen.html"""
        if 0 < screen < len(MainWindowClass.session.screens()):
            screen = screen
        else:
            screen = 0

        MainWindowClass.current_screen = MainWindowClass.session.screens()[screen]

    def resize_window(self):
        x = MainWindowClass.current_screen.availableGeometry().x()
        y = MainWindowClass.current_screen.availableGeometry().y()
        w = MainWindowClass.current_screen.availableGeometry().width()
        h = MainWindowClass.current_screen.availableGeometry().height()
        MainWindowClass.window_half_size = (w / 2, h / 2)

        self.move(x + w / 4, y + h / 4)

        self.setMinimumSize(w / 2, h / 2)
        self.setMaximumSize(w, h)
