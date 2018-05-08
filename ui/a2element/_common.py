"""
a2element._common

@created: Sep 3, 2016
@author: eRiC
"""
import time
import threading
from copy import deepcopy
from functools import partial

from PySide import QtGui, QtCore

import a2core
import a2util
from a2ctrl.base import Icons
from a2ctrl import get_cfg_value


class DrawCtrl(QtGui.QWidget):
    """
    Display widget to host everything that you want to show to the
    user for him to set up on your module.

    :param bool _init_ctrl: Set False when using multiple inheritance to keep it from calling super() again.
    """
    def __init__(self, main, cfg, mod, _init_ctrl=True):
        if _init_ctrl:
            super(DrawCtrl, self).__init__()
        self.a2 = a2core.A2Obj.inst()
        self.main = main
        self.cfg = cfg
        self.mod = mod
        self.check_delay = 250
        self._check_scheduled = False
        cfg_name = a2util.get_cfg_default_name(self.cfg)
        self.user_cfg = self.a2.db.get(cfg_name, self.mod.key)
        self.is_expandable_widget = False
        self._check_timer = QtCore.QTimer()
        self._check_timer.setInterval(self.check_delay)
        self._check_timer.timeout.connect(self._check)
        self._check_args = None

    def get_user_value(self, typ, name=None, default=None):
        """
        Get a user value. 'value'
        Name is 'value' by default so you can just get the default value by stating the type. Voila!
        """
        return get_cfg_value(self.cfg, self.user_cfg, name, typ, default)

    def set_user_value(self, this, name=None):
        """
        Set a user value in the module config.
        Name is None by by default so you can just set the default value by ... well:
        passing the value. Voila!
        """
        self.mod.set_user_cfg(self.cfg, this, name)

    def change(self, specific=None):
        """
        Triggers the module to save it's settings to the database and
        a2 include rewrite and restart if the module is enabled.
        """
        self.mod.change()
        if self.mod.enabled:
            self.main.settings_changed(specific)

    def delayed_check(self, *args):
        """
        Calls the check method with a little delay to prevent spamming reload.
        """
        self._check_args = args
        self._check_timer.start()

    def _check(self):
        if self._check_timer.isActive():
            self._check_timer.stop()
        self.check(*self._check_args)

    def check(self, *args):
        """
        For the element to gather data from the widgets and call change on demand.
        To be re-implemented when subclassing DrawCtrl.
        """
        pass


