# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyInstallerTool.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PyInstallerTool(object):
    def setupUi(self, PyInstallerTool):
        PyInstallerTool.setObjectName("PyInstallerTool")
        PyInstallerTool.setWindowModality(QtCore.Qt.ApplicationModal)
        PyInstallerTool.resize(870, 776)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        PyInstallerTool.setFont(font)
        self.centralwidget = QtWidgets.QWidget(PyInstallerTool)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_project_files = QtWidgets.QWidget()
        self.tab_project_files.setObjectName("tab_project_files")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.tab_project_files)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tab_project_files)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.le_program_entry_old = QtWidgets.QLineEdit(self.tab_project_files)
        self.le_program_entry_old.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.le_program_entry_old.setObjectName("le_program_entry_old")
        self.horizontalLayout_3.addWidget(self.le_program_entry_old)
        self.pb_select_program_entry = QtWidgets.QPushButton(self.tab_project_files)
        self.pb_select_program_entry.setObjectName("pb_select_program_entry")
        self.horizontalLayout_3.addWidget(self.pb_select_program_entry)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_13 = QtWidgets.QLabel(self.tab_project_files)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_19.addWidget(self.label_13)
        self.le_exefile_specfile_name = QtWidgets.QLineEdit(self.tab_project_files)
        self.le_exefile_specfile_name.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.le_exefile_specfile_name.setObjectName("le_exefile_specfile_name")
        self.verticalLayout_19.addWidget(self.le_exefile_specfile_name)
        self.verticalLayout_5.addLayout(self.verticalLayout_19)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_2 = QtWidgets.QLabel(self.tab_project_files)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_21.addWidget(self.label_2)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.pb_reset_root_level = QtWidgets.QPushButton(self.tab_project_files)
        self.pb_reset_root_level.setObjectName("pb_reset_root_level")
        self.horizontalLayout_20.addWidget(self.pb_reset_root_level)
        self.pb_up_level_root = QtWidgets.QPushButton(self.tab_project_files)
        self.pb_up_level_root.setObjectName("pb_up_level_root")
        self.horizontalLayout_20.addWidget(self.pb_up_level_root)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21.setStretch(0, 9)
        self.verticalLayout.addLayout(self.horizontalLayout_21)
        self.le_project_root = QtWidgets.QLineEdit(self.tab_project_files)
        self.le_project_root.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.le_project_root.setReadOnly(True)
        self.le_project_root.setObjectName("le_project_root")
        self.verticalLayout.addWidget(self.le_project_root)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line = QtWidgets.QFrame(self.tab_project_files)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.tab_project_files)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.pb_clear_module_search_path = QtWidgets.QPushButton(self.tab_project_files)
        self.pb_clear_module_search_path.setObjectName("pb_clear_module_search_path")
        self.horizontalLayout_5.addWidget(self.pb_clear_module_search_path)
        self.pb_select_module_search_path = QtWidgets.QPushButton(self.tab_project_files)
        self.pb_select_module_search_path.setObjectName("pb_select_module_search_path")
        self.horizontalLayout_5.addWidget(self.pb_select_module_search_path)
        self.horizontalLayout_5.setStretch(0, 9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.te_module_search_path_old = QtWidgets.QTextEdit(self.tab_project_files)
        self.te_module_search_path_old.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.te_module_search_path_old.setObjectName("te_module_search_path_old")
        self.verticalLayout_3.addWidget(self.te_module_search_path_old)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.tab_project_files)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.tab_project_files)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.pb_clear_other_data = QtWidgets.QPushButton(self.tab_project_files)
        self.pb_clear_other_data.setObjectName("pb_clear_other_data")
        self.horizontalLayout_6.addWidget(self.pb_clear_other_data)
        self.pb_select_other_data = QtWidgets.QPushButton(self.tab_project_files)
        self.pb_select_other_data.setObjectName("pb_select_other_data")
        self.horizontalLayout_6.addWidget(self.pb_select_other_data)
        self.horizontalLayout_6.setStretch(0, 9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.te_other_data_old = QtWidgets.QTextEdit(self.tab_project_files)
        self.te_other_data_old.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.te_other_data_old.setObjectName("te_other_data_old")
        self.verticalLayout_4.addWidget(self.te_other_data_old)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.tab_project_files)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.le_file_icon_path_old = QtWidgets.QLineEdit(self.tab_project_files)
        self.le_file_icon_path_old.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.le_file_icon_path_old.setObjectName("le_file_icon_path_old")
        self.horizontalLayout_11.addWidget(self.le_file_icon_path_old)
        self.pb_select_file_icon = QtWidgets.QPushButton(self.tab_project_files)
        self.pb_select_file_icon.setObjectName("pb_select_file_icon")
        self.horizontalLayout_11.addWidget(self.pb_select_file_icon)
        self.horizontalLayout_11.setStretch(0, 9)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.verticalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_17.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab_project_files, "")
        self.tab_build_control = QtWidgets.QWidget()
        self.tab_build_control.setObjectName("tab_build_control")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_build_control)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.rb_pack_to_one_dir = QtWidgets.QRadioButton(self.tab_build_control)
        self.rb_pack_to_one_dir.setObjectName("rb_pack_to_one_dir")
        self.horizontalLayout_9.addWidget(self.rb_pack_to_one_dir)
        self.rb_pack_to_one_file = QtWidgets.QRadioButton(self.tab_build_control)
        self.rb_pack_to_one_file.setObjectName("rb_pack_to_one_file")
        self.horizontalLayout_9.addWidget(self.rb_pack_to_one_file)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.cb_execute_with_console = QtWidgets.QCheckBox(self.tab_build_control)
        self.cb_execute_with_console.setObjectName("cb_execute_with_console")
        self.verticalLayout_12.addWidget(self.cb_execute_with_console)
        self.cb_without_confirm = QtWidgets.QCheckBox(self.tab_build_control)
        self.cb_without_confirm.setObjectName("cb_without_confirm")
        self.verticalLayout_12.addWidget(self.cb_without_confirm)
        self.cb_use_upx = QtWidgets.QCheckBox(self.tab_build_control)
        self.cb_use_upx.setObjectName("cb_use_upx")
        self.verticalLayout_12.addWidget(self.cb_use_upx)
        self.cb_clean_before_build = QtWidgets.QCheckBox(self.tab_build_control)
        self.cb_clean_before_build.setObjectName("cb_clean_before_build")
        self.verticalLayout_12.addWidget(self.cb_clean_before_build)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_11 = QtWidgets.QLabel(self.tab_build_control)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.le_bytecode_encryption_key = QtWidgets.QLineEdit(self.tab_build_control)
        self.le_bytecode_encryption_key.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.le_bytecode_encryption_key.setObjectName("le_bytecode_encryption_key")
        self.horizontalLayout_15.addWidget(self.le_bytecode_encryption_key)
        self.verticalLayout_12.addLayout(self.horizontalLayout_15)
        self.line_4 = QtWidgets.QFrame(self.tab_build_control)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_12.addWidget(self.line_4)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.tab_build_control)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.le_output_dir = QtWidgets.QLineEdit(self.tab_build_control)
        self.le_output_dir.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.le_output_dir.setObjectName("le_output_dir")
        self.horizontalLayout_12.addWidget(self.le_output_dir)
        self.pb_select_output_dir = QtWidgets.QPushButton(self.tab_build_control)
        self.pb_select_output_dir.setObjectName("pb_select_output_dir")
        self.horizontalLayout_12.addWidget(self.pb_select_output_dir)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.verticalLayout_12.addLayout(self.verticalLayout_9)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_17 = QtWidgets.QLabel(self.tab_build_control)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_15.addWidget(self.label_17)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.le_spec_dir = QtWidgets.QLineEdit(self.tab_build_control)
        self.le_spec_dir.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.le_spec_dir.setObjectName("le_spec_dir")
        self.horizontalLayout_16.addWidget(self.le_spec_dir)
        self.pb_select_spec_dir = QtWidgets.QPushButton(self.tab_build_control)
        self.pb_select_spec_dir.setObjectName("pb_select_spec_dir")
        self.horizontalLayout_16.addWidget(self.pb_select_spec_dir)
        self.verticalLayout_15.addLayout(self.horizontalLayout_16)
        self.verticalLayout_12.addLayout(self.verticalLayout_15)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.tab_build_control)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.le_temp_working_dir = QtWidgets.QLineEdit(self.tab_build_control)
        self.le_temp_working_dir.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.le_temp_working_dir.setObjectName("le_temp_working_dir")
        self.horizontalLayout_14.addWidget(self.le_temp_working_dir)
        self.pb_select_temp_working_dir = QtWidgets.QPushButton(self.tab_build_control)
        self.pb_select_temp_working_dir.setObjectName("pb_select_temp_working_dir")
        self.horizontalLayout_14.addWidget(self.pb_select_temp_working_dir)
        self.verticalLayout_11.addLayout(self.horizontalLayout_14)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.tab_build_control)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_10.addWidget(self.label_9)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.le_upx_search_path = QtWidgets.QLineEdit(self.tab_build_control)
        self.le_upx_search_path.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.le_upx_search_path.setObjectName("le_upx_search_path")
        self.horizontalLayout_13.addWidget(self.le_upx_search_path)
        self.pb_select_upx_search_path = QtWidgets.QPushButton(self.tab_build_control)
        self.pb_select_upx_search_path.setObjectName("pb_select_upx_search_path")
        self.horizontalLayout_13.addWidget(self.pb_select_upx_search_path)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.verticalLayout_12.addLayout(self.verticalLayout_10)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.tab_build_control)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.le_version_file = QtWidgets.QLineEdit(self.tab_build_control)
        self.le_version_file.setEnabled(False)
        self.le_version_file.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.le_version_file.setObjectName("le_version_file")
        self.horizontalLayout_10.addWidget(self.le_version_file)
        self.pb_select_version_file = QtWidgets.QPushButton(self.tab_build_control)
        self.pb_select_version_file.setEnabled(False)
        self.pb_select_version_file.setObjectName("pb_select_version_file")
        self.horizontalLayout_10.addWidget(self.pb_select_version_file)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.verticalLayout_12.addLayout(self.verticalLayout_7)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.tab_build_control)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_13.addWidget(self.label_14)
        self.te_upx_exclude_files = QtWidgets.QTextEdit(self.tab_build_control)
        self.te_upx_exclude_files.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.te_upx_exclude_files.setAcceptDrops(False)
        self.te_upx_exclude_files.setObjectName("te_upx_exclude_files")
        self.verticalLayout_13.addWidget(self.te_upx_exclude_files)
        self.verticalLayout_12.addLayout(self.verticalLayout_13)
        self.verticalLayout_14.addLayout(self.verticalLayout_12)
        self.tabWidget.addTab(self.tab_build_control, "")
        self.horizontalLayout_18.addWidget(self.tabWidget)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_6.addWidget(self.label_15)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb_pyi_info = QtWidgets.QLabel(self.centralwidget)
        self.lb_pyi_info.setFrameShape(QtWidgets.QFrame.Box)
        self.lb_pyi_info.setText("")
        self.lb_pyi_info.setObjectName("lb_pyi_info")
        self.horizontalLayout_2.addWidget(self.lb_pyi_info)
        self.pb_reinstall_pyi = QtWidgets.QPushButton(self.centralwidget)
        self.pb_reinstall_pyi.setObjectName("pb_reinstall_pyi")
        self.horizontalLayout_2.addWidget(self.pb_reinstall_pyi)
        self.horizontalLayout_2.setStretch(0, 9)
        self.verticalLayout_18.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_py_info = QtWidgets.QLabel(self.centralwidget)
        self.lb_py_info.setFrameShape(QtWidgets.QFrame.Box)
        self.lb_py_info.setText("")
        self.lb_py_info.setObjectName("lb_py_info")
        self.horizontalLayout.addWidget(self.lb_py_info)
        self.pb_select_py_env = QtWidgets.QPushButton(self.centralwidget)
        self.pb_select_py_env.setObjectName("pb_select_py_env")
        self.horizontalLayout.addWidget(self.pb_select_py_env)
        self.horizontalLayout.setStretch(0, 9)
        self.verticalLayout_18.addLayout(self.horizontalLayout)
        self.lb_platform_info = QtWidgets.QLabel(self.centralwidget)
        self.lb_platform_info.setMinimumSize(QtCore.QSize(0, 29))
        self.lb_platform_info.setFrameShape(QtWidgets.QFrame.Box)
        self.lb_platform_info.setText("")
        self.lb_platform_info.setObjectName("lb_platform_info")
        self.verticalLayout_18.addWidget(self.lb_platform_info)
        self.horizontalLayout_7.addLayout(self.verticalLayout_18)
        self.horizontalLayout_7.setStretch(1, 9)
        self.verticalLayout_20.addLayout(self.horizontalLayout_7)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_20.addWidget(self.line_5)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_17.addWidget(self.label_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_8.addWidget(self.label_18)
        self.cb_log_level = QtWidgets.QComboBox(self.centralwidget)
        self.cb_log_level.setObjectName("cb_log_level")
        self.cb_log_level.addItem("")
        self.cb_log_level.addItem("")
        self.cb_log_level.addItem("")
        self.cb_log_level.addItem("")
        self.cb_log_level.addItem("")
        self.cb_log_level.addItem("")
        self.horizontalLayout_8.addWidget(self.cb_log_level)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_17.setStretch(0, 9)
        self.verticalLayout_16.addLayout(self.horizontalLayout_17)
        self.te_pyi_out_stream = QtWidgets.QTextEdit(self.centralwidget)
        self.te_pyi_out_stream.setMinimumSize(QtCore.QSize(0, 456))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.te_pyi_out_stream.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.te_pyi_out_stream.setFont(font)
        self.te_pyi_out_stream.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.te_pyi_out_stream.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.te_pyi_out_stream.setReadOnly(True)
        self.te_pyi_out_stream.setObjectName("te_pyi_out_stream")
        self.verticalLayout_16.addWidget(self.te_pyi_out_stream)
        self.verticalLayout_20.addLayout(self.verticalLayout_16)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lb_running_gif = QtWidgets.QLabel(self.centralwidget)
        self.lb_running_gif.setText("")
        self.lb_running_gif.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_running_gif.setObjectName("lb_running_gif")
        self.horizontalLayout_4.addWidget(self.lb_running_gif)
        self.lb_running_tip = QtWidgets.QLabel(self.centralwidget)
        self.lb_running_tip.setText("")
        self.lb_running_tip.setObjectName("lb_running_tip")
        self.horizontalLayout_4.addWidget(self.lb_running_tip)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout_20.addLayout(self.horizontalLayout_4)
        self.pb_gen_executable = QtWidgets.QPushButton(self.centralwidget)
        self.pb_gen_executable.setMinimumSize(QtCore.QSize(0, 56))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pb_gen_executable.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pb_gen_executable.setFont(font)
        self.pb_gen_executable.setObjectName("pb_gen_executable")
        self.verticalLayout_20.addWidget(self.pb_gen_executable)
        self.horizontalLayout_18.addLayout(self.verticalLayout_20)
        self.horizontalLayout_18.setStretch(0, 5)
        self.horizontalLayout_18.setStretch(1, 4)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_18)
        PyInstallerTool.setCentralWidget(self.centralwidget)

        self.retranslateUi(PyInstallerTool)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PyInstallerTool)

    def retranslateUi(self, PyInstallerTool):
        _translate = QtCore.QCoreApplication.translate
        PyInstallerTool.setWindowTitle(_translate("PyInstallerTool", "程序打包工具"))
        self.label.setToolTip(_translate("PyInstallerTool", "要打包的程序的启动入口脚本(*.py *.pyw *.pyc *.spec)，此项必填。\n"
"如果指定了SPEC文件，则以下绝大部分项目文件及生成控制都将不生效。"))
        self.label.setText(_translate("PyInstallerTool", "主程序："))
        self.le_program_entry_old.setToolTip(_translate("PyInstallerTool", "要打包的程序的启动入口脚本(*.py *.pyw *.pyc *.spec)，此项必填。\n"
"如果指定了SPEC文件，则以下绝大部分项目文件及生成控制都将不生效。"))
        self.pb_select_program_entry.setText(_translate("PyInstallerTool", "选择"))
        self.label_13.setToolTip(_translate("PyInstallerTool", "打包完成后的exe可执行文件文件的名称，此项留空则使用主程序文件名。"))
        self.label_13.setText(_translate("PyInstallerTool", "生成文件名称："))
        self.le_exefile_specfile_name.setToolTip(_translate("PyInstallerTool", "打包完成后的exe可执行文件文件的名称，此项留空则使用主程序文件名。"))
        self.label_2.setToolTip(_translate("PyInstallerTool", "当前的项目根目录，选择主程序文件后自动确定。"))
        self.label_2.setText(_translate("PyInstallerTool", "项目根目录："))
        self.pb_reset_root_level.setToolTip(_translate("PyInstallerTool", "将项目根目录重置为主程序所在目录。"))
        self.pb_reset_root_level.setText(_translate("PyInstallerTool", "重置"))
        self.pb_up_level_root.setToolTip(_translate("PyInstallerTool", "将项目根目录向上移一级。"))
        self.pb_up_level_root.setText(_translate("PyInstallerTool", "上一级"))
        self.le_project_root.setToolTip(_translate("PyInstallerTool", "当前的项目根目录，选择主程序文件后自动确定。"))
        self.label_3.setToolTip(_translate("PyInstallerTool", "程序的其他模块的搜索目录(仅当PYINSTALLER无法自动找到时使用)。"))
        self.label_3.setText(_translate("PyInstallerTool", "其他模块搜索路径："))
        self.pb_clear_module_search_path.setToolTip(_translate("PyInstallerTool", "清空其他模块搜索目录文本框。"))
        self.pb_clear_module_search_path.setText(_translate("PyInstallerTool", "清空"))
        self.pb_select_module_search_path.setText(_translate("PyInstallerTool", "选择"))
        self.label_4.setToolTip(_translate("PyInstallerTool", "非源代码性质的其他资源文件，例如一些图片、配置文件等。"))
        self.label_4.setText(_translate("PyInstallerTool", "非源代码资源文件："))
        self.pb_clear_other_data.setText(_translate("PyInstallerTool", "清空"))
        self.pb_select_other_data.setText(_translate("PyInstallerTool", "选择"))
        self.label_7.setToolTip(_translate("PyInstallerTool", "生成的exe可执行文件的图标，支持.ico、.icns图标文件。"))
        self.label_7.setText(_translate("PyInstallerTool", "文件图标路径："))
        self.le_file_icon_path_old.setToolTip(_translate("PyInstallerTool", "生成的exe可执行文件的图标，支持.ico、.icns图标文件。"))
        self.pb_select_file_icon.setText(_translate("PyInstallerTool", "选择"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_project_files), _translate("PyInstallerTool", "项目文件"))
        self.rb_pack_to_one_dir.setToolTip(_translate("PyInstallerTool", "将程序打包成单文件夹形式，exe可执行程序在文件夹的首层目录内。"))
        self.rb_pack_to_one_dir.setText(_translate("PyInstallerTool", "打包成单目录(建议)"))
        self.rb_pack_to_one_file.setToolTip(_translate("PyInstallerTool", "将程序以及添加的其他资源文件打包成单一文件的形式，启动速度较慢。"))
        self.rb_pack_to_one_file.setText(_translate("PyInstallerTool", "打包成单文件"))
        self.cb_execute_with_console.setToolTip(_translate("PyInstallerTool", "打包完成后启动程序是否显示命令行窗口，注意，后缀为pyw的主程序打包后不显示控制台，此项设置失效。"))
        self.cb_execute_with_console.setText(_translate("PyInstallerTool", "打包的程序运行时显示控制台"))
        self.cb_without_confirm.setToolTip(_translate("PyInstallerTool", "当要储存生成的exe可执行文件的文件夹不为空时，是否清空该文件夹。"))
        self.cb_without_confirm.setText(_translate("PyInstallerTool", "输出目录不为空时清空而不是中断"))
        self.cb_use_upx.setToolTip(_translate("PyInstallerTool", "打包过程中是否使用upx对文件进行压缩。\n"
"注意，某些二进制文件在经过upx压缩后可能无法正常运行。\n"
"仅当系统环境变量PATH中有upx路径信息或在以下“upx可执行文件查找路径”指定了upx查找路径时，此项设置才生效。"))
        self.cb_use_upx.setText(_translate("PyInstallerTool", "使用UPX对文件进行压缩"))
        self.cb_clean_before_build.setToolTip(_translate("PyInstallerTool", "生成exe可执行文件前是否清空PYINSTALLER生成的临时文件夹(即build文件夹，此文件夹可用于下次加速生成)。"))
        self.cb_clean_before_build.setText(_translate("PyInstallerTool", "构建前清理缓存并删除临时文件"))
        self.label_11.setToolTip(_translate("PyInstallerTool", "用于加密打包过程中生成PYC文件时的加密。"))
        self.label_11.setText(_translate("PyInstallerTool", "字节码加密秘钥："))
        self.le_bytecode_encryption_key.setToolTip(_translate("PyInstallerTool", "用于加密打包过程中生成PYC文件时的加密。"))
        self.le_bytecode_encryption_key.setPlaceholderText(_translate("PyInstallerTool", "可留空，Python字节码的加密秘钥"))
        self.label_8.setText(_translate("PyInstallerTool", "生成文件储存位置："))
        self.le_output_dir.setPlaceholderText(_translate("PyInstallerTool", "可留空，默认储存位置：项目根目录/dist"))
        self.pb_select_output_dir.setText(_translate("PyInstallerTool", "选择"))
        self.label_17.setText(_translate("PyInstallerTool", "SPEC文件储存位置："))
        self.le_spec_dir.setPlaceholderText(_translate("PyInstallerTool", "可留空，默认储存位置：项目根目录"))
        self.pb_select_spec_dir.setText(_translate("PyInstallerTool", "选择"))
        self.label_10.setText(_translate("PyInstallerTool", "临时文件目录："))
        self.le_temp_working_dir.setPlaceholderText(_translate("PyInstallerTool", "可留空，默认目录：项目根目录/build"))
        self.pb_select_temp_working_dir.setText(_translate("PyInstallerTool", "选择"))
        self.label_9.setText(_translate("PyInstallerTool", "UPX可执行文件查找路径："))
        self.le_upx_search_path.setPlaceholderText(_translate("PyInstallerTool", "可留空，找不到UPX时将不进行压缩"))
        self.pb_select_upx_search_path.setText(_translate("PyInstallerTool", "选择"))
        self.label_12.setText(_translate("PyInstallerTool", "可执行文件版本信息文件："))
        self.le_version_file.setToolTip(_translate("PyInstallerTool", "功能暂未完成。"))
        self.pb_select_version_file.setToolTip(_translate("PyInstallerTool", "功能暂未完成。"))
        self.pb_select_version_file.setText(_translate("PyInstallerTool", "选择"))
        self.label_14.setText(_translate("PyInstallerTool", "UPX压缩时排除的文件名："))
        self.te_upx_exclude_files.setPlaceholderText(_translate("PyInstallerTool", "某些动态链接库或可执行文件使用UPX压缩后可能无法正常运行，可将这些文件名添加到此处以使UPX在压缩时略过，文件名之间请使用空格分隔。"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_build_control), _translate("PyInstallerTool", "生成控制"))
        self.label_16.setToolTip(_translate("PyInstallerTool", "所选PYTHON环境下的PYINSTALLER的版本信息。"))
        self.label_16.setText(_translate("PyInstallerTool", "Pyi版本："))
        self.label_6.setToolTip(_translate("PyInstallerTool", "当前选择的PYTHON环境的版本信息。"))
        self.label_6.setText(_translate("PyInstallerTool", "Py信息："))
        self.label_15.setToolTip(_translate("PyInstallerTool", "操作系统的版本信息。"))
        self.label_15.setText(_translate("PyInstallerTool", "系统信息："))
        self.lb_pyi_info.setToolTip(_translate("PyInstallerTool", "所选PYTHON环境下的PYINSTALLER的版本信息。"))
        self.pb_reinstall_pyi.setToolTip(_translate("PyInstallerTool", "在当前选择的PYTHON环境中安装或重新安装PYINSTALLER库。"))
        self.pb_reinstall_pyi.setText(_translate("PyInstallerTool", "安装"))
        self.lb_py_info.setToolTip(_translate("PyInstallerTool", "当前选择的PYTHON环境的版本信息。"))
        self.pb_select_py_env.setToolTip(_translate("PyInstallerTool", "如果可选项目为空，需要先在“包管理器”中添加本机Python环境。"))
        self.pb_select_py_env.setText(_translate("PyInstallerTool", "选择环境"))
        self.lb_platform_info.setToolTip(_translate("PyInstallerTool", "操作系统的版本信息。"))
        self.label_5.setToolTip(_translate("PyInstallerTool", "打包时输出的流程信息，包含一些用于分析打包问题的信息。"))
        self.label_5.setText(_translate("PyInstallerTool", "日志信息："))
        self.label_18.setToolTip(_translate("PyInstallerTool", "打包程序时输出的流程信息的详细程度，越靠前越详细，默认INFO。"))
        self.label_18.setText(_translate("PyInstallerTool", "追踪级别："))
        self.cb_log_level.setToolTip(_translate("PyInstallerTool", "打包程序时输出的流程信息的详细程度，越靠前越详细，默认INFO。"))
        self.cb_log_level.setItemText(0, _translate("PyInstallerTool", "TRACE"))
        self.cb_log_level.setItemText(1, _translate("PyInstallerTool", "DEBUG"))
        self.cb_log_level.setItemText(2, _translate("PyInstallerTool", "INFO"))
        self.cb_log_level.setItemText(3, _translate("PyInstallerTool", "WARN"))
        self.cb_log_level.setItemText(4, _translate("PyInstallerTool", "ERROR"))
        self.cb_log_level.setItemText(5, _translate("PyInstallerTool", "CRITICAL"))
        self.te_pyi_out_stream.setToolTip(_translate("PyInstallerTool", "打包时输出的流程信息，包含一些用于分析打包问题的信息。"))
        self.pb_gen_executable.setText(_translate("PyInstallerTool", "生成可执行文件"))
