# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/TreeVisualizer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Design\\../Resources/TreeIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.OptionFrame = QtWidgets.QFrame(self.centralwidget)
        self.OptionFrame.setMinimumSize(QtCore.QSize(1000, 140))
        self.OptionFrame.setMaximumSize(QtCore.QSize(16777215, 140))
        self.OptionFrame.setStyleSheet("QFrame{\n"
"    background-color: rgb(26, 29, 34);\n"
"}")
        self.OptionFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OptionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OptionFrame.setObjectName("OptionFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.OptionFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.OptionFrame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LeftSide = QtWidgets.QWidget(self.widget)
        self.LeftSide.setMinimumSize(QtCore.QSize(380, 140))
        self.LeftSide.setObjectName("LeftSide")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.LeftSide)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.V1 = QtWidgets.QVBoxLayout()
        self.V1.setObjectName("V1")
        self.H1 = QtWidgets.QHBoxLayout()
        self.H1.setObjectName("H1")
        self.ParentLabel = QtWidgets.QLabel(self.LeftSide)
        self.ParentLabel.setMinimumSize(QtCore.QSize(120, 30))
        self.ParentLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.ParentLabel.setFont(font)
        self.ParentLabel.setStyleSheet("QLabel{\n"
"    color: rgb(191, 207, 231);\n"
"}")
        self.ParentLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ParentLabel.setObjectName("ParentLabel")
        self.H1.addWidget(self.ParentLabel)
        self.ParentField = QtWidgets.QLineEdit(self.LeftSide)
        self.ParentField.setMinimumSize(QtCore.QSize(120, 30))
        self.ParentField.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.ParentField.setFont(font)
        self.ParentField.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: rgb(34,36,44);\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"    border: 2px solid rgb(85,170,255);\n"
"    background-color: rgb(43,45,56);\n"
"}")
        self.ParentField.setObjectName("ParentField")
        self.H1.addWidget(self.ParentField)
        self.V1.addLayout(self.H1)
        self.H2 = QtWidgets.QHBoxLayout()
        self.H2.setObjectName("H2")
        self.ChildLabel = QtWidgets.QLabel(self.LeftSide)
        self.ChildLabel.setMinimumSize(QtCore.QSize(120, 30))
        self.ChildLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.ChildLabel.setFont(font)
        self.ChildLabel.setStyleSheet("QLabel{\n"
"    color: rgb(191, 207, 231);\n"
"}")
        self.ChildLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ChildLabel.setObjectName("ChildLabel")
        self.H2.addWidget(self.ChildLabel)
        self.ChildField = QtWidgets.QLineEdit(self.LeftSide)
        self.ChildField.setMinimumSize(QtCore.QSize(120, 30))
        self.ChildField.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.ChildField.setFont(font)
        self.ChildField.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color: rgb(34,36,44);\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"    border: 2px solid rgb(85,170,255);\n"