class EditCtrl(QtGui.QGroupBox):
    """
    frame widget for an edit control which enables basic arrangement of the
    control up & down as well as deleting the control.

    It's made to work with handwritten and compiled Uis right away.
    To embedd a compiled ui tell it so add_layout=False in the super()-statement:
        super(MyNewCtrl, self).__init__(add_layout=False)
    state the mainWidget in setupUi:
        self.ui.setupUi(self.mainWidget)
    and then set the self.mainWidget-layout to your top layout in the compiled ui:
        self.mainWidget.setLayout(self.ui.mytoplayout)

    TODO: currently this is embedded as menuitems on a button which is pretty shitty.
        I'd like to have some actual up/down buttons and an x to indicate delete
        functionality
    """
    def __init__(self, cfg, main, parent_cfg, add_layout=True):
        super(EditCtrl, self).__init__()
        self.a2 = a2core.A2Obj.inst()
        self.cfg = cfg
        self.main = main
        self.parent_cfg = parent_cfg
        self._setup_ui(add_layout)
        self.helpUrl = self.a2.urls.helpEditCtrl
        self.is_expandable_widget = False

    @staticmethod
    def element_name():
        return 'EditCtrl'

    @staticmethod
    def element_icon():
        return None

    def move(self, value, *args):
        if self.parent_cfg and self.parent_cfg[0].get('typ', '') == 'nfo':
            top_index = 1
        else:
            top_index = 0

        index = self.parent_cfg.index(self.cfg)
        maxIndex = len(self.parent_cfg) - 1
        if isinstance(value, bool):
            if value:
                newindex = top_index
                # self.main.ui.scrollArea.scrollToTop()
                # self.main.ui.scrollArea
            else:
                newindex = maxIndex
                # TODO: scrolling should be done in module_view
                # self.scroll_to_bottom()
        else:
            newindex = index + value
        # hop out if already at start or end
        if index == newindex or newindex < top_index or newindex > maxIndex:
            # print('returning from move! curr/new/max: %s/%s/%s' % (index, newindex, maxIndex))
            return

        # cfg = self.parent_cfg.pop(index)
        self.parent_cfg.pop(index)
        self.parent_cfg.insert(newindex, self.cfg)
        self.main.edit_mod(keep_scroll=True)

    def delete(self):
        if self.cfg in self.parent_cfg:
            self.parent_cfg.remove(self.cfg)
            self.main.edit_mod(keep_scroll=True)

    def duplicate(self):
        newCfg = deepcopy(self.cfg)
        self.parent_cfg.append(newCfg)
        self.main.edit_mod()
        self.scroll_to_bottom()

    def cut(self):
        self.main.edit_clipboard.append(deepcopy(self.cfg))
        self.delete()

    def help(self):
        a2util.surf_to(self.helpUrl)

    def _setup_ui(self, add_layout):
        self.setTitle(self.cfg['typ'])
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        self.setSizePolicy(sizePolicy)
        self._ctrlLayout = QtGui.QHBoxLayout(self)
        self._ctrlLayout.setSpacing(0)
        self._ctrlLayout.setContentsMargins(0, 0, 0, 0)
        self.mainWidget = QtGui.QWidget(self)
        if add_layout:
            self.mainLayout = QtGui.QVBoxLayout()
            self.mainLayout.setContentsMargins(5, 5, 5, 5)
            self.mainWidget.setLayout(self.mainLayout)
        self._ctrlLayout.addWidget(self.mainWidget)

        self._ctrlButtonLayout = QtGui.QVBoxLayout()
        self._ctrlButtonLayout.setSpacing(0)
        self._ctrlButtonLayout.setContentsMargins(5, 0, 5, 5)
        self._ctrlButtonLayout.setObjectName("ctrlButtonLayout")

        self._ctrlButton = QtGui.QPushButton(self)
        self._ctrlButton.setMinimumSize(QtCore.QSize(40, 40))
        self._ctrlButton.setMaximumSize(QtCore.QSize(40, 40))
        self._ctrlButton.setText("...")
        self._ctrlButton.setFlat(True)
        self._ctrlButton.setObjectName("ctrlButton")
        self._ctrlButtonLayout.addWidget(self._ctrlButton)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum,
                                       QtGui.QSizePolicy.Expanding)
        self._ctrlButtonLayout.addItem(spacerItem)
        self._ctrlLayout.addLayout(self._ctrlButtonLayout)
        self._ctrlLayout.setStretch(0, 1)

        self._ctrl_menu = QtGui.QMenu(self)
        self._ctrl_menu.aboutToShow.connect(self._build_menu)
        self._ctrlButton.setMenu(self._ctrl_menu)

    def _build_menu(self):
        """
        TODO: don't show top/to top, bottom/to bottom when already at top/bottom
        """
        self._ctrl_menu.clear()
        icons = Icons.inst()
        menu_items = [('Up', partial(self.move, -1), icons.up),
                      ('Down', partial(self.move, 1), icons.down),
                      ('To Top', partial(self.move, True), icons.up_align),
                      ('To Bottom', partial(self.move, False), icons.down_align),
                      ('Delete', self.delete, icons.delete),
                      ('Duplicate', self.duplicate, icons.copy),
                      ('Help on %s' % self.element_name(), self.help, icons.help)]

        clipboard_count = ''
        if self.main.edit_clipboard:
            clipboard_count = ' (%i)' % len(self.main.edit_clipboard)

        if self.cfg.get('typ') == 'group':
            menu_items.insert(-1, ('Paste' + clipboard_count, self.paste, icons.paste))
        else:
            menu_items.insert(-1, ('Cut' + clipboard_count, self.cut, icons.cut))

        for label, func, icon in menu_items:
            action = self._ctrl_menu.addAction(icon, label, func)
        self._ctrl_menu.insertSeparator(action)

    def check_new_name(self):
        """
        If no name set yet, like on new controls this creates a new unique
        name for the control from the module name + control type + incremental number
        """
        if 'name' not in self.cfg:
            # build the base control name
            new_name = '%s_%s' % (self.main.mod.name, self.element_name())
            # find biggest number
            this_type = self.cfg['typ']
            controls = [cfg.get('name', '') for cfg in self.main.temp_config
                        if cfg.get('typ') == this_type]

            new_name = a2util.get_next_free_number(new_name, controls)
            self.cfg['name'] = new_name

    def scroll_to_bottom(self):
        # self._scrollValB4 = self.main.ui.scrollBar.value()
        # self._scrollMaxB4 = self.main.ui.scrollBar.maximum()
        # print('scroll_to_bottom...')
        # QtCore.QTimer.singleShot(300, self._scroll_to_bottom)
        # threading.Thread(target=self._scroll_to_bottom).start()
        pass

    def _scroll_to_bottom(self, *args):
        # print('scrollValB4: %s' % self._scrollValB4)
        time.sleep(0.1)
        tmax = 0.3
        curve = QtCore.QEasingCurve(QtCore.QEasingCurve.OutQuad)
        res = 0.01
        steps = tmax / res
        tsteps = 1 / steps
        t = 0.0
        # this = self.main.ui.scrollBar.value()
        scrollEnd = self.main.ui.scrollBar.maximum()
        if not scrollEnd:
            scrollEnd = self._scrollMaxB4 + 100
        r = scrollEnd - self._scrollValB4
        self.main.ui.scrollBar.setValue(self._scrollValB4)
        while t <= 1.0:
            time.sleep(res)
            t += tsteps
            v = curve.valueForProgress(t)
            scrollval = self._scrollValB4 + (v * r)
            self.main.ui.scrollBar.setValue(scrollval)
