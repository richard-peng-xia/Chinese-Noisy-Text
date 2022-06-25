"""Functions adding noise to text"""
import jieba
import random
from utils import *

punctuation = ["！", "？", "｡", "＂", "＃", "＄", "％", "＆", "＇", "（", "）", "＊", "＋", "，",
               "－", "／", "：", "；", "＜", "＝", "＞", "＠", "［", "＼", "］", "＾", '＿', "｀",
               "｛", "｜", "｝", "～", "｢", "｣", "､", "、", "〃", "》", "「", "」", "『", "』", "【",
               "】", "〔", "〕", "〖", "〗", "〘", "〙", "〚", "〛", "〜", "〝", "〞", "〟", "–",
               "‘", "‛", "”", "„", "‟", "…", "‧", "﹏", "."]


# 冗余错误
def redundant_token(file, probability):
    lst_word_level = []  # 整个语料分词后合成的总的列表
    lst_word = []  # 整个语料分词后每个句子的列表
    D1 = {}  # 整个语料分词后的词表D1
    D2 = {}  # 整个语料字符级分词后的词表D2

    # 加载语料Cm
    with open(file, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for row in lines:
            lst_row = row.split('\n')[0].replace(' ', '')
            row_split_word_level = list(jieba.cut(lst_row))  # 每行分词后的列表
            lst_word.append(row_split_word_level)
            for split_word_ in row_split_word_level:
                lst_word_level.append(split_word_)  # 整个语料分词后合成的列表
        for word in lst_word_level:
            if word not in punctuation:
                D1[word] = D1.get(word, 0) + 1
        noise_word = lst_word.copy()  # 存放加噪后句子的列表
        for s_ in noise_word:  # 遍历语料中的每个句子S*
            idx = int(random.random() * len(s_))
            idx2 = int(random.random() * len(s_))
            idx3 = int(random.random() * len(s_))
            if s_[idx] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w1 = random.choice(list(D1))  # 从D1左侧随机取一个单词w1
                    s_[idx] = w1 + s_[idx]  # 在w左侧添加w1
            if s_[idx2] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w1 = random.choice(list(D1))  # 从D1左侧随机取一个单词w1
                    s_[idx2] = w1 + s_[idx2]  # 在w左侧添加w1
            if s_[idx3] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w1 = random.choice(list(D1))  # 从D1左侧随机取一个单词w1
                    s_[idx3] = w1 + s_[idx3]  # 在w左侧添加w1
        c_tmp = []  # 临时语料
        lst_char_level = []  # 整个语料按字符级分词后合成的列表
        lst_char = []  # 整个语料按字符级分词后每句的列表
        for _s in noise_word:
            c_tmp.append(''.join(_s))  # 将加噪的句子放入临时语料库c_tmp
        for _s in c_tmp:
            tmp = []
            for _w in _s:
                lst_char.append(_w)
                tmp.append(_w)
            lst_char_level.append(tmp)
        for word in lst_char:
            if word not in punctuation:
                D2[word] = D2.get(word, 0) + 1
        noise_char = lst_char_level.copy()  # 存放加字符噪后句子的列表
        for s_ in noise_char:  # 遍历c_tmp语料中的每个句子S*
            idx = int(random.random() * len(s_))
            idx2 = int(random.random() * len(s_))
            idx3 = int(random.random() * len(s_))
            if s_[idx] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w2 = random.choice(list(D2))  # 从D2左侧随机取一个单词w2
                    s_[idx] = w2 + s_[idx]  # 在w左侧添加w2
            if s_[idx2] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w2 = random.choice(list(D2))  # 从D2左侧随机取一个单词w2
                    s_[idx2] = w2 + s_[idx2]  # 在w左侧添加w2
            if s_[idx3] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w2 = random.choice(list(D2))  # 从D2左侧随机取一个单词w2
                    s_[idx3] = w2 + s_[idx3]  # 在w左侧添加w2
        c_noise = []  # 最终的噪声语料库
        for _s in noise_char:
            c_noise.append(''.join(_s))  # 将加字符级噪的句子放入最终语料库c_noise
            c_noise.append("\n")
        with open("add_noise/redundant_file.txt", "w", encoding="utf-8") as f2:
            f2.writelines(''.join(c_noise))
        return "*********冗余错误加噪完成*********"


# 缺词错误
def missing_token(file, probability):
    lst_word_level = []  # 整个语料分词后合成的总的列表
    lst_word = []  # 整个语料分词后每个句子的列表

    # 加载语料Cm
    with open(file, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for row in lines:
            lst_row = row.split('\n')[0].replace(' ', '')
            row_split_word_level = list(jieba.cut(lst_row))  # 每行分词后的列表
            lst_word.append(row_split_word_level)
            for split_word_ in row_split_word_level:
                lst_word_level.append(split_word_)  # 整个语料分词后合成的列表

        noise_word = lst_word.copy()  # 存放加噪后句子的列表
        for s_ in noise_word:  # 遍历语料中的每个句子S*
            idx = int(random.random() * len(s_))
            if -len(s_) < idx < len(s_):
                if s_[idx] not in punctuation and idx < len(s_):
                    k = random.random()  # 获取一个随机数k
                    if k >= probability:
                        continue
                    else:
                        del (s_[idx])  # 删除w
        c_tmp = []  # 临时语料
        lst_char_level = []  # 整个语料按字符级分词后合成的列表
        lst_char = []  # 整个语料按字符级分词后每句的列表
        for _s in noise_word:
            c_tmp.append(''.join(_s))  # 将加噪的句子放入临时语料库c_tmp
        for _s in c_tmp:
            tmp = []
            for _w in _s:
                lst_char.append(_w)
                tmp.append(_w)
            lst_char_level.append(tmp)
        noise_char = lst_char_level.copy()  # 存放加字符噪后句子的列表
        for s_ in noise_char:  # 遍历c_tmp语料中的每个句子S*
            idx = int(random.random() * len(s_))
            if idx < len(s_):
                if s_[idx] not in punctuation and idx < len(s_):
                    k = random.random()  # 获取一个随机数k
                    if k >= probability:
                        continue
                    else:
                        if s_ is not None:
                            del (s_[idx])  # 删除w
        c_noise = []  # 最终的噪声语料库
        for _s in noise_char:
            c_noise.append(''.join(_s))  # 将加字符级噪的句子放入最终语料库c_noise
            c_noise.append("\n")
        with open("add_noise/missing_file.txt", "w", encoding="utf-8") as f2:
            f2.writelines(''.join(c_noise))
        return "*********缺词错误加噪完成*********"


# 词序错误
def ordering_token(file, probability):
    lst_word_level = []  # 整个语料分词后合成的总的列表
    lst_word = []  # 整个语料分词后每个句子的列表

    # 加载语料Cm
    with open(file, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for row in lines:
            lst_row = row.split('\n')[0].replace(' ', '')
            row_split_word_level = list(jieba.cut(lst_row))  # 每行分词后的列表
            lst_word.append(row_split_word_level)
            for split_word_ in row_split_word_level:
                lst_word_level.append(split_word_)  # 整个语料分词后合成的列表
        noise_word = lst_word.copy()  # 存放加噪后句子的列表
        for s_ in noise_word:  # 遍历语料中的每个句子S*
            idx = int(random.random() * len(s_))
            idx2 = int(random.random() * len(s_))
            idx3 = int(random.random() * len(s_))
            if s_[idx] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                    if s_[i_] not in punctuation:
                        s_[idx] = s_[i_]  # 相互交换顺序
                        s_[i_] = s_[idx]
            if s_[idx2] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                    if s_[i_] not in punctuation:
                        s_[idx2] = s_[i_]  # 相互交换顺序
                        s_[i_] = s_[idx2]
            if s_[idx3] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                    if s_[i_] not in punctuation:
                        s_[idx3] = s_[i_]  # 相互交换顺序
                        s_[i_] = s_[idx3]
        c_tmp = []  # 临时语料
        lst_char_level = []  # 整个语料按字符级分词后合成的列表
        lst_char = []  # 整个语料按字符级分词后每句的列表
        for _s in noise_word:
            c_tmp.append(''.join(_s))  # 将加噪的句子放入临时语料库c_tmp
        for _s in c_tmp:
            tmp = []
            for _w in _s:
                lst_char.append(_w)
                tmp.append(_w)
            lst_char_level.append(tmp)
        noise_char = lst_char_level.copy()  # 存放加字符噪后句子的列表
        for s_ in noise_char:  # 遍历c_tmp语料中的每个句子S*
            idx = int(random.random() * len(s_))
            idx2 = int(random.random() * len(s_))
            idx3 = int(random.random() * len(s_))
            if s_[idx] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                    if s_[i_] not in punctuation:
                        s_[idx] = s_[i_]  # 相互交换顺序
                        s_[i_] = s_[idx]
                    else:
                        i__ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                        if s_[i__] not in punctuation:
                            s_[idx] = s_[i__]  # 相互交换顺序
                            s_[i__] = s_[idx]
            if s_[idx2] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                    if s_[i_] not in punctuation:
                        s_[idx2] = s_[i_]  # 相互交换顺序
                        s_[i_] = s_[idx2]
                    else:
                        i__ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                        if s_[i__] not in punctuation:
                            s_[idx2] = s_[i__]  # 相互交换顺序
                            s_[i__] = s_[idx2]
            if s_[idx3] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                    if s_[i_] not in punctuation:
                        s_[idx3] = s_[i_]  # 相互交换顺序
                        s_[i_] = s_[idx3]
                    else:
                        i__ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                        if s_[i__] not in punctuation:
                            s_[idx3] = s_[i__]  # 相互交换顺序
                            s_[i__] = s_[idx3]
        c_noise = []  # 最终的噪声语料库
        for _s in noise_char:
            c_noise.append(''.join(_s))  # 将加字符级噪的句子放入最终语料库c_noise
            c_noise.append("\n")
        with open("add_noise/ordering_file.txt", "w", encoding="utf-8") as f2:
            f2.writelines(''.join(c_noise))
        return "*********词序错误加噪完成*********"


# 选词错误
def selection_token(file, probability):
    lst_word_level = []  # 整个语料分词后合成的总的列表
    lst_word = []  # 整个语料分词后每个句子的列表
    D1 = {}  # 整个语料分词后的词表D1
    D2 = {}  # 整个语料字符级分词后的词表D2

    # 加载语料Cm
    with open(file, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for row in lines:
            lst_row = row.split('\n')[0].replace(' ', '')
            row_split_word_level = list(jieba.cut(lst_row))  # 每行分词后的列表
            lst_word.append(row_split_word_level)
            for split_word_ in row_split_word_level:
                lst_word_level.append(split_word_)  # 整个语料分词后合成的列表
        for word in lst_word_level:
            if word not in punctuation:
                D1[word] = D1.get(word, 0) + 1
        noise_word = lst_word.copy()  # 存放加噪后句子的列表
        for s_ in noise_word:  # 遍历语料中的每个句子S*
            idx = int(random.random() * len(s_))
            idx2 = int(random.random() * len(s_))
            idx3 = int(random.random() * len(s_))
            if s_[idx] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w1 = random.choice(list(D1))  # 从D1随机取一个单词w1
                    s_[idx] = w1  # 用别的单词替代w
            if s_[idx2] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w1 = random.choice(list(D1))  # 从D1随机取一个单词w1
                    s_[idx2] = w1  # 用别的单词替代w
            if s_[idx3] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w1 = random.choice(list(D1))  # 从D1随机取一个单词w1
                    s_[idx3] = w1  # 用别的单词替代w
        c_tmp = []  # 临时语料
        lst_char_level = []  # 整个语料按字符级分词后合成的列表
        lst_char = []  # 整个语料按字符级分词后每句的列表
        for _s in noise_word:
            c_tmp.append(''.join(_s))  # 将加噪的句子放入临时语料库c_tmp
        for _s in c_tmp:
            tmp = []
            for _w in _s:
                lst_char.append(_w)
                tmp.append(_w)
            lst_char_level.append(tmp)
        for word in lst_char:
            if word not in punctuation:
                D2[word] = D2.get(word, 0) + 1
        noise_char = lst_char_level.copy()  # 存放加字符噪后句子的列表
        # 错误字加噪
        for s_ in noise_char:  # 遍历c_tmp语料中的每个句子S*
            idx = int(random.random() * len(s_))
            idx2 = int(random.random() * len(s_))
            idx3 = int(random.random() * len(s_))
            if s_[idx] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w1 = random.choice(list(D2))  # 从词表中任意选择一个字
                    s_[idx] = w1
            if s_[idx2] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w1 = random.choice(list(D2))  # 从词表中任意选择一个字
                    s_[idx2] = w1
            if s_[idx3] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w1 = random.choice(list(D2))  # 从词表中任意选择一个字
                    s_[idx3] = w1
        # 同音字加噪
        for s_ in noise_char:  # 遍历c_tmp语料中的每个句子S*
            idx = int(random.random() * len(s_))
            idx2 = int(random.random() * len(s_))
            idx3 = int(random.random() * len(s_))
            if s_[idx] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w2 = homophones_char(s_[idx])  # 从词表中找出w的同音字
                    if w2 is not None:
                        s_[idx] = w2
            if s_[idx2] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w2 = homophones_char(s_[idx2])  # 从词表中找出w的同音字
                    if w2 is not None:
                        s_[idx2] = w2
            if s_[idx3] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w2 = homophones_char(s_[idx3])  # 从词表中找出w的同音字
                    if w2 is not None:
                        s_[idx3] = w2
        # 形近字加噪
        for s_ in noise_char:  # 遍历c_tmp语料中的每个句子S*
            idx = int(random.random() * len(s_))
            idx2 = int(random.random() * len(s_))
            idx3 = int(random.random() * len(s_))
            if s_[idx] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w2 = similar_form_characters(s_[idx])  # 从词表中找出w的形近字
                    if w2 is not None:
                        s_[idx] = w2
            if s_[idx2] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w2 = similar_form_characters(s_[idx2])  # 从词表中找出w的形近字
                    if w2 is not None:
                        s_[idx2] = w2
            if s_[idx3] not in punctuation:
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    w2 = similar_form_characters(s_[idx3])  # 从词表中找出w的形近字
                    if w2 is not None:
                        s_[idx3] = w2
        c_noise = []  # 最终的噪声语料库
        for _s in noise_char:
            c_noise.append(''.join(_s))  # 将加字符级噪的句子放入最终语料库c_noise
            c_noise.append("\n")
        with open("add_noise/selection_file.txt", "w", encoding="utf-8") as f2:
            f2.writelines(''.join(c_noise))
        return "*********选词错误加噪完成*********"


# 综合错误
def comprehensive_token(file, probability):
    lst_word_level = []  # 整个语料分词后合成的总的列表
    lst_word = []  # 整个语料分词后每个句子的列表
    D1 = {}  # 整个语料分词后的词表D1
    D2 = {}  # 整个语料字符级分词后的词表D2

    # 加载语料Cm
    with open(file, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for row in lines:
            lst_row = row.split('\n')[0].replace(' ', '')
            row_split_word_level = list(jieba.cut(lst_row))  # 每行分词后的列表
            lst_word.append(row_split_word_level)
            for split_word_ in row_split_word_level:
                lst_word_level.append(split_word_)  # 整个语料分词后合成的列表
        for word in lst_word_level:
            if word not in punctuation:
                D1[word] = D1.get(word, 0) + 1
        noise_word = lst_word.copy()  # 存放加噪后句子的列表
        for s_ in noise_word:  # 遍历语料中的每个句子S*
            idx = int(random.random() * len(s_))
            idx2 = int(random.random() * len(s_)) - 1
            idx3 = int(random.random() * len(s_)) - 2
            if s_[idx] not in punctuation and idx < len(s_):
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    rk = random.randint(0, 3)
                    if rk == 0:
                        w1 = random.choice(list(D1))  # 从D1左侧随机取一个单词w1
                        s_[idx] = w1 + s_[idx]  # 在w左侧添加w1
                    elif rk == 1:
                        s_[idx] = ''  # 删除w
                    elif rk == 2:
                        i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                        if s_[i_] not in punctuation:
                            s_[idx] = s_[i_]  # 相互交换顺序
                            s_[i_] = s_[idx]
                    elif rk == 3:
                        w1 = random.choice(list(D1))  # 从D1随机取一个单词w1
                        s_[idx] = w1  # 用别的单词替代w
            if s_[idx2] not in punctuation and idx2 < len(s_):
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    rk = random.randint(0, 3)
                    if rk == 0:
                        w1 = random.choice(list(D1))  # 从D1左侧随机取一个单词w1
                        s_[idx2] = w1 + s_[idx2]  # 在w左侧添加w1
                    elif rk == 1:
                        s_[idx2] = ''  # 删除w
                    elif rk == 2:
                        i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                        if s_[i_] not in punctuation:
                            s_[idx2] = s_[i_]  # 相互交换顺序
                            s_[i_] = s_[idx2]
                    elif rk == 3:
                        w1 = random.choice(list(D1))  # 从D1随机取一个单词w1
                        s_[idx2] = w1  # 用别的单词替代w
            if idx3 < len(s_):
                if s_[idx3] not in punctuation:
                    k = random.random()  # 获取一个随机数k
                    if k >= probability:
                        continue
                    else:
                        rk = random.randint(0, 3)
                        if rk == 0:
                            w1 = random.choice(list(D1))  # 从D1左侧随机取一个单词w1
                            s_[idx3] = w1 + s_[idx3]  # 在w左侧添加w1
                        elif rk == 1:
                            s_[idx3] = ''  # 删除w
                        elif rk == 2:
                            i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                            if s_[i_] not in punctuation:
                                s_[idx3] = s_[i_]  # 相互交换顺序
                                s_[i_] = s_[idx3]
                        elif rk == 3:
                            w1 = random.choice(list(D1))  # 从D1随机取一个单词w1
                            s_[idx3] = w1  # 用别的单词替代w
        c_tmp = []  # 临时语料
        lst_char_level = []  # 整个语料按字符级分词后合成的列表
        lst_char = []  # 整个语料按字符级分词后每句的列表
        for _s in noise_word:
            c_tmp.append(''.join(_s))  # 将加噪的句子放入临时语料库c_tmp
        for _s in c_tmp:
            tmp = []
            for _w in _s:
                lst_char.append(_w)
                tmp.append(_w)
            lst_char_level.append(tmp)
        for word in lst_char:
            if word not in punctuation:
                D2[word] = D2.get(word, 0) + 1
        noise_char = lst_char_level.copy()  # 存放加字符噪后句子的列表
        for s_ in noise_char:  # 遍历c_tmp语料中的每个句子S*
            idx2 = int(random.random() * len(s_))
            idx = int(random.random() * len(s_)) - 1
            idx3 = int(random.random() * len(s_)) - 2
            if s_[idx2] not in punctuation and -len(s_) < idx2 < len(s_):
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    rk = random.randint(0, 3)
                    if rk == 0:
                        w2 = random.choice(list(D2))  # 从D2左侧随机取一个单词w2
                        s_[idx2] = w2 + s_[idx2]  # 在w左侧添加w2
                    elif rk == 1 and idx2 < len(s_) and s_[idx2] is not None:
                        del s_[idx2]  # 删除w
                    elif rk == 2:
                        i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                        if s_[i_] not in punctuation:
                            s_[idx2] = s_[i_]  # 相互交换顺序
                            s_[i_] = s_[idx2]
                        else:
                            i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                            if s_[i_] not in punctuation:
                                s_[idx2] = s_[i_]  # 相互交换顺序
                                s_[i_] = s_[idx2]
                    elif rk == 3:
                        rk2 = random.randint(0, 2)
                        if rk2 == 0:
                            w1 = random.choice(list(D2))  # 从词表中任意选择一个字
                            s_[idx2] = w1
                        elif rk2 == 1:
                            w2 = homophones_char(s_[idx2])  # 从词表中找出w的同音字
                            if w2 is not None:
                                s_[idx2] = w2
                        elif rk2 == 2:
                            w2 = similar_form_characters(s_[idx2])  # 从词表中找出w的形近字
                            if w2 is not None:
                                s_[idx2] = w2
            if s_[idx] not in punctuation and -len(s_) < idx < len(s_):
                k = random.random()  # 获取一个随机数k
                if k >= probability:
                    continue
                else:
                    rk = random.randint(0, 3)
                    if rk == 0:
                        w2 = random.choice(list(D2))  # 从D2左侧随机取一个单词w2
                        s_[idx] = w2 + s_[idx]  # 在w左侧添加w2
                    elif rk == 1 and idx < len(s_) and s_[idx] is not None:
                        del s_[idx]  # 删除w
                    elif rk == 2:
                        i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                        if s_[i_] not in punctuation:
                            s_[idx] = s_[i_]  # 相互交换顺序
                            s_[i_] = s_[idx]
                        else:
                            i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                            if s_[i_] not in punctuation:
                                s_[idx] = s_[i_]  # 相互交换顺序
                                s_[i_] = s_[idx]
                    elif rk == 3:
                        rk2 = random.randint(0, 2)
                        if rk2 == 0:
                            w1 = random.choice(list(D2))  # 从词表中任意选择一个字
                            s_[idx] = w1
                        elif rk2 == 1:
                            w2 = homophones_char(s_[idx])  # 从词表中找出w的同音字
                            if w2 is not None:
                                s_[idx] = w2
                        elif rk2 == 2:
                            w2 = similar_form_characters(s_[idx])  # 从词表中找出w的形近字
                            if w2 is not None:
                                s_[idx] = w2
            if -len(s_) < idx3 < len(s_) and s_[idx3] not in punctuation:
                    k = random.random()  # 获取一个随机数k
                    if k >= probability:
                        continue
                    else:
                        rk = random.randint(0, 3)
                        if rk == 0:
                            w2 = random.choice(list(D2))  # 从D2左侧随机取一个单词w2
                            s_[idx3] = w2 + s_[idx3]  # 在w左侧添加w2
                        elif rk == 1 and idx3 < len(s_) and s_[idx3] is not None:
                            del s_[idx3]  # 删除w
                        elif rk == 2:
                            i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                            if s_[i_] not in punctuation:
                                s_[idx3] = s_[i_]  # 相互交换顺序
                                s_[i_] = s_[idx3]
                            else:
                                i_ = random.randint(0, len(s_) - 1)  # 取一个大小在0到每个句子长度-1之间的随机数
                                if s_[i_] not in punctuation:
                                    s_[idx3] = s_[i_]  # 相互交换顺序
                                    s_[i_] = s_[idx3]
                        elif rk == 3:
                            rk2 = random.randint(0, 2)
                            if rk2 == 0:
                                w1 = random.choice(list(D2))  # 从词表中任意选择一个字
                                s_[idx3] = w1
                            elif rk2 == 1:
                                w2 = homophones_char(s_[idx3])  # 从词表中找出w的同音字
                                if w2 is not None:
                                    s_[idx3] = w2
                            elif rk2 == 2:
                                w2 = similar_form_characters(s_[idx3])  # 从词表中找出w的形近字
                                if w2 is not None:
                                    s_[idx3] = w2
        c_noise = []  # 最终的噪声语料库
        for _s in noise_char:
            c_noise.append(''.join(_s))  # 将加字符级噪的句子放入最终语料库c_noise
            c_noise.append("\n")
        with open("add_noise/comprehensive_file.txt", "w", encoding="utf-8") as f2:
            f2.writelines(''.join(c_noise))
        return "*********综合错误加噪完成*********"
