# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'package_download.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_package_download(object):
    def setupUi(self, package_download):
        package_download.setObjectName("package_download")
        package_download.setWindowModality(QtCore.Qt.WindowModal)
        package_download.resize(620, 605)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        package_download.setFont(font)
        package_download.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(package_download)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_14.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.uiPlainTextEdit_package_names = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.uiPlainTextEdit_package_names.setObjectName("uiPlainTextEdit_package_names")
        self.verticalLayout_8.addWidget(self.uiPlainTextEdit_package_names)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiPushButton_clear_package_names = QtWidgets.QPushButton(self.centralwidget)
        self.uiPushButton_clear_package_names.setObjectName("uiPushButton_clear_package_names")
        self.horizontalLayout_3.addWidget(self.uiPushButton_clear_package_names)
        self.uiPushButton_load_from_text = QtWidgets.QPushButton(self.centralwidget)
        self.uiPushButton_load_from_text.setObjectName("uiPushButton_load_from_text")
        self.horizontalLayout_3.addWidget(self.uiPushButton_load_from_text)
        self.uiPushButton_save_as_text = QtWidgets.QPushButton(self.centralwidget)
        self.uiPushButton_save_as_text.setObjectName("uiPushButton_save_as_text")
        self.horizontalLayout_3.addWidget(self.uiPushButton_save_as_text)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_11.addWidget(self.line_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.uiComboBox_derived_from = QtWidgets.QComboBox(self.centralwidget)
        self.uiComboBox_derived_from.setObjectName("uiComboBox_derived_from")
        self.verticalLayout_9.addWidget(self.uiComboBox_derived_from)
        self.verticalLayout_11.addLayout(self.verticalLayout_9)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_11.addWidget(self.line_8)
        self.uiLabel_pkgdownload_tips = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.uiLabel_pkgdownload_tips.setFont(font)
        self.uiLabel_pkgdownload_tips.setWordWrap(True)
        self.uiLabel_pkgdownload_tips.setObjectName("uiLabel_pkgdownload_tips")
        self.verticalLayout_11.addWidget(self.uiLabel_pkgdownload_tips)
        self.horizontalLayout_6.addLayout(self.verticalLayout_11)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.uiCheckBox_download_deps = QtWidgets.QCheckBox(self.groupBox)
        self.uiCheckBox_download_deps.setObjectName("uiCheckBox_download_deps")
        self.verticalLayout_7.addWidget(self.uiCheckBox_download_deps)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.uiRadioButton_unlimited = QtWidgets.QRadioButton(self.groupBox_2)
        self.uiRadioButton_unlimited.setObjectName("uiRadioButton_unlimited")
        self.verticalLayout_5.addWidget(self.uiRadioButton_unlimited)
        self.uiRadioButton_no_binary = QtWidgets.QRadioButton(self.groupBox_2)
        self.uiRadioButton_no_binary.setObjectName("uiRadioButton_no_binary")
        self.verticalLayout_5.addWidget(self.uiRadioButton_no_binary)
        self.uiRadioButton_only_binary = QtWidgets.QRadioButton(self.groupBox_2)
        self.uiRadioButton_only_binary.setObjectName("uiRadioButton_only_binary")
        self.verticalLayout_5.addWidget(self.uiRadioButton_only_binary)
        self.uiRadioButton_prefer_binary = QtWidgets.QRadioButton(self.groupBox_2)
        self.uiRadioButton_prefer_binary.setObjectName("uiRadioButton_prefer_binary")
        self.verticalLayout_5.addWidget(self.uiRadioButton_prefer_binary)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.uiCheckBox_include_pre = QtWidgets.QCheckBox(self.groupBox)
        self.uiCheckBox_include_pre.setObjectName("uiCheckBox_include_pre")
        self.verticalLayout_7.addWidget(self.uiCheckBox_include_pre)
        self.uiCheckBox_ignore_requires_python = QtWidgets.QCheckBox(self.groupBox)
        self.uiCheckBox_ignore_requires_python.setObjectName("uiCheckBox_ignore_requires_python")
        self.verticalLayout_7.addWidget(self.uiCheckBox_ignore_requires_python)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.uiPushButton_save_to = QtWidgets.QPushButton(self.groupBox)
        self.uiPushButton_save_to.setObjectName("uiPushButton_save_to")
        self.horizontalLayout_5.addWidget(self.uiPushButton_save_to)
        self.horizontalLayout_5.setStretch(0, 9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.uiLineEdit_save_to = QtWidgets.QLineEdit(self.groupBox)
        self.uiLineEdit_save_to.setObjectName("uiLineEdit_save_to")
        self.verticalLayout_2.addWidget(self.uiLineEdit_save_to)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.uiLineEdit_platform = QtWidgets.QLineEdit(self.groupBox)
        self.uiLineEdit_platform.setObjectName("uiLineEdit_platform")
        self.verticalLayout.addWidget(self.uiLineEdit_platform)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.uiLineEdit_python_version = QtWidgets.QLineEdit(self.groupBox)
        self.uiLineEdit_python_version.setMinimumSize(QtCore.QSize(180, 0))
        self.uiLineEdit_python_version.setMaximumSize(QtCore.QSize(180, 16777215))
        self.uiLineEdit_python_version.setObjectName("uiLineEdit_python_version")
        self.horizontalLayout.addWidget(self.uiLineEdit_python_version)
        self.horizontalLayout.setStretch(1, 9)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.uiComboBox_implementation = QtWidgets.QComboBox(self.groupBox)
        self.uiComboBox_implementation.setMinimumSize(QtCore.QSize(180, 0))
        self.uiComboBox_implementation.setMaximumSize(QtCore.QSize(180, 16777215))
        self.uiComboBox_implementation.setObjectName("uiComboBox_implementation")
        self.uiComboBox_implementation.addItem("")
        self.uiComboBox_implementation.setItemText(0, "")
        self.uiComboBox_implementation.addItem("")
        self.uiComboBox_implementation.addItem("")
        self.uiComboBox_implementation.addItem("")
        self.uiComboBox_implementation.addItem("")
        self.uiComboBox_implementation.addItem("")
        self.horizontalLayout_2.addWidget(self.uiComboBox_implementation)
        self.horizontalLayout_2.setStretch(1, 9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.uiLineEdit_abis = QtWidgets.QLineEdit(self.groupBox)
        self.uiLineEdit_abis.setObjectName("uiLineEdit_abis")
        self.verticalLayout_3.addWidget(self.uiLineEdit_abis)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.uiCheckBox_use_index_url = QtWidgets.QCheckBox(self.groupBox)
        self.uiCheckBox_use_index_url.setObjectName("uiCheckBox_use_index_url")
        self.verticalLayout_4.addWidget(self.uiCheckBox_use_index_url)
        self.uiLineEdit_index_url = QtWidgets.QLineEdit(self.groupBox)
        self.uiLineEdit_index_url.setObjectName("uiLineEdit_index_url")
        self.verticalLayout_4.addWidget(self.uiLineEdit_index_url)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_12.addLayout(self.verticalLayout_7)
        self.verticalLayout_13.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uiPushButton_show_dllist = QtWidgets.QPushButton(self.centralwidget)
        self.uiPushButton_show_dllist.setMinimumSize(QtCore.QSize(0, 42))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.uiPushButton_show_dllist.setFont(font)
        self.uiPushButton_show_dllist.setObjectName("uiPushButton_show_dllist")
        self.horizontalLayout_4.addWidget(self.uiPushButton_show_dllist)
        self.uiPushButton_start_download = QtWidgets.QPushButton(self.centralwidget)
        self.uiPushButton_start_download.setMinimumSize(QtCore.QSize(0, 42))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.uiPushButton_start_download.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.uiPushButton_start_download.setFont(font)
        self.uiPushButton_start_download.setObjectName("uiPushButton_start_download")
        self.horizontalLayout_4.addWidget(self.uiPushButton_start_download)
        self.verticalLayout_13.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        self.verticalLayout_14.addLayout(self.horizontalLayout_6)
        package_download.setCentralWidget(self.centralwidget)

        self.retranslateUi(package_download)
        QtCore.QMetaObject.connectSlotsByName(package_download)

    def retranslateUi(self, package_download):
        _translate = QtCore.QCoreApplication.translate
        package_download.setWindowTitle(_translate("package_download", "模块安装包下载"))
        self.label.setToolTip(_translate("package_download", "需要下载的模块名称，每行一个名称。"))
        self.label.setText(_translate("package_download", "名称："))
        self.uiPlainTextEdit_package_names.setToolTip(_translate("package_download", "需要下载的模块名称，每行一个名称。"))
        self.uiPushButton_clear_package_names.setToolTip(_translate("package_download", "清空名称编辑区文字。"))
        self.uiPushButton_clear_package_names.setText(_translate("package_download", "清空"))
        self.uiPushButton_load_from_text.setToolTip(_translate("package_download", "从文本文件加载名称到名称编辑区。"))
        self.uiPushButton_load_from_text.setText(_translate("package_download", "从文件加载名称"))
        self.uiPushButton_save_as_text.setToolTip(_translate("package_download", "将名称编辑区的文字保存到文本文件。"))
        self.uiPushButton_save_as_text.setText(_translate("package_download", "名称保存到文件"))
        self.label_8.setToolTip(_translate("package_download", "下载安装包时需调用的 Python 环境。\n"
"右侧留空的下载条件，下载时会使用从此环境派生的条件。"))
        self.label_8.setText(_translate("package_download", "下载条件默认派生自："))
        self.uiComboBox_derived_from.setToolTip(_translate("package_download", "下载安装包时需调用的 Python 环境。\n"
"右侧留空的下载条件，下载时会使用从此环境派生的条件。"))
        self.uiLabel_pkgdownload_tips.setText(_translate("package_download", "名称后支持跟随以下符号限定要下载的版本：\n"
"\"==\"、\">=\"、\"<=\"、\">\"、\"<\"、\",\"\n"
"每行一个名称，名称和限定符中不允许出现空格。\n"
"例如：fastpip>=0.6.2,<0.10.0\n"
"如果限制条件留空，则下载兼容所选环境的安装包。"))
        self.groupBox.setTitle(_translate("package_download", "下载条件"))
        self.uiCheckBox_download_deps.setToolTip(_translate("package_download", "对于名称编辑区中的每一个需要下载的模块，是否同时下载模块的依赖库。"))
        self.uiCheckBox_download_deps.setText(_translate("package_download", "下载需要下载的包的依赖"))
        self.uiRadioButton_unlimited.setToolTip(_translate("package_download", "不限制下载二进制包或者源代码包。"))
        self.uiRadioButton_unlimited.setText(_translate("package_download", "不限制下载的包类型"))
        self.uiRadioButton_no_binary.setToolTip(_translate("package_download", "仅下载包的源代码安装包。"))
        self.uiRadioButton_no_binary.setText(_translate("package_download", "仅选择源代码包"))
        self.uiRadioButton_only_binary.setToolTip(_translate("package_download", "仅下载包的二进制安装包。"))
        self.uiRadioButton_only_binary.setText(_translate("package_download", "仅选择二进制包"))
        self.uiRadioButton_prefer_binary.setToolTip(_translate("package_download", "对于既有二进制安装包又有源代码安装包的模块，\n"
"如果较新版本没有发布二进制安装包，则宁愿下载较旧版本的二进制安装包。"))
        self.uiRadioButton_prefer_binary.setText(_translate("package_download", "宁选择旧二进制包而非新源代码包"))
        self.uiCheckBox_include_pre.setToolTip(_translate("package_download", "如果模块的最新版本是预发行版或者是开发版，\n"
"也下载这些版本，否则只下载模块的最新稳定版本。"))
        self.uiCheckBox_include_pre.setText(_translate("package_download", "包括预发行版和开发版"))
        self.uiCheckBox_ignore_requires_python.setToolTip(_translate("package_download", "对于那些对 Python 版本有限制要求的模块，是否忽略其限制要求。"))
        self.uiCheckBox_ignore_requires_python.setText(_translate("package_download", "忽略包的 Python 版本限制"))
        self.label_3.setToolTip(_translate("package_download", "下载的模块安装包的保存路径。"))
        self.label_3.setText(_translate("package_download", "下载至："))
        self.uiPushButton_save_to.setToolTip(_translate("package_download", "选择下载的模块安装包的保存路径。"))
        self.uiPushButton_save_to.setText(_translate("package_download", "选择目录"))
        self.uiLineEdit_save_to.setToolTip(_translate("package_download", "下载的模块安装包的保存路径。"))
        self.label_4.setToolTip(_translate("package_download", "是否只下载兼容此处列出的平台的模块安装包。"))
        self.label_4.setText(_translate("package_download", "兼容平台(空格分隔)："))
        self.uiLineEdit_platform.setToolTip(_translate("package_download", "是否只下载兼容此处列出的平台的模块安装包。"))
        self.label_5.setToolTip(_translate("package_download", "是否只下载兼容此处列出的 Python 版本的模块安装包。"))
        self.label_5.setText(_translate("package_download", "兼容 Python 版本："))
        self.uiLineEdit_python_version.setToolTip(_translate("package_download", "是否只下载兼容此处列出的 Python 版本的模块安装包。"))
        self.label_6.setToolTip(_translate("package_download", "是否只下载兼容此处列出的 Python 实现的模块安装包。"))
        self.label_6.setText(_translate("package_download", "兼容解释器实现："))
        self.uiComboBox_implementation.setToolTip(_translate("package_download", "是否只下载兼容此处列出的 Python 实现的模块安装包。"))
        self.uiComboBox_implementation.setItemText(1, _translate("package_download", "无特定实现"))
        self.uiComboBox_implementation.setItemText(2, _translate("package_download", "CPython"))
        self.uiComboBox_implementation.setItemText(3, _translate("package_download", "Jython"))
        self.uiComboBox_implementation.setItemText(4, _translate("package_download", "PyPy"))
        self.uiComboBox_implementation.setItemText(5, _translate("package_download", "IronPython"))
        self.label_7.setToolTip(_translate("package_download", "是否只下载兼容此处列出的 Python ABI的模块安装包。"))
        self.label_7.setText(_translate("package_download", "兼容ABI(空格分隔)："))
        self.uiLineEdit_abis.setToolTip(_translate("package_download", "是否只下载兼容此处列出的 Python ABI的模块安装包。"))
        self.uiCheckBox_use_index_url.setToolTip(_translate("package_download", "是否从临时镜像源下载安装包。\n"
"如果不勾选此选项，则默认从系统已设置的镜像源地址下载。"))
        self.uiCheckBox_use_index_url.setText(_translate("package_download", "使用临时镜像源："))
        self.uiLineEdit_index_url.setToolTip(_translate("package_download", "临时镜像源地址。"))
        self.uiPushButton_show_dllist.setText(_translate("package_download", "下载列表"))
        self.uiPushButton_start_download.setText(_translate("package_download", "开始下载"))