# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guioverview.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(793, 555)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLabel.sizePolicy().hasHeightForWidth())
        self.labelLabel.setSizePolicy(sizePolicy)
        self.labelLabel.setObjectName(_fromUtf8("labelLabel"))
        self.horizontalLayout.addWidget(self.labelLabel)
        self.lineEditLabel = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditLabel.sizePolicy().hasHeightForWidth())
        self.lineEditLabel.setSizePolicy(sizePolicy)
        self.lineEditLabel.setObjectName(_fromUtf8("lineEditLabel"))
        self.horizontalLayout.addWidget(self.lineEditLabel)
        self.checkBoxInitH5 = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxInitH5.setObjectName(_fromUtf8("checkBoxInitH5"))
        self.horizontalLayout.addWidget(self.checkBoxInitH5)
        self.checkBoxSetStates = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxSetStates.setChecked(True)
        self.checkBoxSetStates.setObjectName(_fromUtf8("checkBoxSetStates"))
        self.horizontalLayout.addWidget(self.checkBoxSetStates)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.tableViewChannels = QtGui.QTableView(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewChannels.sizePolicy().hasHeightForWidth())
        self.tableViewChannels.setSizePolicy(sizePolicy)
        self.tableViewChannels.setFrameShape(QtGui.QFrame.Box)
        self.tableViewChannels.setAlternatingRowColors(True)
        self.tableViewChannels.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableViewChannels.setSortingEnabled(True)
        self.tableViewChannels.setObjectName(_fromUtf8("tableViewChannels"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBoxLeftImage = QtGui.QComboBox(self.layoutWidget)
        self.comboBoxLeftImage.setObjectName(_fromUtf8("comboBoxLeftImage"))
        self.verticalLayout.addWidget(self.comboBoxLeftImage)
        self.scrollAreaImage = QtGui.QScrollArea(self.layoutWidget)
        self.scrollAreaImage.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollAreaImage.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollAreaImage.setWidgetResizable(False)
        self.scrollAreaImage.setObjectName(_fromUtf8("scrollAreaImage"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 57, 599))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollAreaImage.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollAreaImage)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.comboBoxRightImage = QtGui.QComboBox(self.layoutWidget1)
        self.comboBoxRightImage.setObjectName(_fromUtf8("comboBoxRightImage"))
        self.verticalLayout_2.addWidget(self.comboBoxRightImage)
        self.scrollAreaImageRight = QtGui.QScrollArea(self.layoutWidget1)
        self.scrollAreaImageRight.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollAreaImageRight.setWidgetResizable(False)
        self.scrollAreaImageRight.setObjectName(_fromUtf8("scrollAreaImageRight"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 186, 499))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.scrollAreaImageRight.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.addWidget(self.scrollAreaImageRight)
        self.verticalLayout_3.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName(_fromUtf8("menuActions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Initialize_from_current_folder = QtGui.QAction(MainWindow)
        self.action_Initialize_from_current_folder.setObjectName(_fromUtf8("action_Initialize_from_current_folder"))
        self.actionToggleExtract = QtGui.QAction(MainWindow)
        self.actionToggleExtract.setObjectName(_fromUtf8("actionToggleExtract"))
        self.actionToggleSort = QtGui.QAction(MainWindow)
        self.actionToggleSort.setObjectName(_fromUtf8("actionToggleSort"))
        self.action_Next_channel = QtGui.QAction(MainWindow)
        self.action_Next_channel.setObjectName(_fromUtf8("action_Next_channel"))
        self.action_Previous_channel = QtGui.QAction(MainWindow)
        self.action_Previous_channel.setObjectName(_fromUtf8("action_Previous_channel"))
        self.actionSave_actions_to_file = QtGui.QAction(MainWindow)
        self.actionSave_actions_to_file.setObjectName(_fromUtf8("actionSave_actions_to_file"))
        self.actionOne_Down = QtGui.QAction(MainWindow)
        self.actionOne_Down.setObjectName(_fromUtf8("actionOne_Down"))
        self.actionToggle_sort_negative = QtGui.QAction(MainWindow)
        self.actionToggle_sort_negative.setObjectName(_fromUtf8("actionToggle_sort_negative"))
        self.actionToggle_sorted_positive = QtGui.QAction(MainWindow)
        self.actionToggle_sorted_positive.setObjectName(_fromUtf8("actionToggle_sorted_positive"))
        self.actionToggle_sorted_negative = QtGui.QAction(MainWindow)
        self.actionToggle_sorted_negative.setObjectName(_fromUtf8("actionToggle_sorted_negative"))
        self.menuActions.addAction(self.action_Initialize_from_current_folder)
        self.menuActions.addAction(self.actionToggleExtract)
        self.menuActions.addAction(self.actionToggleSort)
        self.menuActions.addAction(self.actionToggle_sort_negative)
        self.menuActions.addAction(self.action_Next_channel)
        self.menuActions.addAction(self.action_Previous_channel)
        self.menuActions.addAction(self.actionSave_actions_to_file)
        self.menuActions.addAction(self.actionToggle_sorted_positive)
        self.menuActions.addAction(self.actionToggle_sorted_negative)
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.labelLabel.setText(_translate("MainWindow", "Label for sorted sessions:", None))
        self.checkBoxInitH5.setText(_translate("MainWindow", "Initialize from h5-files", None))
        self.checkBoxSetStates.setText(_translate("MainWindow", "Set states upon initialization", None))
        self.menuActions.setTitle(_translate("MainWindow", "&Actions", None))
        self.action_Initialize_from_current_folder.setText(_translate("MainWindow", "&Initialize from current folder", None))
        self.action_Initialize_from_current_folder.setShortcut(_translate("MainWindow", "Ctrl+I", None))
        self.actionToggleExtract.setText(_translate("MainWindow", "Toggle &extract", None))
        self.actionToggleExtract.setShortcut(_translate("MainWindow", "E", None))
        self.actionToggleSort.setText(_translate("MainWindow", "Toggle sort &positive", None))
        self.actionToggleSort.setShortcut(_translate("MainWindow", "S", None))
        self.action_Next_channel.setText(_translate("MainWindow", "&Next channel", None))
        self.action_Next_channel.setShortcut(_translate("MainWindow", "Space", None))
        self.action_Previous_channel.setText(_translate("MainWindow", "&Previous channel", None))
        self.action_Previous_channel.setShortcut(_translate("MainWindow", "Shift+Up", None))
        self.actionSave_actions_to_file.setText(_translate("MainWindow", "Save &actions to file", None))
        self.actionOne_Down.setText(_translate("MainWindow", "One Down", None))
        self.actionOne_Down.setShortcut(_translate("MainWindow", "Shift+Down", None))
        self.actionToggle_sort_negative.setText(_translate("MainWindow", "Toggle sort &negative", None))
        self.actionToggle_sort_negative.setShortcut(_translate("MainWindow", "Shift+S", None))
        self.actionToggle_sorted_positive.setText(_translate("MainWindow", "Toggle sorted positive", None))
        self.actionToggle_sorted_positive.setShortcut(_translate("MainWindow", "M", None))
        self.actionToggle_sorted_negative.setText(_translate("MainWindow", "Toggle sorted negative", None))
        self.actionToggle_sorted_negative.setShortcut(_translate("MainWindow", "Shift+M", None))

