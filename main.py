from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
import sys, os
import design
from GPA import Gpa

class GPAApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(GPAApp, self).__init__(parent)
        self.setupUi(self)
        self.label_3.hide()
        self.vCodeEdit.hide()
        self.gpa = Gpa()
        self.getVCode.clicked.connect(self.on_get_vcode_clicked)
        self.login.clicked.connect(self.on_login_clicked)
        self.getGpa.clicked.connect(self.on_get_gpa_clicked)
        self.openGradeFile.clicked.connect(self.on_open_grade_file_clicked)

    def on_get_vcode_clicked(self):
        if self.usernameEdit.text() and self.pwdEdit.text():
            self.gpa.getIndexHtml()
            self.gpa.getVerifyCodePic()
            os.system('open vCode.png')
            self.label_3.show()
            self.vCodeEdit.show()

    def on_login_clicked(self):
        if self.vCodeEdit.text():
            self.gpa.getVerifyCode(self.vCodeEdit.text())
            try:
                self.gpa.login(self.usernameEdit.text(), self.pwdEdit.text())
            except Exception as e:
                QtWidgets.QMessageBox.information(self, "Title", e)
            # vPic = QPixmap(r'/Users/Seagullbird/Desktop/Codes/Python/GPA/vCode.png')
            # if vPic.isNull(): 
            #     print('vCode image unloaded')
            # self.label.setScaledContents(True)
            # self.label.setPixmap(vPic)
            # self.label.show()

    def on_get_gpa_clicked(self):
        self.gpa.getGradePage()
        self.gpa.getGradeTable()
        self.gpa.calcGpa()
        self.gpaLabel.setText('Gpa: %.2f' % self.gpa.gpa)

    def on_open_grade_file_clicked(self):
        os.system('open allGrade.html -a /Applications/Safari.app')

def main():
	app = QtWidgets.QApplication(sys.argv)
	form = GPAApp()
	form.show()
	app.exec_()




if __name__ == '__main__':
    main()