# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'converter.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import converter_functions

file_path = ""

def getConversionMode():
        if ui.convertOne.isChecked():
                conversionMode = 1

        elif ui.convertMany.isChecked():
                conversionMode = 2

        elif ui.convertDir.isChecked():
                conversionMode = 3

        else:
                conversionMode = -1

        return conversionMode



"""
Gets the selected input and output format. The fonction returns
an array with the following form [INPUT_FORMAT, OUTPUT_FORMAT]
"""
def formatToConvert():
        if ui.mp3TOwav.isChecked():
                return ("mp3","wav")
        elif ui.wavTOmp3.isChecked():
                return ("wav","mp3")
        elif ui.jpgTOpng.isChecked():
                return ("jpg","png")
        elif ui.pngTOjpg.isChecked():
                return ("png","jpg")
        elif ui.allTOpdf.isChecked():
                return ("all_images","pdf")
        elif ui.docTOpdf.isChecked():
                return ("doc","pdf")
        else:
                return ("","")



"""
Selects a conversion mode :
- Convert One File
- Convert Many Files
- Convert a full directory
"""
def browseFiles():
        global file_path
        conversionMode = getConversionMode()

        if conversionMode == 1:
                path = QFileDialog.getOpenFileName()
                ui.label_PATH.setText(path[0])
                file_path = path

        elif conversionMode == 2:
                path = QFileDialog.getOpenFileNames()
                ui.label_PATH.setText(path[0][0])
                file_path = path

        elif conversionMode == 3:
                path = QFileDialog.getExistingDirectory()
                ui.label_PATH.setText(path)
                file_path = path
        else:
                print("ERROR")
        

