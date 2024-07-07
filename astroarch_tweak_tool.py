import sys
import os
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QFile, QTimer
from ui_astroarch_tweak_tool import  Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        
        super(MainWindow, self).__init__()
        self.ui =  Ui_Form()
        self.ui.setupUi(self)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.status)
        self.timer.start(1000)

        # call function on clicked button and radio button
        self.ui.btn_update.clicked.connect(self.btn_update_action)
        self.ui.rb_gps_off.clicked.connect(self.rb_gps_off_action)
        self.ui.rb_gps_on.clicked.connect(self.rb_gps_on_action)
        self.ui.rb_gps_on_ublox.clicked.connect(self.rb_gps_on_ublox_action)
        self.ui.rb_blue_off.clicked.connect(self.rb_blue_off_action)
        self.ui.rb_blue_on.clicked.connect(self.rb_blue_on_action)
        self.ui.rb_ftp_off.clicked.connect(self.rb_ftp_off_action)
        self.ui.rb_ftp_on.clicked.connect(self.rb_ftp_on_action)

    def btn_update_action(self):
        self.ui.lb_update_error.setText("")
        print("update")
        cmd = "konsole -e '/bin/zsh -i -c \"update-astroarch\"'"
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, errors = proc.communicate()
        if proc.returncode or errors:
            self.ui.lb_update_error.setText("update error")
            self.ui.lb_update_error.setStyleSheet("color:red")
            print("error")
        else:
            print("ok")

    def rb_gps_off_action(self):
        self.ui.lb_gps_error.setText("")
        print("gps off")
        cmd = "konsole -e '/bin/zsh -i -c \"gps_off\"'"
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, errors = proc.communicate()
        if proc.returncode or errors:
            print("error")
        else:
            print("ok")

    def rb_gps_on_action(self):
        self.ui.lb_gps_error.setText("")
        print("gps on")
        cmd = "konsole -e '/bin/zsh -i -c \"gps_on\"'"
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, errors = proc.communicate()
        if proc.returncode or errors:
            self.ui.lb_gps_error.setText("gps error")
            self.ui.lb_gps_error.setStyleSheet("color:red")
            print("error")
        else:
            print("ok")

    def rb_gps_on_ublox_action(self):
        self.ui.lb_gps_error.setText("")
        print("gps on ublox")
        cmd = "konsole -e '/bin/zsh -i -c \"gps_ublox_on\"'"
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)        
        output, errors = proc.communicate()
        if proc.returncode or errors:
            self.ui.lb_gps_error.setText("gps ublox error")
            self.ui.lb_gps_error.setStyleSheet("color:red")
            print("error")
        else:
            print("ok")

    def rb_blue_off_action(self):
        self.ui.lb_blue_error.setText("")
        print("Bluetooh off")
        cmd = "konsole -e '/bin/zsh -i -c \"bluetooth_off\"'"
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, errors = proc.communicate()
        if proc.returncode or errors:
            print("error")
        else:
            print("ok")

    def rb_blue_on_action(self):
        self.ui.lb_blue_error.setText("")
        print("Bluetooh on")
        cmd = "konsole -e '/bin/zsh -i -c \"bluetooth_on\"'"
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, errors = proc.communicate()
        if proc.returncode or errors:
            self.ui.lb_blue_error.setText("bluetooth error")
            self.ui.lb_blue_error.setStyleSheet("color:red")
            print("error")
        else:
            print("ok")

    def rb_ftp_off_action(self):
        self.ui.lb_ftp_error.setText("")
        print("FTP off")
        cmd = "konsole -e '/bin/zsh -i -c \"ftp_off\"'"
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, errors = proc.communicate()
        if proc.returncode or errors:
            print("error")
        else:
            print("ok")

    def rb_ftp_on_action(self):
        self.ui.lb_ftp_error.setText("")
        print("FTP on")
        cmd = "konsole -e '/bin/zsh -i -c \"ftp_on\"'"
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, errors = proc.communicate()
        if proc.returncode or errors:
            self.ui.lb_ftp_error.setText("ftp error")
            self.ui.lb_ftp_error.setStyleSheet("color:red")
            print("error")
        else:
            print("ok")


    def status(self):
        # services status
        gps_status = os.system('systemctl is-active gpsd')
        bluetooh_status = os.system('systemctl is-active bluetooth')
        ftp_status = os.system('systemctl is-active vsftpd')

        # set radio button gps
        with open('/etc/default/gpsd') as gpsd_file:
            file = gpsd_file.readlines()
            for line in file:
                if line.find('ttyACM0') != -1 and gps_status == 0:
                    self.ui.rb_gps_on_ublox.setChecked(True)
                    self.ui.lb_gps.setStyleSheet("color: green;")
                elif line.find('gps0') != -1 and gps_status == 0:
                    self.ui.rb_gps_on.setChecked(True)
                    self.ui.lb_gps.setStyleSheet("color: green;")   
        if gps_status == 768:
            self.ui.rb_gps_off.setChecked(True)
            self.ui.lb_gps.setStyleSheet("color: red;")

        # set radio button bluetooh
        if bluetooh_status == 0:
            self.ui.rb_blue_on.setChecked(True)
            self.ui.lb_bluetooh.setStyleSheet("color: green;")
        else:
            self.ui.rb_blue_off.setChecked(True)
            self.ui.lb_bluetooh.setStyleSheet("color: red;")

        # set radio button ftp
        if ftp_status == 0:
            self.ui.rb_ftp_on.setChecked(True)
            self.ui.lb_ftp.setStyleSheet("color: green;")
        else:
            self.ui.rb_ftp_off.setChecked(True)
            self.ui.lb_ftp.setStyleSheet("color: red;")

            
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
