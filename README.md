Add word(s) to a file (to be determined, maybe a csv file) to build a vocabulary, and the words in vocabulary do not repeat, so that a student doesn't need to worry about duplicate words.


#### word(s) examples:

abandon

or

abandon, apple, come, come true, good

用python3运行\\wsl$\Ubuntu\home\lintj\addVocabulary\main.py，

会添加单词到\\wsl$\Ubuntu\home\lintj\file.csv

单词间中逗号隔开，中英文逗号均可。

## to-do:  
把中文转换成拼音再进行排序。

Additional useless notes:  
list(map(str.encode, ['一', '二', '三']))  
[b'\xe4\xb8\x80', b'\xe4\xba\x8c', b'\xe4\xb8\x89']
