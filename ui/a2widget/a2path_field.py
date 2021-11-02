"""
A universal file/folder path field with a browse button.
the field can be made writable or read-only to allow only browsed paths
it can be made browsing for folders or files

At files it can be set to save-mode where inexistent paths can be selected
and filtered file types can be set. See:
https://doc.qt.io/qtforpython/PySide6/QtWidgets/QFileDialog.html?highlight=qfiledialog#detailed-description

TODO: add recent paths?
"""
import os
from a2qt import QtCore, QtWidgets

import a2ctrl
import a2util
from a2widget.a2more_button import A2MoreButton

MSG_ERROR_CHANGABLE = 'PathField cannot be set writable while not being changable at the same time!'


class BrowseType(object):
    folder = 0
    file = 1


class A2PathField(QtWidgets.QWidget):
    changed = QtCore.Signal(str)

    def __init__(
        self,
        parent,
        value='',
        file_types='',
        writable=True,
        label_text=None,
        save_mode=False,
        changable=True,
    ):
        super(A2PathField, self).__init__(parent)
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.line_field = QtWidgets.QLineEdit(self)
        self.line_field.setText(value)
        self.line_field.textChanged.connect(self._on_text_changed)
        self.main_layout.addWidget(self.line_field)
        self.browse_button = QtWidgets.QPushButton('Browse...', self)
        self.browse_button.setIcon(a2ctrl.Icons.folder2)
        self.browse_button.clicked.connect(self.browse)
        self.main_layout.addWidget(self.browse_button)

        self.options_menu = QtWidgets.QMenu()
        self.a2option_button = A2MoreButton(self)
        self.a2option_button.menu_called.connect(self.show_options_menu)
        self.main_layout.addWidget(self.a2option_button)

        self._set_delay = 500

        self._value = value
        self.file_types = file_types
        self.save_mode = save_mode
        self.browse_type = BrowseType.file
        self.label_text = label_text

        self._changable = None
        self.changable = changable
        self._writable = None
        self.writable = writable

        self._timer = QtCore.QTimer()
        self._timer.setInterval(self._set_delay)
        self._timer.timeout.connect(self._send_changed)

    @property
    def writable(self):
        return self._writable

    @writable.setter
    def writable(self, state):
        if state == self._writable:
            return

        if state and not self.changable:
            raise RuntimeError(MSG_ERROR_CHANGABLE)

        self._writable = state
        self.line_field.setReadOnly(not state)

    @property
    def changable(self):
        return self._changable

    @changable.setter
    def changable(self, state):
        if state == self._changable:
            return

        if not state and self.writable:
            self.writable = False
        self._changable = state
        self.browse_button.setVisible(state)

    def browse(self):
        if self.browse_type == BrowseType.file:
            file_types = 'All Files (*)' if not self.file_types else self.file_types
            if self.save_mode:
                file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
                    self, self.label_text, self._value, file_types
                )
            else:
                file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                    self, self.label_text, self._value, file_types
                )
        else:
            file_path = QtWidgets.QFileDialog.getExistingDirectory(
                self, caption=self.label_text, dir=self._value
            )

        if file_path:
            self.value = file_path

    def _on_text_changed(self, text):
        self._timer.start()

    def _send_changed(self):
        if self._timer.isActive():
            self._timer.stop()
        new_value = self.line_field.text()
        if new_value == self._value:
            return
        self._value = new_value
        self.changed.emit(self._value)

    def setText(self, this):
        """Just to be compatible with QDesigner setting text already"""
        self.value = this

    def setEnabled(self, state):
        """
        Used to make the field changable/static.
        :param bool state: True: Field value can be changed via browsing OR typing if enabled.
            False: Field is for display only. Copying/exploring to path is still possible
        """
        self.changable = state

    def setReadOnly(self, state):
        """
        Used to enable writing in the field. Can still be changed via browsing if 'changable'!
        :param bool state: True: you can type in the field/ False: typing disabled.
        """
        self.writable = not state

    def setPlaceholderText(self, text):
        self.line_field.setPlaceholderText(text)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, this):
        self._value = os.path.normpath(this)
        self.line_field.setText(self._value)
        self.changed.emit(self._value)

    def show_options_menu(self, menu):
        menu.addAction(a2ctrl.Icons.copy, 'Copy Path', self.copy_path)
        menu.addAction(a2ctrl.Icons.folder, 'Explore Path', self.explore_path)

    def explore_path(self):
        a2util.explore(self.value)

    def copy_path(self):
        QtWidgets.QApplication.clipboard().setText(self.value)


if __name__ == '__main__':
    from a2widget.demo import path_field_demo

    path_field_demo.show()
