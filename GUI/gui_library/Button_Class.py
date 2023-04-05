from PySide2.QtWidgets import QPushButton


class ButtonClass(QPushButton):

    def __init__(self, parent, geometry, text, style):
        super(ButtonClass, self).__init__(parent)

        x, y, w, h = geometry

        self.move(x, y)
        self.resize(w, h)
        self.setStyleSheet(style)
        self.set_text(text)
        self.show()

    def set_text(self, text):
        if text is not None:
            self.setText(text)
