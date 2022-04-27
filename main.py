from word_cloud import *
from excel import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    file = extract_excel('sample.xlsx')
    wc = Word_Cloud(file, 40)
    wc.make_cloud()
    result_file = wc.analyze_wordlist()

    plt.figure(figsize=(10,8))
    plt.axis('off')
    plt.imshow(result_file)
    plt.show()