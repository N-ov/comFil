from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os
import googleapiclient.discovery
import google_auth_oauthlib.flow
import googleapiclient.errors
import time
import threading


def start(args):
    filter = Filter()
    function = filter.startFilter
    thread = threading.Thread(target=function, args=(args,))
    thread.start()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(558, 292)
        Dialog.setFixedSize(558, 292)
        Dialog.setStyleSheet("background-color: rgb(50, 76, 128);")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 571, 291))
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
                                     "    border: 1px;\n"
                                     "    background: rgb(35,40,49);\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab {\n"
                                     "    background: rgb(70, 94, 140);\n"
                                     "    min-width: 37.5ex;\n"
                                     "    min-height: 8ex;\n"
                                     "    margin-left: 0px;\n"
                                     "    left: -1px;\n"
                                     "    color:white;\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:selected {\n"
                                     "    background: rgb(39, 59, 99);\n"
                                     "}\n"
                                     "QTabBar::tab:hover {\n"
                                     "    background:rgb(50, 72, 115)\n"
                                     "}")
        self.tabWidget.setObjectName("tabWidget")
        self.Main = QtWidgets.QWidget()
        self.Main.setObjectName("Main")
        self.label = QtWidgets.QLabel(self.Main)
        self.label.setGeometry(QtCore.QRect(0, 70, 561, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.Main)
        self.pushButton.setGeometry(QtCore.QRect(180, 130, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border:transparent;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(50, 72, 115);")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.Main, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(0, 40, 561, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 0, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_3.setGeometry(QtCore.QRect(360, 0, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(20)
        self.spinBox_3.setProperty("value", 10)
        self.spinBox_3.setObjectName("spinBox_3")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 90, 561, 31))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(90, 0, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox_2.setGeometry(QtCore.QRect(361, 0, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(20)
        self.spinBox_2.setProperty("value", 5)
        self.spinBox_2.setObjectName("spinBox_2")
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 140, 561, 31))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox.setGeometry(QtCore.QRect(90, 0, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.frame_9 = QtWidgets.QFrame(self.tab_2)
        self.frame_9.setGeometry(QtCore.QRect(0, 190, 561, 31))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_6 = QtWidgets.QLabel(self.frame_9)
        self.label_6.setGeometry(QtCore.QRect(90, 0, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_3.setGeometry(QtCore.QRect(322, 0, 171, 31))
        self.lineEdit_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(70, 94, 140);\n"
                                      "border: transparent;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame_7 = QtWidgets.QFrame(self.tab)
        self.frame_7.setGeometry(QtCore.QRect(0, 30, 561, 21))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(90, 0, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit.setGeometry(QtCore.QRect(322, 0, 171, 21))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(70, 94, 140);\n"
                                    "border: transparent;")
        self.lineEdit.setObjectName("lineEdit")
        self.frame_8 = QtWidgets.QFrame(self.tab)
        self.frame_8.setGeometry(QtCore.QRect(0, 70, 561, 21))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_8)
        self.checkBox_3.setGeometry(QtCore.QRect(90, 0, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.frame_10 = QtWidgets.QFrame(self.tab)
        self.frame_10.setGeometry(QtCore.QRect(0, 110, 561, 21))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_10)
        self.checkBox_4.setGeometry(QtCore.QRect(90, 0, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.frame_11 = QtWidgets.QFrame(self.tab)
        self.frame_11.setGeometry(QtCore.QRect(0, 150, 561, 21))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_5 = QtWidgets.QLabel(self.frame_11)
        self.label_5.setGeometry(QtCore.QRect(90, 0, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_2.setGeometry(QtCore.QRect(322, 0, 171, 21))
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(70, 94, 140);\n"
                                      "border: transparent;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.frame_12 = QtWidgets.QFrame(self.tab)
        self.frame_12.setGeometry(QtCore.QRect(0, 190, 561, 21))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_12)
        self.checkBox_5.setGeometry(QtCore.QRect(90, 0, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.frame_4 = QtWidgets.QFrame(self.tab)
        self.frame_4.setGeometry(QtCore.QRect(10, 230, 561, 21))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.spinBox_4 = QtWidgets.QSpinBox(self.frame_4)
        self.spinBox_4.setGeometry(QtCore.QRect(361, 0, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_4.setFont(font)
        self.spinBox_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(20)
        self.spinBox_4.setProperty("value", 2)
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(80, 0, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setGeometry(QtCore.QRect(40, 20, 481, 141))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(self.tab_3)
        self.progressBar.setGeometry(QtCore.QRect(40, 180, 481, 23))
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 220, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border:transparent;\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(50, 72, 115);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Youtube Comment Filter"))
        self.pushButton.setText(_translate("Dialog", "Get started"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main), _translate("Dialog", "Главная"))
        self.label_2.setText(_translate("Dialog", "Number of threads"))
        self.label_3.setText(_translate("Dialog", "Wait time on 429 error"))
        self.checkBox.setText(_translate("Dialog", "Using latest api version"))
        self.label_6.setText(_translate("Dialog", "Video id"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Настройки API"))
        self.label_4.setText(_translate("Dialog", "File name of censored words"))
        self.lineEdit.setText(_translate("Dialog", "default.txt"))
        self.checkBox_3.setText(_translate("Dialog", "Auto delete comments"))
        self.checkBox_4.setText(_translate("Dialog", "Delete links"))
        self.label_5.setText(_translate("Dialog", "File name of link exceptions"))
        self.lineEdit_2.setText(_translate("Dialog", "linkdefault.txt"))
        self.checkBox_5.setText(_translate("Dialog", "Delete duplicated comments"))
        self.label_7.setText(_translate("Dialog", "Count of comments to delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Настройки фильтра"))
        self.textBrowser.setHtml(_translate("Dialog",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                            "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                            "type=\"text/css\">\n "
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; "
                                            "font-size:8.25pt; font-weight:400; font-style:normal;\">\n "
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                            "font-size:11pt; color:#00bf39;\">Console "
                                            "connected</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Start filter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Консоль"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Вывод"))
        self.pushButton_2.clicked.connect(self.onClicked)

    def onClicked(self):
        thrd({
            "api": {
                "threads": self.spinBox_3.value(),
                "wait": self.spinBox_2.value(),
                "latestApi": self.checkBox.isChecked(),
                "videoId": self.lineEdit_3.text()
            },
            "filter": {
                "fileNameCensored": self.lineEdit.text(),
                "autoDelete": self.checkBox_3.isChecked(),
                "delLinks": self.checkBox_4.isChecked(),
                "fileNameExc": self.lineEdit_2.text(),
                "deleteDuplicated": self.checkBox_5.isChecked(),
                "count": self.spinBox_3.value()
            },
            "UIs": {
                'console': self.textBrowser,
                'progressBar': self.progressBar
            }
        })



class Filter:
    def __init__(self):
        self.russianLetters = 'йцукенгшщзхъфывапролджэячсмитьбю'
        self.blackListedWords = None
        self.linkExceptions = None
        self.commentList = []
        self.similarLetters = {
            'o': 'о',
            'c': 'с',
            'k': 'к',
            'x': 'х',
            'p': 'р',
            'y': 'у',
            '6': 'б',
            'H': 'Н',
            'M': 'М',
            'A': 'А',
            'E': 'Е',
            'e': 'e',
            'C': 'с',
            'О': 'о',
            'X': 'х',
            '0': 'о',
            '8': 'В'
        }

    def startFilter(self, settings):  # Starting the filter

        self.blackListedWords = open(settings['filter']['fileNameCensored'], 'r', encoding='utf-8')
        self.blackListedWords = self.blackListedWords.read()
        self.blackListedWords = self.blackListedWords.split('\n')

        self.linkExceptions = open(settings['filter']['fileNameExc'], 'r', encoding='utf-8')
        self.linkExceptions = self.linkExceptions.read()
        self.linkExceptions = self.linkExceptions.split('\n')

        commentCount = 0
        settings['UIs']['console'].append('Getting video comments (this might take a while)')
        videoComments = self.getVideoComments(settings['api']['videoId'])
        time.sleep(0.1)
        for comment in videoComments:
            commentCount += 1
            val = int(commentCount / len(self.commentList) * 100)
            settings['UIs']['progressBar'].setValue(val)
            if self.filterString(comment['text']):

                if settings['filter']['autoDelete']:
                    # self.deleteComment(comment['id'])
                    settings['UIs']['console'].append('comment "' + comment['text'] + '" has been deleted!')
                else:
                    settings['UIs']['console'].append('Founds suspicious comment ' + comment['text'])

            if self.filterLink(comment['text']):

                if settings['filter']['autoDelete']:
                    # self.deleteComment(comment['id'])
                    settings['UIs']['console'].append('Link comment "' + comment['text'] + '" has been deleted!')
                    self.deleteComment(comment['id'])
                else:
                    settings['UIs']['console'].append('Founds suspicious link comment ' + comment['text'])

    def replaceString(self, string):
        output = ''

        for letter in string:
            if letter in self.similarLetters:
                output += self.similarLetters[letter]
            else:
                output += letter

        return output

    def filterLink(self, string):
        if string.find('http') != -1 and string.find('://') != -1:
            hasException = False

            for exception in self.linkExceptions:
                if string.find(exception):
                    hasException = True
            if not hasException:
                return True

        if string.find('.com ') != -1 or string.find('.ru ') != -1:
            hasException = False

            for exception in self.linkExceptions:
                if string.find(exception):
                    hasException = True
            return hasException

    def deleteComment(self, vid):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, ["https://www.googleapis.com/auth/youtube.force-ssl"])
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        request = youtube.comments().delete(
            id=vid
        )
        request.execute()

    def getCommentPage(self, videoId, token):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyAtf0cVlKwq75vDnTa0V-xXQpnQZ5mz7tY"

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=DEVELOPER_KEY)

        request = youtube.commentThreads().list(
            part="snippet",
            videoId=videoId,
            pageToken=token,
            maxResults=100
        )
        response = request.execute()
        for item in response['items']:
            self.commentList.append({
                'videoId': item['snippet']['topLevelComment']['id'],
                'text': item['snippet']['topLevelComment']['snippet']['textDisplay']
            })
        if 'nextPageToken' in response:
            self.getCommentPage(videoId, response['nextPageToken'])
        else:
            return self.commentList

    def getVideoComments(self, videoId):
        return self.getCommentPage(videoId, '')

    def filterString(self, string):  # Filtering string by word
        for word in string.split():
            replacedWord = self.replaceString(word)
            filteredWord = self.removeExtraLetters(replacedWord)
            if filteredWord in self.blackListedWords:
                return True

    def removeExtraLetters(self, string):  # Removing letters that are not in Russian alphabet
        output = ''

        for letter1 in string:
            if letter1 in self.russianLetters:
                output += letter1
        return output


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    ex = Ui_Dialog()
    ex.setupUi(win)
    win.show()
    sys.exit(app.exec_())
