from PySide2.QtWidgets import QFrame


class FrameClass(QFrame):

    def __init__(self, parent, geometry, style):
        super(FrameClass, self).__init__(parent)

        x, y, w, h = geometry

        self.move(x, y)
        self.resize(w, h)
        self.setStyleSheet(style)
        self.show()