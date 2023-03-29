from GUI.gui_library.Frame_Class import FrameClass
from PySide2.QtWidgets import QWidget


class MenuClass(QWidget):

    def __init__(self, parent):
        super(MenuClass, self).__init__(parent)

        self.f_menu = FrameClass(self,
                                 (0, 0, self.width(), self.height()),
                                 "QFrame {background-color: rgba(80, 120, 190,255);}")

        # Fixed Max and width but should adjust according to DPI settings
        self.setMaximumWidth(150)
        self.setMinimumWidth(10)
        self.setToolTip("Menu panel")
        self.setToolTipDuration(parent.TOOL_TIP_DURATION)

    def resizeEvent(self, event):
        self.f_menu.resize(self.width(), self.height())