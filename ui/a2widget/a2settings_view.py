"""
Objects for the the a2 settings tabs.
"""
import os
import sys

from a2qt import QtGui, QtCore, QtWidgets

import a2ahk
import a2core
import a2util
import a2ctrl.connect
import a2path
from a2widget import a2module_source, a2hotkey

log = a2core.get_logger(__name__)


class A2Settings(QtWidgets.QWidget):
    def __init__(self, main):
        super(A2Settings, self).__init__(parent=main)
        self.a2 = a2core.A2Obj.inst()
        self.main = main
        self._setup_ui()
        self._source_widgets = {}
        self._draw_module_sources()
        self.is_expandable_widget = True

    def _draw_module_sources(self):
        enabled_list = [name for name, data in self.a2.enabled.items() if data[0]]
        self.ui.no_sources_msg.setVisible(self.a2.module_sources == {})
        for module_source in sorted(self.a2.module_sources.values(), key=lambda x: x.name):
            widget = a2module_source.ModSourceWidget(
                self.main, module_source, show_enabled=module_source.name in enabled_list
            )
            widget.toggled.connect(self.main.load_runtime_and_ui)
            widget.changed.connect(self.main.load_runtime_and_ui)
            self.ui.mod_source_layout.addWidget(widget)
            self._source_widgets[module_source] = widget

    def _setup_ui(self):
        from a2widget import a2settings_view_ui

        a2ctrl.check_ui_module(a2settings_view_ui)
        self.ui = a2settings_view_ui.Ui_a2settings()
        self.ui.setupUi(self)

        a2ui_hotkey = self.a2.db.get('a2_hotkey') or a2core.A2DEFAULT_HOTKEY
        self.ui.a2hotkey.set_config({'key': a2ui_hotkey})
        self.ui.a2hotkey.hotkey_changed.connect(self.set_a2_hotkey)

        self.ui.remember_selection.setChecked(self.a2.db.get('remember_last') or False)
        self.ui.remember_selection.clicked[bool].connect(self.remember_last_toggle)

        self.add_source_menu = QtWidgets.QMenu(self)
        self.ui.a2add_button.clicked.connect(self.build_add_source_menu)
        self.ui.a2add_button.setIcon(a2ctrl.Icons.inst().list_add)

        self.ui.db_print_all_button.clicked.connect(self.get_db_digest)

        self.ui.a2settings_tab.setCurrentIndex(0)
        self.ui.a2settings_tab.currentChanged.connect(self.on_tab_changed)

        IntegrationUIHandler(self, self.ui, self.a2)

    def remember_last_toggle(self, state):
        self.a2.db.set('remember_last', state)

    def set_a2_hotkey(self, key):
        self.a2.db.set('a2_hotkey', key)
        self.main.settings_changed('hotkeys')

    def build_add_source_menu(self):
        icons = a2ctrl.Icons.inst()
        menu = self.add_source_menu
        menu.clear()

        if self.a2.dev_mode:
            menu.addAction(icons.folder_add, 'Create Local', self.main.create_local_source)

        menu.addAction(icons.cloud_download, 'Add From URL', self.add_source_url)

        featured_path = os.path.join(self.a2.paths.defaults, 'featured_packages.json')
        featured_packages = a2util.json_read(featured_path)
        available = set(featured_packages).difference(self.a2.module_sources)
        if available:
            submenu = menu.addMenu('Featured:')
            for pack_name in available:
                action = submenu.addAction(icons.file_download, pack_name, self.on_add_featured)
                action.setData(featured_packages[pack_name])
        menu.popup(QtGui.QCursor.pos())

    def get_db_digest(self):
        self.ui.db_printout.clear()
        self.ui.db_printout.setText(self.a2.db._get_digest())

    def on_add_featured(self):
        self.add_source_url(self.sender().data())

    def add_source_url(self, url=None):
        dialog = a2module_source.AddSourceDialog(self.main, url)
        dialog.okayed.connect(self.main.load_runtime_and_ui)
        dialog.show()

    def on_tab_changed(self, tab_index):
        widget = self.ui.a2settings_tab.widget(tab_index)
        if widget.children():
            return

        build_func_name = f'_build_{widget.objectName()}'
        try:
            build_func = getattr(self, build_func_name)
        except AttributeError:
            return

        build_func(widget)
        widget.sizeHint = self._size_hint

    def _build_licenses_tab(self, widget):
        """Build the licenses tab on demand."""
        from a2widget import a2licenses_widget_ui

        a2ctrl.check_ui_module(a2licenses_widget_ui)
        ui = a2licenses_widget_ui.Ui_Form()
        ui.setupUi(self.ui.a2settings_tab)
        text = ui.a2license_text.text()
        for tag, version in (
            ('{ahk_version}', a2ahk.call_lib_cmd('get_AutoHotkey_version')),
            ('{py_version}', sys.version.split(' ', 1)[0]),
            ('{qt_version}', QtCore.__version__),
        ):
            if tag in text:
                text = text.replace(tag, version)
        ui.a2license_text.setText(text)
        widget.setLayout(ui.license_layout)

    def _build_console_tab(self, widget):
        ConsoleUiHandler(self, widget, self.ui, self.a2)

    def _build_advanced_tab(self, widget):
        AdvancedSettingsUiHandler(self, widget, self.ui, self.a2)

    def _size_hint(self):
        """For building the tab widgets dynamically. Default sizeHint is WAY too big!"""
        return QtCore.QSize(0, 0)


