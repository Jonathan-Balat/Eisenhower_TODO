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

        self.__widget_setup()
        
        #
        # self.menu_option_generator = MenuGroupClass()
        self.__setup_submenu()

        # TODO: Fixed Max and width but should adjust according to DPI settings
        # self.setMaximumWidth(150)
        # self.setMinimumWidth(10)

        # self.setToolTip("Menu panel")
        # self.setToolTipDuration(parent.TOOL_TIP_DURATION)

        self.setMouseTracking(True)

    ####################    EVENT SECTION    ####################
    def __widget_setup(self):
        # Menu_main
        self.f_menu = FrameClass(self,
                                 (0, 0, 0, 0),
                                 "QFrame {background-color: rgba(80, 120, 190, 90);}")
        self.btn_pin = ButtonClass(self.f_menu,
                                   (0, 0, 0, 0),
                                   None,
                                   "QPushButton {background-color: rgba(150,255,150,255);}")
        self.btn_pin.clicked.connect(self.btn_pin_event)

        # Menu_submenu
        self.wdt_account = QWidget(self.f_menu)
        self.wdt_account.setMinimumHeight(100)
        self.wdt_account.setMaximumHeight(100)

        self.f_account = FrameClass(self.wdt_account,
                                    (0, 0, 0, 0),
                                    "QFrame {background-color: rgba(0, 190, 0, 255);}")

        # Menu_submenu
        self.wdt_menu = QWidget(self.f_menu)

        self.f_submenu = FrameClass(self.wdt_menu,
                                    (0, 0, 0, 0),
                                    "QFrame {background-color: rgba(0, 120, 0, 255);}")

        # Reorder widgets
        self.btn_pin.raise_()

    def __setup_submenu(self):

        self.btn_option = ButtonClass(self.wdt_menu,
                                   (0,0,0,0),
                                   None,
                                   "QPushButton {background-color: rgba(170,0,0,255);}")
        self.btn_option.clicked.connect(lambda: print("Menu 1"))

    ####################    EVENT SECTION    ####################
    def resizeEvent(self, event):
        width, height = self.parent().size().toTuple()

        self.setMaximumSize(int(width * 0.1), height)
        self.setMinimumSize(0, self.maximumHeight())
        self.resize(width, height)

        self.f_menu.setMinimumSize(0, height)
        self.f_menu.setMaximumSize(self.maximumWidth(), self.maximumHeight())

        self.btn_pin.setGeometry(self.maximumWidth() - 30, 5, 25, 25)

        # Menu_submenu
        self.wdt_account.setGeometry(0, 0, self.maximumWidth(), 0)
        self.f_account.setGeometry(0, 0, self.wdt_account.width(), self.wdt_account.height())

        self.wdt_menu.setGeometry(0, self.wdt_account.height(), self.maximumWidth(), self.maximumHeight() - self.wdt_account.height())
        self.f_submenu.setGeometry(0, 0, self.wdt_menu.width(), self.wdt_menu.height())
        self.btn_option.setGeometry(25, 25, self.wdt_menu.width() - 50, 50)

    def leaveEvent(self, event):
        if self.bMenuOpen and not self.bMenuPinned:
            self.close_menu()

    def enterEvent(self, event):
        if not self.bMenuOpen:
            self.open_menu()

    def btn_pin_event(self):
        self.bMenuPinned = not self.bMenuPinned

        if self.bMenuPinned:
            self.btn_pin.setText("X")
        else:
            self.btn_pin.setText("Pin")

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
