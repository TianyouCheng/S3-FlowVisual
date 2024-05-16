# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
# from qt_core import *

from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt

# STYLE
# ///////////////////////////////////////////////////////////////
# 用以给箭头按钮加圆角，需要箭头图片
# QComboBox:drop-down  {{	
#     subcontrol-origin: padding;
#     subcontrol-position: top right;

#     border-top-right-radius: {_radius}; 
#     border-bottom-right-radius: {_radius};
# }}


style = '''
QComboBox {{
	border: none;
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
}}
QComboBox QAbstractItemView{{
    background-color: {_bg_color};
    selection-background-color: {_bg_color_pressed};
    outline: 0;
}}
=
'''

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyComboBox(QComboBox):
    def __init__(
        self, 
        radius,
        color,
        bg_color,
        bg_color_hover,
        bg_color_pressed,
        parent = None,
    ):
        super().__init__()

        # SET PARAMETRES
        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)
        

        # SET STYLESHEET
        custom_style = style.format(
            _color = color,
            _radius = radius,
            _bg_color = bg_color,
            _bg_color_hover = bg_color_hover,
            _bg_color_pressed = bg_color_pressed
        )
        self.setStyleSheet(custom_style)
