# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\eric\io\code\a2\ui\a2widget\keyboard\base.ui'
#
# Created: Thu Oct 26 09:37:09 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Keyboard(object):
    def setupUi(self, Keyboard):
        Keyboard.setObjectName("Keyboard")
        Keyboard.resize(3708, 706)
        self.verticalLayout = QtGui.QVBoxLayout(Keyboard)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.key_field = QtGui.QLineEdit(Keyboard)
        self.key_field.setObjectName("key_field")
        self.horizontalLayout_2.addWidget(self.key_field)
        self.label_2 = QtGui.QLabel(Keyboard)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.check_numpad = QtGui.QCheckBox(Keyboard)
        self.check_numpad.setObjectName("check_numpad")
        self.horizontalLayout_2.addWidget(self.check_numpad)
        self.check_mouse = QtGui.QCheckBox(Keyboard)
        self.check_mouse.setObjectName("check_mouse")
        self.horizontalLayout_2.addWidget(self.check_mouse)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.keys_widget = QtGui.QWidget(Keyboard)
        self.keys_widget.setObjectName("keys_widget")
        self.keys_layout = QtGui.QHBoxLayout(self.keys_widget)
        self.keys_layout.setContentsMargins(0, 0, 0, 0)
        self.keys_layout.setContentsMargins(0, 0, 0, 0)
        self.keys_layout.setObjectName("keys_layout")
        self.main_block = QtGui.QVBoxLayout()
        self.main_block.setContentsMargins(-1, -1, 30, -1)
        self.main_block.setObjectName("main_block")
        self.f_row = QtGui.QHBoxLayout()
        self.f_row.setObjectName("f_row")
        self.escape = QtGui.QPushButton(self.keys_widget)
        self.escape.setObjectName("escape")
        self.f_row.addWidget(self.escape)
        self.main_block.addLayout(self.f_row)
        self.f_spacer = QtGui.QWidget(self.keys_widget)
        self.f_spacer.setObjectName("f_spacer")
        self.main_block.addWidget(self.f_spacer)
        self.enter_key_rows = QtGui.QHBoxLayout()
        self.enter_key_rows.setObjectName("enter_key_rows")
        self.top_letter_rows = QtGui.QVBoxLayout()
        self.top_letter_rows.setObjectName("top_letter_rows")
        self.number_row = QtGui.QHBoxLayout()
        self.number_row.setObjectName("number_row")
        self.backspace = QtGui.QPushButton(self.keys_widget)
        self.backspace.setObjectName("backspace")
        self.number_row.addWidget(self.backspace)
        self.top_letter_rows.addLayout(self.number_row)
        self.letter_row_top = QtGui.QHBoxLayout()
        self.letter_row_top.setObjectName("letter_row_top")
        self.tab = QtGui.QPushButton(self.keys_widget)
        self.tab.setObjectName("tab")
        self.letter_row_top.addWidget(self.tab)
        self.top_letter_rows.addLayout(self.letter_row_top)
        self.enter_key_rows.addLayout(self.top_letter_rows)
        self.main_block.addLayout(self.enter_key_rows)
        self.letter_row_middle = QtGui.QHBoxLayout()
        self.letter_row_middle.setObjectName("letter_row_middle")
        self.capslock = QtGui.QPushButton(self.keys_widget)
        self.capslock.setObjectName("capslock")
        self.letter_row_middle.addWidget(self.capslock)
        self.main_block.addLayout(self.letter_row_middle)
        self.letter_row_bottom = QtGui.QHBoxLayout()
        self.letter_row_bottom.setObjectName("letter_row_bottom")
        self.l_shift_key = QtGui.QPushButton(self.keys_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.l_shift_key.setFont(font)
        self.l_shift_key.setObjectName("l_shift_key")
        self.letter_row_bottom.addWidget(self.l_shift_key)
        self.r_shift_key = QtGui.QPushButton(self.keys_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.r_shift_key.setFont(font)
        self.r_shift_key.setObjectName("r_shift_key")
        self.letter_row_bottom.addWidget(self.r_shift_key)
        self.main_block.addLayout(self.letter_row_bottom)
        self.bottom_row = QtGui.QHBoxLayout()
        self.bottom_row.setObjectName("bottom_row")
        self.l_ctrl_key = QtGui.QPushButton(self.keys_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.l_ctrl_key.setFont(font)
        self.l_ctrl_key.setObjectName("l_ctrl_key")
        self.bottom_row.addWidget(self.l_ctrl_key)
        self.l_win_key = QtGui.QPushButton(self.keys_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.l_win_key.setFont(font)
        self.l_win_key.setObjectName("l_win_key")
        self.bottom_row.addWidget(self.l_win_key)
        self.l_alt_key = QtGui.QPushButton(self.keys_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.l_alt_key.setFont(font)
        self.l_alt_key.setObjectName("l_alt_key")
        self.bottom_row.addWidget(self.l_alt_key)
        self.space = QtGui.QPushButton(self.keys_widget)
        self.space.setCheckable(True)
        self.space.setObjectName("space")
        self.bottom_row.addWidget(self.space)
        self.r_alt_key = QtGui.QPushButton(self.keys_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.r_alt_key.setFont(font)
        self.r_alt_key.setObjectName("r_alt_key")
        self.bottom_row.addWidget(self.r_alt_key)
        self.r_win_key = QtGui.QPushButton(self.keys_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.r_win_key.setFont(font)
        self.r_win_key.setObjectName("r_win_key")
        self.bottom_row.addWidget(self.r_win_key)
        self.appskey = QtGui.QPushButton(self.keys_widget)
        self.appskey.setObjectName("appskey")
        self.bottom_row.addWidget(self.appskey)
        self.r_ctrl_key = QtGui.QPushButton(self.keys_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.r_ctrl_key.setFont(font)
        self.r_ctrl_key.setObjectName("r_ctrl_key")
        self.bottom_row.addWidget(self.r_ctrl_key)
        self.bottom_row.setStretch(3, 1)
        self.main_block.addLayout(self.bottom_row)
        self.keys_layout.addLayout(self.main_block)
        self.cursor_block = QtGui.QVBoxLayout()
        self.cursor_block.setContentsMargins(-1, -1, 30, -1)
        self.cursor_block.setObjectName("cursor_block")
        self.print_block = QtGui.QHBoxLayout()
        self.print_block.setObjectName("print_block")
        self.printscreen = QtGui.QPushButton(self.keys_widget)
        self.printscreen.setObjectName("printscreen")
        self.print_block.addWidget(self.printscreen)
        self.scroll_key = QtGui.QPushButton(self.keys_widget)
        self.scroll_key.setObjectName("scroll_key")
        self.print_block.addWidget(self.scroll_key)
        self.pause = QtGui.QPushButton(self.keys_widget)
        self.pause.setObjectName("pause")
        self.print_block.addWidget(self.pause)
        self.print_spacer = QtGui.QWidget(self.keys_widget)
        self.print_spacer.setObjectName("print_spacer")
        self.print_block.addWidget(self.print_spacer)
        self.cursor_block.addLayout(self.print_block)
        self.cursor_spacer = QtGui.QWidget(self.keys_widget)
        self.cursor_spacer.setObjectName("cursor_spacer")
        self.cursor_block.addWidget(self.cursor_spacer)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.up = QtGui.QPushButton(self.keys_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.up.setFont(font)
        self.up.setObjectName("up")
        self.gridLayout.addWidget(self.up, 3, 1, 1, 1)
        self.left = QtGui.QPushButton(self.keys_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.left.setFont(font)
        self.left.setObjectName("left")
        self.gridLayout.addWidget(self.left, 4, 0, 1, 1)
        self.insert = QtGui.QPushButton(self.keys_widget)
        self.insert.setObjectName("insert")
        self.gridLayout.addWidget(self.insert, 0, 0, 1, 1)
        self.home = QtGui.QPushButton(self.keys_widget)
        self.home.setObjectName("home")
        self.gridLayout.addWidget(self.home, 0, 1, 1, 1)
        self.pgup = QtGui.QPushButton(self.keys_widget)
        self.pgup.setObjectName("pgup")
        self.gridLayout.addWidget(self.pgup, 0, 2, 1, 1)
        self.delete = QtGui.QPushButton(self.keys_widget)
        self.delete.setObjectName("del")
        self.gridLayout.addWidget(self.delete, 1, 0, 1, 1)
        self.end = QtGui.QPushButton(self.keys_widget)
        self.end.setObjectName("end")
        self.gridLayout.addWidget(self.end, 1, 1, 1, 1)
        self.pgdn = QtGui.QPushButton(self.keys_widget)
        self.pgdn.setObjectName("pgdn")
        self.gridLayout.addWidget(self.pgdn, 1, 2, 1, 1)
        self.right = QtGui.QPushButton(self.keys_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.right.setFont(font)
        self.right.setObjectName("right")
        self.gridLayout.addWidget(self.right, 4, 2, 1, 1)
        self.down = QtGui.QPushButton(self.keys_widget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.down.setFont(font)
        self.down.setObjectName("down")
        self.gridLayout.addWidget(self.down, 4, 1, 1, 1)
        self.label = QtGui.QLabel(self.keys_widget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.cursor_block.addLayout(self.gridLayout)
        self.keys_layout.addLayout(self.cursor_block)
        self.num_block_widget = QtGui.QWidget(self.keys_widget)
        self.num_block_widget.setObjectName("num_block_widget")
        self.gridLayout_3 = QtGui.QGridLayout(self.num_block_widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.num_spacer = QtGui.QWidget(self.num_block_widget)
        self.num_spacer.setObjectName("num_spacer")
        self.gridLayout_3.addWidget(self.num_spacer, 0, 0, 1, 4)
        self.numlock = QtGui.QPushButton(self.num_block_widget)
        self.numlock.setObjectName("numlock")
        self.gridLayout_3.addWidget(self.numlock, 1, 0, 1, 1)
        self.numpaddiv = QtGui.QPushButton(self.num_block_widget)
        self.numpaddiv.setObjectName("numpaddiv")
        self.gridLayout_3.addWidget(self.numpaddiv, 1, 1, 1, 1)
        self.numpadmult = QtGui.QPushButton(self.num_block_widget)
        self.numpadmult.setObjectName("numpadmult")
        self.gridLayout_3.addWidget(self.numpadmult, 1, 2, 1, 1)
        self.numpadsub = QtGui.QPushButton(self.num_block_widget)
        self.numpadsub.setObjectName("numpadsub")
        self.gridLayout_3.addWidget(self.numpadsub, 1, 3, 1, 1)
        self.numpad7 = QtGui.QPushButton(self.num_block_widget)
        self.numpad7.setObjectName("numpad7")
        self.gridLayout_3.addWidget(self.numpad7, 2, 0, 1, 1)
        self.numpad8 = QtGui.QPushButton(self.num_block_widget)
        self.numpad8.setObjectName("numpad8")
        self.gridLayout_3.addWidget(self.numpad8, 2, 1, 1, 1)
        self.numpad9 = QtGui.QPushButton(self.num_block_widget)
        self.numpad9.setObjectName("numpad9")
        self.gridLayout_3.addWidget(self.numpad9, 2, 2, 1, 1)
        self.numpadadd = QtGui.QPushButton(self.num_block_widget)
        self.numpadadd.setObjectName("numpadadd")
        self.gridLayout_3.addWidget(self.numpadadd, 2, 3, 2, 1)
        self.numpad4 = QtGui.QPushButton(self.num_block_widget)
        self.numpad4.setObjectName("numpad4")
        self.gridLayout_3.addWidget(self.numpad4, 3, 0, 1, 1)
        self.numpad5 = QtGui.QPushButton(self.num_block_widget)
        self.numpad5.setObjectName("numpad5")
        self.gridLayout_3.addWidget(self.numpad5, 3, 1, 1, 1)
        self.numpad6 = QtGui.QPushButton(self.num_block_widget)
        self.numpad6.setObjectName("numpad6")
        self.gridLayout_3.addWidget(self.numpad6, 3, 2, 1, 1)
        self.numpad1 = QtGui.QPushButton(self.num_block_widget)
        self.numpad1.setObjectName("numpad1")
        self.gridLayout_3.addWidget(self.numpad1, 4, 0, 1, 1)
        self.numpad2 = QtGui.QPushButton(self.num_block_widget)
        self.numpad2.setObjectName("numpad2")
        self.gridLayout_3.addWidget(self.numpad2, 4, 1, 1, 1)
        self.numpad3 = QtGui.QPushButton(self.num_block_widget)
        self.numpad3.setObjectName("numpad3")
        self.gridLayout_3.addWidget(self.numpad3, 4, 2, 1, 1)
        self.numpadenter = QtGui.QPushButton(self.num_block_widget)
        self.numpadenter.setObjectName("numpadenter")
        self.gridLayout_3.addWidget(self.numpadenter, 4, 3, 2, 1)
        self.numpad0 = QtGui.QPushButton(self.num_block_widget)
        self.numpad0.setObjectName("numpad0")
        self.gridLayout_3.addWidget(self.numpad0, 5, 0, 1, 2)
        self.numpaddot = QtGui.QPushButton(self.num_block_widget)
        self.numpaddot.setObjectName("numpaddot")
        self.gridLayout_3.addWidget(self.numpaddot, 5, 2, 1, 1)
        self.keys_layout.addWidget(self.num_block_widget)
        self.mouse_block_widget = QtGui.QWidget(self.keys_widget)
        self.mouse_block_widget.setObjectName("mouse_block_widget")
        self.gridLayout_2 = QtGui.QGridLayout(self.mouse_block_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.wheelup = QtGui.QPushButton(self.mouse_block_widget)
        self.wheelup.setText("")
        self.wheelup.setObjectName("wheelup")
        self.gridLayout_2.addWidget(self.wheelup, 0, 2, 1, 1)
        self.lbutton = QtGui.QPushButton(self.mouse_block_widget)
        self.lbutton.setText("")
        self.lbutton.setObjectName("lbutton")
        self.gridLayout_2.addWidget(self.lbutton, 1, 0, 1, 1)
        self.wheelleft = QtGui.QPushButton(self.mouse_block_widget)
        self.wheelleft.setText("")
        self.wheelleft.setObjectName("wheelleft")
        self.gridLayout_2.addWidget(self.wheelleft, 1, 1, 1, 1)
        self.mbutton = QtGui.QPushButton(self.mouse_block_widget)
        self.mbutton.setText("")
        self.mbutton.setObjectName("mbutton")
        self.gridLayout_2.addWidget(self.mbutton, 1, 2, 1, 1)
        self.wheelright = QtGui.QPushButton(self.mouse_block_widget)
        self.wheelright.setText("")
        self.wheelright.setObjectName("wheelright")
        self.gridLayout_2.addWidget(self.wheelright, 1, 3, 1, 1)
        self.rbutton = QtGui.QPushButton(self.mouse_block_widget)
        self.rbutton.setText("")
        self.rbutton.setObjectName("rbutton")
        self.gridLayout_2.addWidget(self.rbutton, 1, 4, 1, 1)
        self.wheeldown = QtGui.QPushButton(self.mouse_block_widget)
        self.wheeldown.setText("")
        self.wheeldown.setObjectName("wheeldown")
        self.gridLayout_2.addWidget(self.wheeldown, 2, 2, 1, 1)
        self._mouse_body = QtGui.QPushButton(self.mouse_block_widget)
        self._mouse_body.setEnabled(False)
        self._mouse_body.setText("")
        self._mouse_body.setObjectName("_mouse_body")
        self.gridLayout_2.addWidget(self._mouse_body, 3, 0, 1, 5)
        self.keys_layout.addWidget(self.mouse_block_widget)
        self.verticalLayout.addWidget(self.keys_widget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.a2ok_button = QtGui.QPushButton(Keyboard)
        self.a2ok_button.setObjectName("a2ok_button")
        self.horizontalLayout.addWidget(self.a2ok_button)
        self.a2cancel_button = QtGui.QPushButton(Keyboard)
        self.a2cancel_button.setFlat(True)
        self.a2cancel_button.setObjectName("a2cancel_button")
        self.horizontalLayout.addWidget(self.a2cancel_button)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Keyboard)
        QtCore.QMetaObject.connectSlotsByName(Keyboard)

    def retranslateUi(self, Keyboard):
        Keyboard.setWindowTitle(QtGui.QApplication.translate("Keyboard", "Hotkey Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Keyboard", "Show:", None, QtGui.QApplication.UnicodeUTF8))
        self.check_numpad.setText(QtGui.QApplication.translate("Keyboard", "Num Pad", None, QtGui.QApplication.UnicodeUTF8))
        self.check_mouse.setText(QtGui.QApplication.translate("Keyboard", "Mouse", None, QtGui.QApplication.UnicodeUTF8))
        self.escape.setText(QtGui.QApplication.translate("Keyboard", "Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.backspace.setText(QtGui.QApplication.translate("Keyboard", "Backspace", None, QtGui.QApplication.UnicodeUTF8))
        self.tab.setText(QtGui.QApplication.translate("Keyboard", "Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.capslock.setText(QtGui.QApplication.translate("Keyboard", "Caps Lock", None, QtGui.QApplication.UnicodeUTF8))
        self.l_shift_key.setText(QtGui.QApplication.translate("Keyboard", "Shift", None, QtGui.QApplication.UnicodeUTF8))
        self.r_shift_key.setText(QtGui.QApplication.translate("Keyboard", "Shift", None, QtGui.QApplication.UnicodeUTF8))
        self.l_ctrl_key.setText(QtGui.QApplication.translate("Keyboard", "Ctrl", None, QtGui.QApplication.UnicodeUTF8))
        self.l_win_key.setText(QtGui.QApplication.translate("Keyboard", "Win", None, QtGui.QApplication.UnicodeUTF8))
        self.l_alt_key.setText(QtGui.QApplication.translate("Keyboard", "Alt", None, QtGui.QApplication.UnicodeUTF8))
        self.space.setText(QtGui.QApplication.translate("Keyboard", "Space", None, QtGui.QApplication.UnicodeUTF8))
        self.r_alt_key.setText(QtGui.QApplication.translate("Keyboard", "Alt", None, QtGui.QApplication.UnicodeUTF8))
        self.r_win_key.setText(QtGui.QApplication.translate("Keyboard", "Win", None, QtGui.QApplication.UnicodeUTF8))
        self.appskey.setText(QtGui.QApplication.translate("Keyboard", "AppsKey", None, QtGui.QApplication.UnicodeUTF8))
        self.r_ctrl_key.setText(QtGui.QApplication.translate("Keyboard", "Ctrl", None, QtGui.QApplication.UnicodeUTF8))
        self.printscreen.setText(QtGui.QApplication.translate("Keyboard", "Print\n"
"Screen", None, QtGui.QApplication.UnicodeUTF8))
        self.scroll_key.setText(QtGui.QApplication.translate("Keyboard", "Scroll\n"
"Lock", None, QtGui.QApplication.UnicodeUTF8))
        self.pause.setText(QtGui.QApplication.translate("Keyboard", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.up.setText(QtGui.QApplication.translate("Keyboard", "u", None, QtGui.QApplication.UnicodeUTF8))
        self.left.setText(QtGui.QApplication.translate("Keyboard", "l", None, QtGui.QApplication.UnicodeUTF8))
        self.insert.setText(QtGui.QApplication.translate("Keyboard", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.home.setText(QtGui.QApplication.translate("Keyboard", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.pgup.setText(QtGui.QApplication.translate("Keyboard", "Page\n"
"Up", None, QtGui.QApplication.UnicodeUTF8))
        self.delete.setText(QtGui.QApplication.translate("Keyboard", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.end.setText(QtGui.QApplication.translate("Keyboard", "End", None, QtGui.QApplication.UnicodeUTF8))
        self.pgdn.setText(QtGui.QApplication.translate("Keyboard", "Page\n"
"Down", None, QtGui.QApplication.UnicodeUTF8))
        self.right.setText(QtGui.QApplication.translate("Keyboard", "r", None, QtGui.QApplication.UnicodeUTF8))
        self.down.setText(QtGui.QApplication.translate("Keyboard", "d", None, QtGui.QApplication.UnicodeUTF8))
        self.numlock.setText(QtGui.QApplication.translate("Keyboard", "Num\n"
"Lock", None, QtGui.QApplication.UnicodeUTF8))
        self.numpaddiv.setText(QtGui.QApplication.translate("Keyboard", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.numpadmult.setText(QtGui.QApplication.translate("Keyboard", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.numpadsub.setText(QtGui.QApplication.translate("Keyboard", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad7.setText(QtGui.QApplication.translate("Keyboard", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad8.setText(QtGui.QApplication.translate("Keyboard", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad9.setText(QtGui.QApplication.translate("Keyboard", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.numpadadd.setText(QtGui.QApplication.translate("Keyboard", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad4.setText(QtGui.QApplication.translate("Keyboard", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad5.setText(QtGui.QApplication.translate("Keyboard", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad6.setText(QtGui.QApplication.translate("Keyboard", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad1.setText(QtGui.QApplication.translate("Keyboard", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad2.setText(QtGui.QApplication.translate("Keyboard", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad3.setText(QtGui.QApplication.translate("Keyboard", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.numpadenter.setText(QtGui.QApplication.translate("Keyboard", "Enter", None, QtGui.QApplication.UnicodeUTF8))
        self.numpad0.setText(QtGui.QApplication.translate("Keyboard", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.numpaddot.setText(QtGui.QApplication.translate("Keyboard", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.a2ok_button.setText(QtGui.QApplication.translate("Keyboard", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.a2cancel_button.setText(QtGui.QApplication.translate("Keyboard", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

