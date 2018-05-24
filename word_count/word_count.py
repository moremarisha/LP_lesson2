# coding = UTF-8
import logging
import re

logging.basicConfig(level=logging.DEBUG)

def get_word_count(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        word_cnt = 0
        i = 0
        for line in f:
            i += 1
            line = line[:-1].strip(" ")
            line = re.sub(' +', ' ', line)
            line = line.replace('\t', '')
            #logging.info('LINE {i}: {line}'.format(i=i, line=line))
            if line != '':
                word_list = line.split(' ')
                #logging.info(word_list)
                word_line_cnt = len(word_list)
                word_cnt += word_line_cnt
                rep = '{num}) line: {word_line_cnt}; file: {word_cnt}'.format(
                    num=i, word_line_cnt=word_line_cnt, word_cnt=word_cnt
                )
                #logging.info(rep)
        return word_cnt

if __name__ == "__main__":
    file_name = 'referat.txt'
    # file_name = 'my_file.txt'
    word_cnt = get_word_count(file_name)
    logging.info("Слов в тексте: {wc}".format(wc=word_cnt))