class ProxyUiHandler:
    def __init__(self, ui, a2):
        self.ui = ui
        self.a2 = a2
        self.proxy_items = 'user', 'pass', 'server', 'port'

        # filling proxy ui
        self.ui.proxy_box.setChecked(self.a2.db.get('proxy_enabled') or False)
        settings = self.a2.db.get('proxy_settings') or {}
        self.ui.proxy_http.setCurrentIndex(('http', 'https').index(settings.get('http') or 'http'))
        proxy_line_widgets = (
            self.ui.proxy_user,
            self.ui.proxy_pass,
            self.ui.proxy_server,
            self.ui.proxy_port,
        )
        for i, name in enumerate(self.proxy_items):
            value = settings.get(name) or ''
            proxy_line_widgets[i].setText(value)

        self.ui.proxy_box.clicked.connect(self.check_proxy_settings)
        self.ui.proxy_http.currentIndexChanged.connect(self.check_proxy_settings)
        for widget in proxy_line_widgets:
            widget.textChanged.connect(self.check_proxy_settings)

    def check_proxy_settings(self):
        self.a2.db.set('proxy_enabled', self.ui.proxy_box.isChecked())
        settings = {'http': ('http', 'https')[self.ui.proxy_http.currentIndex()]}
        for item in self.proxy_items:
            widget = getattr(self.ui, 'proxy_' + item)
            text = widget.text()
            if text:
                settings[item] = text
        self.a2.db.set('proxy_settings', settings)
        self.a2.setup_proxy()


