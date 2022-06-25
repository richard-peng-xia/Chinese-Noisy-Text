"""tools"""
from pypinyin import pinyin, lazy_pinyin, Style
import random


# 同音字
def homophones_char(word):
    with open("./ChineseHomophones/chinese_homophone_char.txt", 'r', encoding="utf-8") as f:
        lines = f.readlines()
        word_pinyin = lazy_pinyin(word)
        selection = word
        for row in lines:
            str_row = row.split('\n')[0]
            lst_row = str_row.split('\t')
            if word_pinyin[0] == lst_row[0]:
                i = lst_row.index(word)
                r = list(range(1, i-1)) + list(range(i+1, len(lst_row)))
                k = random.choice(r)
                selection = lst_row[k]
            else:
                selection = word
            return selection


# 形近字
def similar_form_characters(word):
    with open('./SimilarCharacter/形近字语料库.txt','r',encoding="utf-8") as f:
        lines = f.readlines()
        lst_raw = []
        for row in lines:
            str_row = row.split('\n')[0]
            lst_row = str_row.split(' ')
            lst_raw.append(lst_row)
        for i in lst_raw:
            if word == i[0]:
                a = len(i[1])
                if a == 1:
                    selection = i[1][0]
                elif a == 0:
                    selection = word
                else:
                    k = random.randint(0, a-1)
                    selection = i[1][k]
                return selection if selection is not None else word