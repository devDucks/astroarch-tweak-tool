# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tweakastroarch.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 400)
        Form.setMaximumSize(QSize(750, 400))
        icon = QIcon()
        icon.addFile(u"astroarch-w-32x32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_gps = QLabel(Form)
        self.lb_gps.setObjectName(u"lb_gps")
        self.lb_gps.setMaximumSize(QSize(150, 40))
        self.lb_gps.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lb_gps.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lb_gps)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.rb_gps_off = QRadioButton(Form)
        self.btn_g_gps = QButtonGroup(Form)
        self.btn_g_gps.setObjectName(u"btn_g_gps")
        self.btn_g_gps.addButton(self.rb_gps_off)
        self.rb_gps_off.setObjectName(u"rb_gps_off")
        self.rb_gps_off.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_3.addWidget(self.rb_gps_off)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.rb_gps_on = QRadioButton(Form)
        self.btn_g_gps.addButton(self.rb_gps_on)
        self.rb_gps_on.setObjectName(u"rb_gps_on")
        self.rb_gps_on.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_3.addWidget(self.rb_gps_on)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.rb_gps_on_ublox = QRadioButton(Form)
        self.btn_g_gps.addButton(self.rb_gps_on_ublox)
        self.rb_gps_on_ublox.setObjectName(u"rb_gps_on_ublox")
        self.rb_gps_on_ublox.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_3.addWidget(self.rb_gps_on_ublox)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.lb_gps_error = QLabel(Form)
        self.lb_gps_error.setObjectName(u"lb_gps_error")
        self.lb_gps_error.setMaximumSize(QSize(150, 40))
        self.lb_gps_error.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lb_gps_error)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"astroarch-w-120x120.png"))

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_update = QLabel(Form)
        self.lb_update.setObjectName(u"lb_update")
        self.lb_update.setMaximumSize(QSize(150, 40))
        self.lb_update.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lb_update.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lb_update.setIndent(-1)

        self.horizontalLayout_2.addWidget(self.lb_update)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.btn_update = QPushButton(Form)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_2.addWidget(self.btn_update)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_18)

        self.lb_update_error = QLabel(Form)
        self.lb_update_error.setObjectName(u"lb_update_error")

        self.horizontalLayout_2.addWidget(self.lb_update_error)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_17)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.horizontalLayout_6.addWidget(self.label_7)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_ftp = QLabel(Form)
        self.lb_ftp.setObjectName(u"lb_ftp")
        self.lb_ftp.setMaximumSize(QSize(150, 40))
        self.lb_ftp.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lb_ftp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lb_ftp.setWordWrap(False)

        self.horizontalLayout_5.addWidget(self.lb_ftp)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)

        self.rb_ftp_off = QRadioButton(Form)
        self.btn_g_ftp = QButtonGroup(Form)
        self.btn_g_ftp.setObjectName(u"btn_g_ftp")
        self.btn_g_ftp.addButton(self.rb_ftp_off)
        self.rb_ftp_off.setObjectName(u"rb_ftp_off")
        self.rb_ftp_off.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_5.addWidget(self.rb_ftp_off)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)

        self.rb_ftp_on = QRadioButton(Form)
        self.btn_g_ftp.addButton(self.rb_ftp_on)
        self.rb_ftp_on.setObjectName(u"rb_ftp_on")
        self.rb_ftp_on.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_5.addWidget(self.rb_ftp_on)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_5.addWidget(self.label_9)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_13)

        self.lb_ftp_error = QLabel(Form)
        self.lb_ftp_error.setObjectName(u"lb_ftp_error")
        self.lb_ftp_error.setMaximumSize(QSize(150, 40))
        self.lb_ftp_error.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lb_ftp_error)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_bluetooh = QLabel(Form)
        self.lb_bluetooh.setObjectName(u"lb_bluetooh")
        self.lb_bluetooh.setMaximumSize(QSize(150, 40))
        self.lb_bluetooh.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lb_bluetooh.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lb_bluetooh)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.rb_blue_off = QRadioButton(Form)
        self.btn_g_blue = QButtonGroup(Form)
        self.btn_g_blue.setObjectName(u"btn_g_blue")
        self.btn_g_blue.addButton(self.rb_blue_off)
        self.rb_blue_off.setObjectName(u"rb_blue_off")
        self.rb_blue_off.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_4.addWidget(self.rb_blue_off)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.rb_blue_on = QRadioButton(Form)
        self.btn_g_blue.addButton(self.rb_blue_on)
        self.rb_blue_on.setObjectName(u"rb_blue_on")
        self.rb_blue_on.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_4.addWidget(self.rb_blue_on)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(150, 40))

        self.horizontalLayout_4.addWidget(self.label_8)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.lb_blue_error = QLabel(Form)
        self.lb_blue_error.setObjectName(u"lb_blue_error")
        self.lb_blue_error.setMaximumSize(QSize(150, 40))
        self.lb_blue_error.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lb_blue_error)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Tweak AstroArch", None))
        self.lb_gps.setText(QCoreApplication.translate("Form", u"GPS", None))
        self.rb_gps_off.setText(QCoreApplication.translate("Form", u"Off", None))
        self.rb_gps_on.setText(QCoreApplication.translate("Form", u"O&n", None))
        self.rb_gps_on_ublox.setText(QCoreApplication.translate("Form", u"On (&U-Blox 7)", None))
        self.lb_gps_error.setText("")
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Tweak AstroArch", None))
        self.lb_update.setText(QCoreApplication.translate("Form", u"Update AstroArch", None))
        self.btn_update.setText(QCoreApplication.translate("Form", u"Update", None))
        self.lb_update_error.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Need help or have a question find us on discord or the <a href=\"https://www.indilib.org/forum/astro-arch.html\"><span style=\" text-decoration: underline; color:#1d99f3;\">Indi forum</span></a> and of course <a href=\"https://github.com/devDucks/astroarch\"><span style=\" text-decoration: underline; color:#1d99f3;\">github</span></a></p></body></html>", None))
        self.lb_ftp.setText(QCoreApplication.translate("Form", u"FTP", None))
        self.rb_ftp_off.setText(QCoreApplication.translate("Form", u"Off", None))
        self.rb_ftp_on.setText(QCoreApplication.translate("Form", u"On", None))
        self.label_9.setText("")
        self.lb_ftp_error.setText("")
        self.lb_bluetooh.setText(QCoreApplication.translate("Form", u"Bluetooh", None))
        self.rb_blue_off.setText(QCoreApplication.translate("Form", u"Off", None))
        self.rb_blue_on.setText(QCoreApplication.translate("Form", u"On", None))
        self.label_8.setText("")
        self.lb_blue_error.setText("")
    # retranslateUi

