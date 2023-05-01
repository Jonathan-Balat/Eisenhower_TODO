from GUI.gui_library.Frame_Class import FrameClass
from GUI.gui_library.Button_Class import ButtonClass
from GUI.gui_library.Animator_class import AnimatorClass
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QRect


class MenuClass(QWidget):

    def __init__(self, parent):
        super(MenuClass, self).__init__(parent)

        self.bMenuOpen = False
        self.bMenuPinned = False

        self.animator = AnimatorClass(parent.session)

        self.__widget_setup(self)

        # TODO: Fixed Max and width but should adjust according to DPI settings
        # self.setMaximumWidth(150)
        # self.setMinimumWidth(10)

        # self.setToolTip("Menu panel")
        # self.setToolTipDuration(parent.TOOL_TIP_DURATION)

        self.setMouseTracking(True)

    ####################    EVENT SECTION    ####################
    def __widget_setup(self, parent):
        # Menu_main
        self.f_menu = FrameClass(parent,
                                 (0, 0, 0, 0),
                                 "QFrame {background-color: rgba(80, 120, 190, 90);}")
        self.btn_pin = ButtonClass(self.f_menu,
                                   (0, 0, 0, 0),
                                   None,
                                   "QPushButton {background-color: rgba(150,255,150,255);}")
        self.btn_pin.clicked.connect(self.btn_pin_event)

        # Menu_submenu
        self.wdt_menu = QWidget(self.f_menu)

        self.f_submenu = FrameClass(self.wdt_menu,
                                    (0, 0, 0, 0),
                                    "QFrame {background-color: rgba(150, 120, 130, 255);}")

    ####################    EVENT SECTION    ####################
    def btn_pin_event(self):
        self.bMenuPinned = not self.bMenuPinned

        if self.bMenuPinned:
            self.btn_pin.setText("X")
        else:
            self.btn_pin.setText("P")

    def resizeEvent(self, event):
        width, height = self.parent().size().toTuple()

        self.setMaximumSize(int(width * 0.1), height)
        self.setMinimumSize(0, self.maximumHeight())
        self.resize(width, height)

        self.f_menu.setMinimumSize(0, height)
        self.f_menu.setMaximumSize(self.maximumWidth(), self.maximumHeight())

        self.btn_pin.setGeometry(self.f_menu.maximumWidth() - 30, 5, 25, 25)

        # Menu_submenu
        self.wdt_menu.setGeometry(0, self.f_menu.maximumHeight()//7, self.f_menu.maximumWidth(), ((self.f_menu.maximumHeight()*6)//7)+1)
        self.f_submenu.setGeometry(0, 0, self.wdt_menu.width(), self.wdt_menu.height())

    def leaveEvent(self, event):
        if self.bMenuOpen and not self.bMenuPinned:
            self.close_menu()

    def enterEvent(self, event):
        if not self.bMenuOpen:
            self.open_menu()

    ####################    STATUS SECTION    ####################
    def set_menu_open_status(self, b_status: bool):
        self.bMenuOpen = b_status

    ####################    ANIMATION SECTION    ####################
    def open_menu(self):
        self.animator.animation_handler(self.f_menu, b"geometry",
                                        QRect(0, 0, 0, self.f_menu.height()),
                                        QRect(0, 0, self.width(), self.height()),
                                        duration=100)

        self.set_menu_open_status(True)

    def close_menu(self):
        self.animator.animation_handler(self.f_menu, b"geometry",
                                        QRect(0, 0, self.f_menu.width(), self.f_menu.height()),
                                        QRect(0, 0, 0, self.height()))

        self.set_menu_open_status(False)
