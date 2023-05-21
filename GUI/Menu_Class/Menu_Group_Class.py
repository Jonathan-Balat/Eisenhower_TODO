from GUI.gui_library.Frame_Class import FrameClass
from GUI.gui_library.Button_Class import ButtonClass
from GUI.gui_library.Animator_class import AnimatorClass
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QRect


""" TODO:
        - Create container for listing down menu options
        - Create generator for menu options 
        - Create animation selection for currently selected option
"""


class MenuGroupClass(QWidget):
    
    def __init__(self):
        super(MenuGroupClass, self).__init__()
        
    def generate_menu_list(self, parent):
        # Layout (Dynamically chosen?)

        # Button
        # Icon (optional)

        # Widget for selection
        ...