from wordcloud import WordCloud
from konlpy.tag import Twitter
from collections import Counter

class Word_Cloud():
    def __init__(self, file_path, number):
        self.twitter = Twitter()
        self.text = open(file_path, 'rt', encoding='UTF8').read()
        print(self.text)
        self.noun_adj_list = []
        self.word_num = number
        self.font_path = 'H2HDRM.TTF'

    def make_cloud(self):
        sentences_tag = []
        sentences_tag = self.twitter.pos(self.text)

        for word, tag in sentences_tag:
            if tag in ['Noun', 'Adjective']:
                self.noun_adj_list.append(word)

    def analyze_wordlist(self):
        result_path = 'test.jpg'
        counts = Counter(self.noun_adj_list)
        tags = counts.most_common(self.word_num) # save top 40 words

        wc = WordCloud(font_path=self.font_path, background_color='white', max_font_size=60)
        cloud = wc.generate_from_frequencies(dict(tags))

        try:
            cloud.to_file(result_path)
            return result_path
        except Exception as e:
            print(e)
