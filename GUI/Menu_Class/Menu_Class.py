from GUI.gui_library.Frame_Class import FrameClass
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QPropertyAnimation, QRect, QEasingCurve, Slot


class MenuClass(QWidget):

    def __init__(self, parent):
        super(MenuClass, self).__init__(parent)

        self.set_menu_open_status(False)

        self.f_menu = FrameClass(self,
                                 (0, 0, 0, 0),
                                 "QFrame {background-color: rgba(80, 120, 190,255);}")

        # Fixed Max and width but should adjust according to DPI settings
        # self.setMaximumWidth(150)
        # self.setMinimumWidth(10)

        # self.setToolTip("Menu panel")
        # self.setToolTipDuration(parent.TOOL_TIP_DURATION)

        self.setMouseTracking(True)

    def resizeEvent(self, event):
        width, height = self.parent().size().toTuple()

        self.setMaximumSize(int(width*0.1), height)
        self.setMinimumSize(0, self.maximumHeight())
        self.resize(width, height)

        self.f_menu.setMinimumSize(0, height)
        self.f_menu.setMaximumSize(self.maximumWidth(), self.maximumHeight())

    def leaveEvent(self, event):
        if self.bMenuOpen:
            self.close_menu()

    def enterEvent(self, event):
        if not self.bMenuOpen:
            self.open_menu()

    def set_menu_open_status(self, b_status: bool):
        self.bMenuOpen = b_status

    def open_menu(self):
        self.__animation_handler(self.f_menu, b"geometry",
                                 QRect(0, 0, 0, self.f_menu.height()),
                                 QRect(0, 0, self.width(), self.height()),
                                 duration=100)

        self.set_menu_open_status(True)

    def close_menu(self):
        self.__animation_handler(self.f_menu, b"geometry",
                                 QRect(0, 0, self.f_menu.width(), self.f_menu.height()),
                                 QRect(0, 0, 0, self.height()))

        self.set_menu_open_status(False)

    def __animation_handler(self, target, property, start_value, end_value,
                            curve_type=QEasingCurve.BezierSpline, duration=250):
        self.animator = QPropertyAnimation(target, property, self)

        self.animator.setDuration(duration)
        self.animator.setStartValue(start_value)
        self.animator.setEndValue(end_value)
        self.animator.setEasingCurve(curve_type)
        self.animator.start()
