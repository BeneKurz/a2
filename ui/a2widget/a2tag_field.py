from functools import partial

from PySide import QtCore, QtGui

import a2ctrl
from a2widget.flowlayout import FlowLayout


class A2TagField(QtGui.QWidget):
    changed = QtCore.Signal(list)

    def __init__(self, parent=None):
        super(A2TagField, self).__init__(parent=parent)
        self.main_layout = FlowLayout(self)

        self.plus_button = QtGui.QToolButton()
        self.plus_menu = QtGui.QMenu(self)
        self.plus_button.setIcon(a2ctrl.Icons().label_plus)
        self.plus_button.clicked.connect(self.build_plus_menu)
        self.main_layout.addWidget(self.plus_button)

        self._tags = []
        self._tags_backup = []
        self._tag_widgets = []
        self._available_tags = []

    def build_plus_menu(self):
        self.plus_menu.clear()
        action = QtGui.QAction(a2ctrl.Icons().label_plus, 'New Tag', self, triggered=self.create_tag)
        self.plus_menu.addAction(action)
        if self._available_tags:
            self.plus_menu.addSeparator()
            for tag in self._available_tags:
                if tag in self._tags:
                    continue
                action = QtGui.QAction(a2ctrl.Icons().label, tag, self,
                                       triggered=partial(self.add, tag))
                self.plus_menu.addAction(action)

        self.plus_menu.popup(self.cursor().pos())

    def create_tag(self):
        print('create_tag...')

    def set_tags(self, these):
        """
        Replaces the saved tags with given ones.

        :param these: Tags to put.
        """
        if isinstance(these, str):
            these = [these]
        elif not isinstance(these, (tuple, list, set)):
            raise RuntimeError('Tag Field needs an iterable as tags')

        self.clear()
        self.add(these)

    def clear(self):
        for widget in self._tag_widgets:
            widget.deleteLater()
        self._tags = []
        self._check_changed()

    @property
    def value(self):
        return self._tags

    @value.setter
    def value(self, these):
        self.set_tags(these)

    def delete(self, tag_name):
        if tag_name not in self._tags:
            return

        i = self._tags.index(tag_name)
        widget = self._tag_widgets.pop(i)
        widget.deleteLater()
        self._tags.remove(tag_name)
        self._check_changed()

    def add(self, tag_name, _emit_change=True):
        if tag_name in self._tags:
            return

        if isinstance(tag_name, (tuple, list, set)):
            for name in tag_name:
                self.add(name, _emit_change=False)
            return
        elif isinstance(tag_name, str):
            self._tags.append(tag_name)
            if tag_name not in self._available_tags:
                self._available_tags.append(tag_name)

            widget = A2Tag(self, tag_name)
            widget.delete_requested.connect(self.delete)
            self._tag_widgets.append(widget)
            self.main_layout.addWidget(widget)

        self._check_changed()

    def _check_changed(self):
        sorted_tags = sorted(self._tags)
        print('sorted_tags: %s' % sorted_tags)
        print('self._tags_backup: %s' % self._tags_backup)
        if sorted_tags != self._tags_backup:
            self._tags_backup = sorted_tags
            self.changed.emit(self._tags)

    @property
    def available_tags(self):
        return self._available_tags

    @available_tags.setter
    def available_tags(self, these):
        if isinstance(these, str):
            self._available_tags = [these]
        elif isinstance(these, (tuple, list)):
            # make sure to make these unique
            these = set(these)
            self._available_tags = list(these)
        elif not isinstance(these, set):
            raise AttributeError('Available tags need to be set with types str, list, tuple or set!')
        else:
            self._available_tags = list(these)


class A2Tag(QtGui.QPushButton):
    delete_requested = QtCore.Signal(str)

    def __init__(self, parent, name):
        super(A2Tag, self).__init__(parent)
        self.name = name
        self.setIcon(a2ctrl.Icons().label)
        self.setText(self.name)
        self.button_menu = None
        self.clicked.connect(self.build_menu)

    def build_menu(self):
        if self.button_menu is None:
            self.button_menu = QtGui.QMenu()
            action = QtGui.QAction(a2ctrl.Icons().delete, 'Delete "%s"' % self.name, self.button_menu,
                                   triggered=self.delete)
            self.button_menu.addAction(action)
        self.button_menu.popup(self.cursor().pos())

    def delete(self):
        self.delete_requested.emit(self.name)


if __name__ == '__main__':
    import a2widget.demo.a2tag_field
    a2widget.demo.a2tag_field.show()