"    background-color: rgb(43,45,56);\n"
"}")
        self.ChildField.setObjectName("ChildField")
        self.H2.addWidget(self.ChildField)
        self.V1.addLayout(self.H2)
        self.H3 = QtWidgets.QHBoxLayout()
        self.H3.setObjectName("H3")
        self.ChildTypeLabel = QtWidgets.QLabel(self.LeftSide)
        self.ChildTypeLabel.setMinimumSize(QtCore.QSize(120, 30))
        self.ChildTypeLabel.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.ChildTypeLabel.setFont(font)
        self.ChildTypeLabel.setStyleSheet("QLabel{\n"
"    color: rgb(191, 207, 231);\n"
"}")
        self.ChildTypeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ChildTypeLabel.setObjectName("ChildTypeLabel")
        self.H3.addWidget(self.ChildTypeLabel)
        self.LeftButton = QtWidgets.QPushButton(self.LeftSide)
        self.LeftButton.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.LeftButton.setFont(font)
        self.LeftButton.setStyleSheet("QPushButton{\n"
"    color: #FFF;\n"
"    background-color: #198754;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #157347;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border: 4px solid #9dccb6;\n"
"}")
        self.LeftButton.setObjectName("LeftButton")
        self.H3.addWidget(self.LeftButton)
        self.RightButton = QtWidgets.QPushButton(self.LeftSide)
        self.RightButton.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.RightButton.setFont(font)
        self.RightButton.setStyleSheet("QPushButton{\n"
"    color: #FFF;\n"
"    background-color: #198754;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #157347;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border: 4px solid #9dccb6;\n"
"}")
        self.RightButton.setObjectName("RightButton")
        self.H3.addWidget(self.RightButton)
        self.V1.addLayout(self.H3)
        self.horizontalLayout_2.addLayout(self.V1)
        self.horizontalLayout_3.addWidget(self.LeftSide)
        self.VL = QtWidgets.QWidget(self.widget)
        self.VL.setObjectName("VL")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.VL)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.V2 = QtWidgets.QVBoxLayout()
        self.V2.setObjectName("V2")
        self.H4 = QtWidgets.QHBoxLayout()
        self.H4.setSpacing(10)
        self.H4.setObjectName("H4")
        self.PreButton = QtWidgets.QPushButton(self.VL)
        self.PreButton.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.PreButton.setFont(font)
        self.PreButton.setStyleSheet("QPushButton{\n"
"    color: #FFF;\n"
"    background-color: #198754;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #157347;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border: 4px solid #9dccb6;\n"
"}")
        self.PreButton.setObjectName("PreButton")
        self.H4.addWidget(self.PreButton)
        self.InButton = QtWidgets.QPushButton(self.VL)
        self.InButton.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.InButton.setFont(font)
        self.InButton.setStyleSheet("QPushButton{\n"
"    color: #FFF;\n"
"    background-color: #198754;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #157347;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border: 4px solid #9dccb6;\n"
"}")
        self.InButton.setObjectName("InButton")
        self.H4.addWidget(self.InButton)
        self.PostButton = QtWidgets.QPushButton(self.VL)
        self.PostButton.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.PostButton.setFont(font)
        self.PostButton.setStyleSheet("QPushButton{\n"
"    color: #FFF;\n"
"    background-color: #198754;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #157347;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border: 4px solid #9dccb6;\n"
"}")
        self.PostButton.setObjectName("PostButton")
        self.H4.addWidget(self.PostButton)
        self.V2.addLayout(self.H4)
        self.ResultLabel = QtWidgets.QLabel(self.VL)
        self.ResultLabel.setMinimumSize(QtCore.QSize(600, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.ResultLabel.setFont(font)
        self.ResultLabel.setStyleSheet("QLabel{\n"
"    color: rgb(191, 207, 231);\n"
"}")
        self.ResultLabel.setObjectName("ResultLabel")
        self.V2.addWidget(self.ResultLabel)
        self.verticalLayout_2.addLayout(self.V2)
        self.horizontalLayout_3.addWidget(self.VL)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout.addWidget(self.OptionFrame)
        self.TreeViewFrame = QtWidgets.QFrame(self.centralwidget)
        self.TreeViewFrame.setMinimumSize(QtCore.QSize(1000, 460))
        self.TreeViewFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TreeViewFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TreeViewFrame.setObjectName("TreeViewFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.TreeViewFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.DisplayTree = QtWidgets.QWidget(self.TreeViewFrame)
        self.DisplayTree.setObjectName("DisplayTree")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.DisplayTree)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.TreeView = QtWidgets.QGraphicsView(self.DisplayTree)
        self.TreeView.setStyleSheet("QGraphicsView{\n"
"    background-color: rgb(26, 29, 34);\n"
"    border: 0px;\n"
"}")
        self.TreeView.setObjectName("TreeView")
        self.horizontalLayout_5.addWidget(self.TreeView)
        self.horizontalLayout_4.addWidget(self.DisplayTree)
        self.verticalLayout.addWidget(self.TreeViewFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tree Visualizer By MahtabulShourav"))
        self.ParentLabel.setText(_translate("MainWindow", "Parent Node:"))
        self.ParentField.setPlaceholderText(_translate("MainWindow", "Add Parent"))
        self.ChildLabel.setText(_translate("MainWindow", "Child->Node:"))
        self.ChildField.setPlaceholderText(_translate("MainWindow", "Add Child"))
        self.ChildTypeLabel.setText(_translate("MainWindow", "Child->Type: "))
        self.LeftButton.setText(_translate("MainWindow", "Left"))
        self.RightButton.setText(_translate("MainWindow", "Right"))
        self.PreButton.setText(_translate("MainWindow", "Pre-Order"))
        self.InButton.setText(_translate("MainWindow", "In-Order"))
        self.PostButton.setText(_translate("MainWindow", "Post-Order"))
        self.ResultLabel.setText(_translate("MainWindow", "Traversal Result:"))
