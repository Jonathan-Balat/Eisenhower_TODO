from GUI.gui_library.Frame_Class import FrameClass
from GUI.gui_library.Button_Class import ButtonClass
from GUI.gui_library.Animator_class import AnimatorClass
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QRect


class MenuClass(QWidget):

    def __init__(self, parent):
        super(MenuClass, self).__init__(parent)

        self.bMenuOpen = False
        self.b_menu_pinned = False

        self.animator = AnimatorClass(parent.session)

        self.f_menu = FrameClass(self,
                                 (0, 0, 0, 0),
                                 "QFrame {background-color: rgba(80, 120, 190, 255);}")

        self.btn_pin = ButtonClass(self.f_menu,
                                   (self.f_menu.width() - 50, 25, 25, 25),
                                   None,
                                   "QPushButton {background-color: rgba(150,150,150,255);}")
        self.btn_pin.clicked.connect(self.btn_pin_event)

        # TODO: Fixed Max and width but should adjust according to DPI settings
        # self.setMaximumWidth(150)
        # self.setMinimumWidth(10)

        # self.setToolTip("Menu panel")
        # self.setToolTipDuration(parent.TOOL_TIP_DURATION)

        self.setMouseTracking(True)

    def btn_pin_event(self):
        self.b_menu_pinned = not self.b_menu_pinned
        if self.b_menu_pinned:
            self.btn_pin.setText("X")
        else:
            self.btn_pin.setText("P")

    def resizeEvent(self, event):
        width, height = self.parent().size().toTuple()

        self.setMaximumSize(int(width*0.1), height)
        self.setMinimumSize(0, self.maximumHeight())
        self.resize(width, height)

        self.f_menu.setMinimumSize(0, height)
        self.f_menu.setMaximumSize(self.maximumWidth(), self.maximumHeight())

        self.btn_pin.setGeometry(self.f_menu.maximumWidth() - 50, 25, 25, 25)

    def leaveEvent(self, event):
        if self.bMenuOpen and not self.b_menu_pinned:
            self.close_menu()

    def enterEvent(self, event):
        if not self.bMenuOpen:
            self.open_menu()

    def set_menu_open_status(self, b_status: bool):
        self.bMenuOpen = b_status

    def open_menu(self):
        self.animator.animation_handler(self.f_menu, b"geometry",
                                 QRect(0, 0, 0, self.f_menu.height()),
                                 QRect(0, 0, self.width(), self.height()),
                                 duration=100)
        self.parent().session.processEvents()
        self.set_menu_open_status(True)

    def close_menu(self):
        self.animator.animation_handler(self.f_menu, b"geometry",
                                 QRect(0, 0, self.f_menu.width(), self.f_menu.height()),
                                 QRect(0, 0, 0, self.height()))

        self.set_menu_open_status(False)