class DataPathUiHandler(QtCore.QObject):
    def __init__(self, parent, ui, a2):
        super(DataPathUiHandler, self).__init__(parent)
        self.ui = ui
        self.a2 = a2
        self.ui.data_folder.setText(self.a2.paths.data)

        if self.a2.is_portable():
            self.ui.button_set_user_dir_standard.hide()
            self.ui.button_set_user_dir_custom.hide()
        else:
            self.ui.portable_label.hide()
            self.ui.button_set_user_dir_standard.clicked.connect(self.set_standard)
            self.ui.button_set_user_dir_custom.clicked.connect(self.build_custom_data_menu)
            self.ui.button_set_user_dir_custom.setIcon(a2ctrl.Icons.inst().more)
            self.menu = QtWidgets.QMenu(self.ui.button_set_user_dir_custom)

            self.ui.button_set_user_dir_standard.setEnabled(self.a2.paths.has_data_override())

    def set_standard(self):
        self._set_path(None)

    def build_custom_data_menu(self):
        icons = a2ctrl.Icons.inst()
        self.menu.clear()

        for path in self.a2.db.get('recent_override_paths') or ():
            action = self.menu.addAction(icons.folder, path, self._on_set_path_action)
            action.setData(path)

        self.menu.addAction(icons.folder2, 'Browse ...', self.browse)
        if (
            self.is_dev
            and os.path.isdir(self.dev_data_path)
            and self.dev_data_path != self.a2.paths.data
        ):
            self.menu.addAction(icons.folder2, 'Use Dev Location', self.use_dev)

        self.menu.popup(QtGui.QCursor.pos())

    def _set_path(self, path):
        """Set the data path and deal with restarts and all."""
        self.a2.paths.set_data_override(path)

        # enlist to recent paths list
        if path and path not in (self.a2.paths.default_data, self.dev_data_path):
            recent_override_paths = self.a2.db.get('recent_override_paths') or []
            if a2util.rolling_list_add(path, recent_override_paths):
                self.a2.db.set('recent_override_paths', recent_override_paths)

        self.a2.start_up()
        self.a2.win.load_runtime_and_ui()

    def _on_set_path_action(self):
        self._set_path(self.sender().data())

    def browse(self):
        file_path = QtWidgets.QFileDialog.getExistingDirectory(
            self.a2.win, caption='Select a Custom Data path', dir=self.a2.paths.data
        )
        if file_path:
            self._set_path(file_path)

    def use_dev(self):
        self._set_path(self.dev_data_path)

    @property
    def is_dev(self):
        return os.path.isdir(os.path.join(self.a2.paths.a2, '.git'))

    @property
    def dev_data_path(self):
        return os.path.join(self.a2.paths.a2, 'data')


class IntegrationUIHandler(QtCore.QObject):
    """
    Care for the system integration checkboxes in the main menu. Currently:
    * Load on Windows Start
    * Add Desktop Shortcut
    * Add Start Menu Schortcuts - which are
      . Start Runtime
      . Open a2 UI
      . Uninstall a2
      . Goto a2 Directory
    """

    def __init__(self, parent, ui, a2):
        super(IntegrationUIHandler, self).__init__(parent)
        self.ui = ui
        self.a2 = a2
        self._cmds = None

        if self.a2.is_portable():
            portable_widget = _IntegrationCheckBox(self.parent(), 'Portable Mode', a2)
            portable_widget.check.setEnabled(False)
            portable_widget.check.setChecked(True)
            self.ui.integrations_layout.addWidget(portable_widget)
            # TBD: finish portable checker
            # button = QtWidgets.QPushButton('check')
            # button.clicked.connect(self._check_portable)
            # portable_widget.layout().insertWidget(1, button)
        else:
            for label, data in self.cmds.items():
                widget = _IntegrationCheckBox(self.parent(), label, a2, data)
                self.ui.integrations_layout.addWidget(widget)

    @property
    def cmds(self):
        if self._cmds is None:
            self._cmds = a2util.json_read(
                os.path.join(self.a2.paths.ui, 'a2widget', 'integration_ui.json')
            )
        return self._cmds

    def _check_portable(self):
        for label, data in self.cmds.items():
            current_path = a2ahk.call_lib_cmd(data['get'])
            if current_path:
                log.warn(f'{label} is set! ({current_path})')