def launchConversion():
        conversionArray = formatToConvert();

        #Nothing is selected
        if (conversionArray[0] == ""):
                return

        print("INPUT : ", conversionArray[0],"\n")
        print("OUTPUT : ", conversionArray[1],"\n")
        

        #Checks if the input format is the correct one
        if converter_functions.checksInputFormat(file_path, getConversionMode(), conversionArray[0], conversionArray[1]) == False:
                print("INPUT ERROR")
                return

        converter_functions.convertFile(file_path, getConversionMode(), conversionArray[0], conversionArray[1])
        
                



        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Converter Alpha 0.1")
        MainWindow.resize(516, 854)
        MainWindow.setStyleSheet("background-color: rgb(173, 127, 168)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 231, 161))
        self.label_2.setStyleSheet("background-color: rgb(117, 80, 123)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.labelConversion = QtWidgets.QLabel(self.centralwidget)
        self.labelConversion.setGeometry(QtCore.QRect(20, 60, 231, 31))
        self.labelConversion.setStyleSheet("background-color: rgb(117, 80, 123);\n"
"color: rgb(255,255,255);")
        self.labelConversion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelConversion.setObjectName("labelConversion")
        self.convertOne = QtWidgets.QRadioButton(self.centralwidget)
        self.convertOne.setGeometry(QtCore.QRect(40, 100, 191, 31))
        self.convertOne.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convertOne.setStyleSheet("padding: 5px;\n"
"\n"
"border-radius: 5px;")
        self.convertOne.setObjectName("convertOne")
        self.convertMany = QtWidgets.QRadioButton(self.centralwidget)
        self.convertMany.setGeometry(QtCore.QRect(40, 140, 191, 31))
        self.convertMany.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convertMany.setStyleSheet("padding: 5px;\n"
"\n"
"border-radius: 5px;")
        self.convertMany.setObjectName("convertMany")
        self.convertDir = QtWidgets.QRadioButton(self.centralwidget)
        self.convertDir.setGeometry(QtCore.QRect(40, 180, 191, 31))
        self.convertDir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convertDir.setStyleSheet("padding: 5px;\n"
"\n"
"border-radius: 5px;")
        self.convertDir.setObjectName("convertDir")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 60, 231, 161))
        self.label_3.setStyleSheet("background-color: rgb(117, 80, 123)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_options = QtWidgets.QLabel(self.centralwidget)
        self.label_options.setGeometry(QtCore.QRect(270, 60, 231, 31))
        self.label_options.setStyleSheet("background-color: rgb(117, 80, 123);\n"
"color: rgb(255,255,255);")
        self.label_options.setAlignment(QtCore.Qt.AlignCenter)
        self.label_options.setObjectName("label_options")
        self.checkBoxZIP = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxZIP.setGeometry(QtCore.QRect(290, 100, 191, 31))
        self.checkBoxZIP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBoxZIP.setStyleSheet("padding: 5px;\n"
"padding-left: 5px;\n"
"\n"
"border-radius: 5px;\n"
"")
        self.checkBoxZIP.setObjectName("checkBoxZIP")
        self.checkBoxDEL = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxDEL.setGeometry(QtCore.QRect(290, 140, 191, 31))
        self.checkBoxDEL.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBoxDEL.setStyleSheet("padding: 5px;\n"
"padding-left: 5px;\n"
"\n"
"border-radius: 5px;\n"
"")
        self.checkBoxDEL.setObjectName("checkBoxDEL")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 280, 481, 81))
        self.label_6.setStyleSheet("background-color: rgb(117, 80, 123)")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_audiofiles = QtWidgets.QLabel(self.centralwidget)
        self.label_audiofiles.setGeometry(QtCore.QRect(20, 280, 481, 31))
        self.label_audiofiles.setStyleSheet("background-color: rgb(117, 80, 123);\n"
"color: rgb(255,255,255);")
        self.label_audiofiles.setAlignment(QtCore.Qt.AlignCenter)
        self.label_audiofiles.setObjectName("label_audiofiles")
        self.mp3TOwav = QtWidgets.QRadioButton(self.centralwidget)
        self.mp3TOwav.setGeometry(QtCore.QRect(40, 310, 191, 31))
        self.mp3TOwav.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mp3TOwav.setStyleSheet("padding: 5px;\n"
"\n"
"border-radius: 5px;")
        self.mp3TOwav.setObjectName("mp3TOwav")
        self.wavTOmp3 = QtWidgets.QRadioButton(self.centralwidget)
        self.wavTOmp3.setGeometry(QtCore.QRect(290, 310, 191, 31))
        self.wavTOmp3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wavTOmp3.setStyleSheet("padding: 5px;\n"
"\n"
"border-radius: 5px;")
        self.wavTOmp3.setObjectName("wavTOmp3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 370, 481, 121))
        self.label_7.setStyleSheet("background-color: rgb(117, 80, 123)")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.jpgTOpng = QtWidgets.QRadioButton(self.centralwidget)
        self.jpgTOpng.setGeometry(QtCore.QRect(40, 400, 191, 31))
        self.jpgTOpng.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.jpgTOpng.setStyleSheet("padding: 5px;\n"
"\n"
"border-radius: 5px;")
        self.jpgTOpng.setObjectName("jpgTOpng")
        self.label_imageFiles = QtWidgets.QLabel(self.centralwidget)
        self.label_imageFiles.setGeometry(QtCore.QRect(20, 370, 481, 31))
        self.label_imageFiles.setStyleSheet("background-color: rgb(117, 80, 123);\n"
"color: rgb(255,255,255);")
        self.label_imageFiles.setAlignment(QtCore.Qt.AlignCenter)
        self.label_imageFiles.setObjectName("label_imageFiles")
        self.pngTOjpg = QtWidgets.QRadioButton(self.centralwidget)
        self.pngTOjpg.setGeometry(QtCore.QRect(290, 400, 191, 31))
        self.pngTOjpg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pngTOjpg.setStyleSheet("padding: 5px;\n"
"\n"
"border-radius: 5px;")
        self.pngTOjpg.setObjectName("pngTOjpg")
        self.label_STEP2 = QtWidgets.QLabel(self.centralwidget)
        self.label_STEP2.setGeometry(QtCore.QRect(20, 220, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_STEP2.setFont(font)
        self.label_STEP2.setStyleSheet("background-color: rgb(173, 127, 168);\n"
"color: rgb(255,255,255);")
        self.label_STEP2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_STEP2.setObjectName("label_STEP2")
        self.label_STEP1 = QtWidgets.QLabel(self.centralwidget)
        self.label_STEP1.setGeometry(QtCore.QRect(20, 0, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_STEP1.setFont(font)
        self.label_STEP1.setStyleSheet("background-color: rgb(173, 127, 168);\n"
"color: rgb(255,255,255);")
        self.label_STEP1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_STEP1.setObjectName("label_STEP1")
        self.allTOpdf = QtWidgets.QRadioButton(self.centralwidget)
        self.allTOpdf.setGeometry(QtCore.QRect(40, 440, 191, 31))
        self.allTOpdf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.allTOpdf.setStyleSheet("padding: 5px;\n"
"\n"
"border-radius: 5px;")
        self.allTOpdf.setObjectName("allTOpdf")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 500, 481, 81))
        self.label_11.setStyleSheet("background-color: rgb(117, 80, 123)")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_textFiles = QtWidgets.QLabel(self.centralwidget)
        self.label_textFiles.setGeometry(QtCore.QRect(20, 500, 481, 31))
        self.label_textFiles.setStyleSheet("background-color: rgb(117, 80, 123);\n"
"color: rgb(255,255,255);")
        self.label_textFiles.setAlignment(QtCore.Qt.AlignCenter)
        self.label_textFiles.setObjectName("label_textFiles")
        self.docTOpdf = QtWidgets.QRadioButton(self.centralwidget)
        self.docTOpdf.setGeometry(QtCore.QRect(40, 530, 191, 31))
        self.docTOpdf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.docTOpdf.setStyleSheet("padding: 5px;\n"
"\n"
"border-radius: 5px;")
        self.docTOpdf.setObjectName("docTOpdf")
        self.label_STEP4 = QtWidgets.QLabel(self.centralwidget)
        self.label_STEP4.setGeometry(QtCore.QRect(20, 710, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_STEP4.setFont(font)
        self.label_STEP4.setStyleSheet("background-color: rgb(173, 127, 168);\n"
"color: rgb(255,255,255);")
        self.label_STEP4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_STEP4.setObjectName("label_STEP4")
        self.pushButton_LAUNCH = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LAUNCH.setGeometry(QtCore.QRect(20, 760, 481, 41))
        self.pushButton_LAUNCH.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_LAUNCH.setStyleSheet("background-color: rgb(117, 80, 123);\n"
"color: rgb(255,255,255);\n"
"border: 2px solid rgb(46, 52, 54);\n"
"border-radius: 5px;")
        self.pushButton_LAUNCH.setObjectName("pushButton_LAUNCH")
        self.label_STEP3 = QtWidgets.QLabel(self.centralwidget)
        self.label_STEP3.setGeometry(QtCore.QRect(20, 580, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_STEP3.setFont(font)
        self.label_STEP3.setStyleSheet("background-color: rgb(173, 127, 168);\n"
"color: rgb(255,255,255);")
        self.label_STEP3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_STEP3.setObjectName("label_STEP3")
        self.pushButton_LOCATE = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LOCATE.setGeometry(QtCore.QRect(150, 630, 231, 41))
        self.pushButton_LOCATE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_LOCATE.setStyleSheet("background-color: rgb(117, 80, 123);\n"
"color: rgb(255,255,255);\n"
"border: 2px solid rgb(46, 52, 54);\n"
"border-radius: 5px;")
        self.pushButton_LOCATE.setObjectName("pushButton_LOCATE")
        self.label_PATH = QtWidgets.QLabel(self.centralwidget)
        self.label_PATH.setGeometry(QtCore.QRect(20, 680, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_PATH.setFont(font)
        self.label_PATH.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_PATH.setStyleSheet("background-color: rgb(117, 80, 123);\n"
"color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"\n"
"padding-left: 10px;")
        self.label_PATH.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_PATH.setObjectName("label_PATH")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 22))
        self.menubar.setStyleSheet("background-color: rgb(117, 80, 123);\n"
"color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionShow_help = QtWidgets.QAction(MainWindow)
        self.actionShow_help.setObjectName("actionShow_help")
        self.menuAide.addAction(self.actionShow_help)
        self.menubar.addAction(self.menuAide.menuAction())

        #Links between first three radio buttons
        self.conversionMode = QtWidgets.QButtonGroup()
        self.conversionMode.addButton(self.convertOne)
        self.conversionMode.addButton(self.convertMany)
        self.conversionMode.addButton(self.convertDir)

        #self.conversionMode.buttonClicked[int].connect(toggleConversionMode)
        
        self.formatToConvert = QtWidgets.QButtonGroup()
        self.formatToConvert.addButton(self.mp3TOwav)
        self.formatToConvert.addButton(self.wavTOmp3)
        self.formatToConvert.addButton(self.jpgTOpng)
        self.formatToConvert.addButton(self.pngTOjpg)
        self.formatToConvert.addButton(self.allTOpdf)
        self.formatToConvert.addButton(self.docTOpdf)

        #self.formatToConvert.buttonClicked[int].connect(formatToConvert)
        
        #Locate file(s)
        self.pushButton_LOCATE.clicked.connect(browseFiles)

        #Starts the conversion
        self.pushButton_LAUNCH.clicked.connect(launchConversion)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Converter Alpha 0.1"))
        self.labelConversion.setText(_translate("MainWindow", "Conversion mode"))
        self.convertOne.setText(_translate("MainWindow", "Convert one file"))
        self.convertMany.setText(_translate("MainWindow", "Convert several files"))
        self.convertDir.setText(_translate("MainWindow", "Convert a full directory"))
        self.label_options.setText(_translate("MainWindow", "Optional settings"))
        self.checkBoxZIP.setText(_translate("MainWindow", "Zip files once converted"))
        self.checkBoxDEL.setText(_translate("MainWindow", "Delete input files"))
        self.label_audiofiles.setText(_translate("MainWindow", "Audio files"))
        self.mp3TOwav.setText(_translate("MainWindow", "MP3 -> WAV"))
        self.wavTOmp3.setText(_translate("MainWindow", "WAV -> MP3"))
        self.jpgTOpng.setText(_translate("MainWindow", "JPG -> PNG"))
        self.label_imageFiles.setText(_translate("MainWindow", "Image files"))
        self.pngTOjpg.setText(_translate("MainWindow", "PNG -> JPG"))
        self.label_STEP2.setText(_translate("MainWindow", "2. Choose which output you want"))
        self.label_STEP1.setText(_translate("MainWindow", "1. Choose a Conversion mode"))
        self.allTOpdf.setText(_translate("MainWindow", "PNG / JPG -> PDF"))
        self.label_textFiles.setText(_translate("MainWindow", "Text files (Windows only)"))
        self.docTOpdf.setText(_translate("MainWindow", "DOCX / DOC -> PDF"))
        self.label_STEP4.setText(_translate("MainWindow", "4. Convert"))
        self.pushButton_LAUNCH.setText(_translate("MainWindow", "Launch Conversion"))
        self.label_STEP3.setText(_translate("MainWindow", "3. Mark the location of your file(s)"))
        self.pushButton_LOCATE.setText(_translate("MainWindow", "Locate file(s)"))
        self.label_PATH.setText(_translate("MainWindow", "..."))
        self.menuAide.setTitle(_translate("MainWindow", "&Help"))
        self.actionShow_help.setText(_translate("MainWindow", "Show help"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConverterProg = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(ConverterProg)
    ConverterProg.show()
    sys.exit(app.exec_())