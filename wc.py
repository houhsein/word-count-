"""
wc 程式
-l 顯示行數
-w 字數
-c 字元數
-L 最長行的長度
"""

import sys, string, argparse

def wc(input_file):
    with open(input_file, 'r', encoding="utf-8") as file:
        global line_count,word_count,char_count,long_line
        lines = file.readlines()
        line_count = len(lines)
        word_count = 0
        char_count = 0
        long_line = 0
        for line in lines:
            words = line.split("\n")
            word_count += len(words)
            char_count += len(line)
            if len(line) > long_line:
                long_line = len(line)

        _result_dic = {'line': _line_show,
                       'word': _word_show,
                       'char': _char_show,
                       'long': _long_show}

    return _result_dic


def _line_show(option):
    if option:
        print("行數:", line_count)

def _word_show(option):
    if option:
        print("字數:", word_count)

def _char_show(option):
    if option:
        print("字元數:", char_count)

def _long_show(option):
    if option:
        print("最長行的長度:", long_line)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Read file")
    
    # parser.add_argument('--foo', action='store_const', const=42) default 為 None
    '''
    parser.add_argument("-l", dest="line", const='line', action="store_const", help="Show the number of lines")
    parser.add_argument("-w", dest="word", const='word', action="store_const", help="Show the number of words")
    parser.add_argument("-c", dest="char", const='char', action="store_const", help="Show the number of characters")
    parser.add_argument("-L", dest="long", const='long', action="store_const", help="Show the longest line")
    '''

    parser.add_argument("-l", dest="line", default=False, action="store_true", help="Show the number of lines")
    parser.add_argument("-w", dest="word", default=False, action="store_true", help="Show the number of words")
    parser.add_argument("-c", dest="char", default=False, action="store_true", help="Show the number of characters")
    parser.add_argument("-L", dest="long", default=False, action="store_true", help="Show the longest line")

    args = parser.parse_args()
    result = wc(args.file)

    # 沒有參數 則全部顯示
    if args.line == args.word == args.char == args.long == False: 
        result['line'](True)
        result['word'](True)
        result['char'](True)
    else:
        result['line'](args.line)
        result['word'](args.word)
        result['char'](args.char)
        result['long'](args.long)
 
if __name__ == '__main__':
    main()
else:
    print("wc 已被匯入為模組")