class _IntegrationCheckBox(QtWidgets.QWidget):
    def __init__(self, parent, label, a2, data=None):
        super(_IntegrationCheckBox, self).__init__(parent)

        self.a2 = a2
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.check = QtWidgets.QCheckBox(label, self)
        self.check.clicked[bool].connect(self._set)
        layout.addWidget(self.check)

        icon_size = self.a2.win.style.get('icon_size_small')
        pixmap = a2ctrl.Icons.inst().help.pixmap(icon_size)
        self.alert_label = QtWidgets.QLabel('')
        self.alert_label.setPixmap(pixmap)
        layout.addWidget(self.alert_label)

        if data is None:
            self.get_cmd = None
            self.set_cmd = None
            self.path_name = None
        else:
            self.get_cmd = data['get']
            self.set_cmd = data['set']
            self.path_name = data['path_name']
        self._update_checkbox()

    def _set(self, state):
        import a2ahk

        a2ahk.call_lib_cmd(self.set_cmd, self.a2.paths.a2, int(state))
        self._update_checkbox()

    def _update_checkbox(self):
        if self.get_cmd is None:
            self.alert_label.setVisible(False)
            return

        try:
            current_path = a2ahk.call_lib_cmd(self.get_cmd)
            tooltip = None
        except RuntimeError as error:
            current_path = ''
            tooltip = str(error)

        checked = False
        if current_path:
            target_path = getattr(self.a2.paths, self.path_name)
            checked = a2path.is_same(current_path, target_path)
            if not checked:
                if tooltip is None:
                    tooltip = f'Currently set to: {current_path}'

        self.alert_label.setVisible(tooltip is not None)
        for wgt in (self, self.check, self.alert_label):
            wgt.setToolTip(tooltip)
        self.check.setChecked(checked)


class AdvancedSettingsUiHandler(QtCore.QObject):
    dev_setting_changed = QtCore.Signal(str)

    def __init__(self, parent, widget, ui, a2):
        super(AdvancedSettingsUiHandler, self).__init__(parent)
        self.main = parent.main
        self.tab_widget = widget
        self.parent_ui = ui
        self.ui = None
        self.a2 = a2
        self._setup_ui()

    def _setup_ui(self):
        from a2widget import a2settings_advanced_ui

        a2ctrl.check_ui_module(a2settings_advanced_ui)
        self.ui = a2settings_advanced_ui.Ui_Form()
        self.ui.setupUi(self.tab_widget)

        self.ui.dev_box.setChecked(self.a2.dev_mode)
        self.ui.dev_box.clicked[bool].connect(self.dev_mode_toggle)
        self.ui.dev_widget.setVisible(self.a2.dev_mode)
        self.ui.code_editor.file_types = 'Executables (*.exe)'
        self.ui.code_editor.writable = False
        # self.ui.loglevel_debug.clicked[bool].connect(a2core.set_loglevel)

        self.dev_set_dict = self.main.devset.get()
        a2ctrl.connect.control_list(
            [self.ui.author_name, self.ui.author_url, self.ui.code_editor, self.ui.json_indent],
            self.dev_set_dict,
            self.dev_setting_changed,
        )
        self.dev_setting_changed.connect(self.on_dev_setting_changed)

        DataPathUiHandler(self, self.ui, self.a2)
        self.ui.python_executable.setText(self.a2.paths.python)
        self.ui.autohotkey.setText(self.a2.paths.autohotkey)

        # self.ui.show_console.setChecked(os.path.basename(self.a2.paths.python).lower() == 'python.exe')
        # self.ui.show_console.clicked[bool].connect(self.toggle_console)

        # TODO: #182
        # ahk_vars = a2ahk.get_variables(self.a2.paths.settings_ahk)
        # self.ui.startup_tooltips.setChecked(ahk_vars['a2_startup_tool_tips'])
        # self.ui.startup_tooltips.clicked[bool].connect(self.toggle_startup_tooltips)

        self.ui.ui_scale_slider.setValue(self.a2.db.get('ui_scale') or 1.0)
        self.ui.ui_scale_slider.setPageStep(0.1)
        self.ui.ui_scale_slider.editing_finished.connect(self.main.rebuild_css)

        ProxyUiHandler(self.ui, self.a2)

        self._setup_hotkey_dialog()

    def _setup_hotkey_dialog(self):
        current_style = a2hotkey.get_current_style()
        index = 0
        for i, (style, label) in enumerate(a2hotkey.iter_dialog_styles()):
            self.ui.hk_dialog_style.addItem(label)
            if style == current_style:
                index = i
                break
        self.ui.hk_dialog_style.setCurrentIndex(index)
        self.ui.hk_dialog_style.currentTextChanged.connect(a2hotkey.set_dialog_style)

        from a2widget.a2hotkey.keyboard_dialog import layouts

        current_layout = layouts.get_current()
        index = 0
        for i, (keyboard_id, label) in enumerate(layouts.iterate()):
            self.ui.hk_dialog_layout.addItem(label)
            if keyboard_id == current_layout:
                index = i
        self.ui.hk_dialog_layout.setCurrentIndex(index)
        self.ui.hk_dialog_layout.currentTextChanged.connect(layouts.set_layout)

    # def toggle_startup_tooltips(self, state):
    #     a2ahk.set_variable(self.a2.paths.settings_ahk, 'a2_startup_tool_tips', state)

    def on_dev_setting_changed(self, *_args):
        self.main.devset.set(self.dev_set_dict)

    def dev_mode_toggle(self, state):
        self.a2.set_dev_mode(state)
        self.ui.dev_widget.setVisible(state)
        self.main.check_main_menu_bar()


