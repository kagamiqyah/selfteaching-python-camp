import json
import stats_word
import jieba

with open('/Users/mac/Documents/Documents - mac的MacBook Air/GitHub/selfteaching-python-camp/exercises/1901050017/d10/mymodule//tang300.json','r',encoding ='UTF-8') as s:
    t = s.read()
try : 
    print(stats_word.stats_text_cn(t,20))
except ValueError as error :
    print(error)
