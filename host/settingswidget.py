# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingswidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SForm(object):
    def setupUi(self, SForm):
        SForm.setObjectName("SForm")
        SForm.resize(480, 740)
        self.verticalLayoutWidget = QtWidgets.QWidget(SForm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 481, 661))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setObjectName("widget")
        self.EnableEndPoints = QtWidgets.QToolButton(self.widget)
        self.EnableEndPoints.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.EnableEndPoints.setText("")
        self.EnableEndPoints.setCheckable(True)
        self.EnableEndPoints.setObjectName("EnableEndPoints")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(60, 15, 400, 20))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_3.setObjectName("widget_3")
        self.EndPointsStop = QtWidgets.QToolButton(self.widget_3)
        self.EndPointsStop.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.EndPointsStop.setText("")
        self.EndPointsStop.setCheckable(True)
        self.EndPointsStop.setObjectName("EndPointsStop")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(60, 15, 400, 20))
        self.label_3.setObjectName("label_3")
        self.widget_9 = QtWidgets.QWidget(self.widget_3)
        self.widget_9.setGeometry(QtCore.QRect(248, 0, 521, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_9.setObjectName("widget_9")
        self.EndPointsReverse = QtWidgets.QToolButton(self.widget_9)
        self.EndPointsReverse.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.EndPointsReverse.setText("")
        self.EndPointsReverse.setCheckable(True)
        self.EndPointsReverse.setObjectName("EndPointsReverse")
        self.label_9 = QtWidgets.QLabel(self.widget_9)
        self.label_9.setGeometry(QtCore.QRect(60, 15, 400, 20))
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_5 = QtWidgets.QWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_5.setObjectName("widget_5")
        self.SoundStop = QtWidgets.QToolButton(self.widget_5)
        self.SoundStop.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.SoundStop.setText("")
        self.SoundStop.setCheckable(True)
        self.SoundStop.setObjectName("SoundStop")
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setGeometry(QtCore.QRect(60, 15, 400, 20))
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_4 = QtWidgets.QWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_4.setObjectName("widget_4")
        self.SwapDirection = QtWidgets.QToolButton(self.widget_4)
        self.SwapDirection.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.SwapDirection.setText("")
        self.SwapDirection.setCheckable(True)
        self.SwapDirection.setObjectName("SwapDirection")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(60, 15, 400, 20))
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_2.setObjectName("widget_2")
        self.StopAccelerometer = QtWidgets.QToolButton(self.widget_2)
        self.StopAccelerometer.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.StopAccelerometer.setText("")
        self.StopAccelerometer.setCheckable(True)
        self.StopAccelerometer.setObjectName("StopAccelerometer")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(60, 15, 400, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_8 = QtWidgets.QWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_8.setObjectName("widget_8")
        self.LockButtons = QtWidgets.QToolButton(self.widget_8)
        self.LockButtons.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.LockButtons.setText("")
        self.LockButtons.setCheckable(True)
        self.LockButtons.setObjectName("LockButtons")
        self.label_8 = QtWidgets.QLabel(self.widget_8)
        self.label_8.setGeometry(QtCore.QRect(60, 15, 400, 20))
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.widget_8)
        self.horizontalLayoutWidget = QtWidgets.QWidget(SForm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 660, 481, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_7 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_7.setObjectName("widget_7")
        self.toolButton_7 = QtWidgets.QToolButton(self.widget_7)
        self.toolButton_7.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.toolButton_7.setObjectName("toolButton_7")
        self.label_7 = QtWidgets.QLabel(self.widget_7)
        self.label_7.setGeometry(QtCore.QRect(50, 15, 420, 20))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_6.setObjectName("widget_6")
        self.toolButton_6 = QtWidgets.QToolButton(self.widget_6)
        self.toolButton_6.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.toolButton_6.setObjectName("toolButton_6")
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        self.label_6.setGeometry(QtCore.QRect(50, 15, 420, 20))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.widget_6)

        self.retranslateUi(SForm)
        QtCore.QMetaObject.connectSlotsByName(SForm)

    def retranslateUi(self, SForm):
        _translate = QtCore.QCoreApplication.translate
        SForm.setWindowTitle(_translate("SForm", "Form"))
        self.label.setText(_translate("SForm", "ВКЛ/ВЫКЛ КОНЕЧНЫЕ ТОЧКИ"))
        self.label_3.setText(_translate("SForm", "ОСТАНОВ В КОН. ТОЧКАХ"))
        self.label_9.setText(_translate("SForm", "РЕВЕРС В КОН. ТОЧКАХ"))
        self.label_5.setText(_translate("SForm", "СТОП ПО УЗ ДАТЧИКУ"))
        self.label_4.setText(_translate("SForm", "СМЕНА НАПРАВЛЕНИЯ"))
        self.label_2.setText(_translate("SForm", "СТОП ПО УДАРУ"))
        self.label_8.setText(_translate("SForm", "ЗАБЛОКИРОВАТЬ КНОПКИ"))
        self.toolButton_7.setText(_translate("SForm", "..."))
        self.label_7.setText(_translate("SForm", "База 1"))
        self.toolButton_6.setText(_translate("SForm", "..."))
        self.label_6.setText(_translate("SForm", "База 2"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SForm = QtWidgets.QWidget()
    ui = Ui_SForm()
    ui.setupUi(SForm)
    SForm.show()
    sys.exit(app.exec_())