class ConsoleUiHandler(QtCore.QObject):
    def __init__(self, parent, tab_widget, ui, a2):
        super(ConsoleUiHandler, self).__init__(parent)
        self.tab_widget = tab_widget
        self.main = parent.main

        self._start_byte = None
        self._end_byte = None
        self._lines = []
        self._lines_shown = 0
        self._sep = None
        self._init_block_size = pow(2, 12)
        self.a2console = QtWidgets.QPlainTextEdit(self.tab_widget)
        self._setup_ui()

    def _setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self.tab_widget)
        self.a2console.setObjectName('a2console')
        layout.addWidget(self.a2console)

        import a2output

        logger = a2output.get_logwriter()
        self._sep = a2output.SEP

        with open(logger.path) as file_obj:
            num_bytes = os.path.getsize(logger.path)
            if num_bytes > self._init_block_size:
                self._start_byte = num_bytes - self._init_block_size
                file_obj.seek(self._start_byte)
            else:
                self._start_byte = 0
            self._end_byte = num_bytes

            # first line might be incomplete, if so add len to start_byte
            first_line = file_obj.__next__()
            if not self.line_gathered(first_line):
                self._start_byte += len(first_line)

            for line in file_obj:
                self.line_gathered(line)

        self.append_lines()

        self.log_watcher = QtCore.QFileSystemWatcher(self)
        self.log_watcher.addPath(logger.path)
        self.log_watcher.fileChanged.connect(self._log_changed)

        QtCore.QTimer(self).singleShot(100, self._scroll_to_bottom)

    def _log_changed(self, log_path):
        with open(log_path) as file_obj:
            file_obj.seek(self._end_byte)
            for line in file_obj:
                self.line_gathered(line)
            self._end_byte = file_obj.tell()
        self.append_lines()

    def _scroll_to_bottom(self):
        self.main._scroll(self.a2console, True, 10)

    def line_gathered(self, line):
        try:
            timestamp, txt = line.split(self._sep, 1)
            if len(timestamp) < 11:
                return False
            txt = txt.strip()
            if not txt:
                return False
            self._lines.append((float(timestamp), txt))
        except ValueError:
            return False
        return True

    def append_lines(self):
        start, end = self._lines_shown, len(self._lines)
        if start == end:
            return

        content = '\n'.join('%.2f - %s' % (ftime, txt) for ftime, txt in self._lines[start:end])
        self.a2console.appendPlainText(content)
        self._lines_shown = end
