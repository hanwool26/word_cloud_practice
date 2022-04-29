import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from excel import *
from word_cloud import *

form_class = uic.loadUiType("main.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_file_btn.clicked.connect(self.load_file_btn_clicked)
        self.qPixmapVar = QPixmap()

    def load_file_btn_clicked(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', './')
        if fname != None:
            self.handler_word_cloud(fname[0])

    def handler_word_cloud(self, file_path):
        file = extract_excel(file_path)
        wc = Word_Cloud(file, int(self.top_rank_edit.text()))
        wc.make_cloud()
        result_file = wc.analyze_wordlist()
        self.qPixmapVar.load(result_file)
        self.qPixmapVar = self.qPixmapVar.scaledToWidth(780)
        self.gui_label.setAlignment(Qt.AlignTop)
        self.gui_label.setPixmap(self.qPixmapVar)


