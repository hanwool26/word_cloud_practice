from word_cloud import *
from excel import *
import matplotlib.pyplot as plt
import qdarkstyle
from PyQt5.QtWidgets import *
from mywindow import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mywindow = MyWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mywindow.show()
    app.exec_()
    '''
    file = extract_excel('sample.xlsx')
    wc = Word_Cloud(file, 40)
    wc.make_cloud()
    result_file = wc.analyze_wordlist()

    plt.figure(figsize=(10,8))
    plt.axis('off')
    plt.imshow(result_file)
    plt.show()
    '''