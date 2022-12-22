import requests
from bs4 import BeautifulSoup
import json
import time
from pyhanlp import *
from googletrans import Translator
import combine
import preprocess


#//*[@id="stream-container-scroll-template"]/li[3]/div/div/div/div[2]/h3/a/text()
def load_dictionary():
    """
    加载HanLP中的mini词库
    :return: 一个set形式的词库
    """
    IOUtil = JClass('com.hankcs.hanlp.corpus.io.IOUtil')
    path = HanLP.Config.CoreDictionaryPath.replace('.txt', '.mini.txt')
    dic = IOUtil.loadDictionary([path])
    return set(dic.keySet())

def backward_segment(text, dic):
    word_list = []
    i = len(text) - 1
    while i >= 0:                                   # 扫描位置作为终点
        longest_word = text[i]                      # 扫描位置的单字
        for j in range(0, i):                       # 遍历[0, i]区间作为待查询词语的起点
            word = text[j: i + 1]                   # 取出[j, i]区间作为待查询单词
            if word in dic:
                if len(word) > len(longest_word):   # 越长优先级越高
                    longest_word = word
                    break
        word_list.insert(0, longest_word)           # 逆向扫描，所以越先查出的单词在位置上越靠后
        i -= len(longest_word)
    return word_list

def forward_segment(text, dic):
    word_list = []
    i = 0
    while i < len(text):
        longest_word = text[i]                      # 当前扫描位置的单字
        for j in range(i + 1, len(text) + 1):       # 所有可能的结尾
            word = text[i:j]                        # 从当前位置到结尾的连续字符串
            if word in dic:                         # 在词典中
                if len(word) > len(longest_word):   # 并且更长
                    longest_word = word             # 则更优先输出
        word_list.append(longest_word)              # 输出最长词
        i += len(longest_word)                      # 正向扫描
    return word_list







seed = ["新冠肺炎","高端","武漢肺炎","疫情","疫苗","變異株","確診"]
point_word = "新冠肺炎"
ttvnews_url = "https://news.ttv.com.tw/"
url = "https://news.ttv.com.tw/search/"
page = 1
titlepath = 'ttvnewstitle.txt'
newwordpath = 'ttv_new_word.txt'
news_dict = {};
with open(titlepath, encoding='UTF-8') as f:
    for line in f.readlines():
        #print(line.rstrip('\n'))
        news_dict[line.rstrip('\n')] = 1
word_dict = {}
with open(newwordpath, encoding='UTF-8') as f:
    for line in f.readlines():
        #print(line.rstrip('\n'))
        wd = ''
        for i in line.rstrip('\n').split(' ')[0:-1]:
            wd += i + ' '
        wd = wd.rstrip(' ')
        try:
            word_dict[wd] = int(line.rstrip('\n').split(' ')[-1])
        except:
            pass
print(len(word_dict))
try:
    for point in seed:
        
        #if point != "新冠肺炎": #先做一次        
         #   break
        
        point_word = point
        for i in range(0,420):
            s_url = url
            for j in point_word.encode(encoding='utf-8'):
                s_url += "%" + hex(j)[2:]
            s_url += '/'+str(page+i)

            html = requests.get(s_url) #請求
            sp = BeautifulSoup(html.text,'lxml') #轉換
            news_list = sp.find_all("a",class_='clearfix')
            print("第",i)
            print(len(news_list)) #搜尋到的數量
            if len(news_list)==0:
                print('跳過')
                time.sleep(3)
                continue
            for j in range(0,len(news_list)):
                #print(news_list[j].get("href"))
                #print(news_list[j].select('div')[0].find(class_='title').text)
                
                if news_dict.get(news_list[j].select('div')[0].find(class_='title').text) != None: #確認是否找過了
                    continue
                time.sleep(1)
                print("之",j)
                new_url = news_list[j].get("href")
                new_html = requests.get(ttvnews_url+new_url)
                new_sp = BeautifulSoup(new_html.text,'lxml')
                content = new_sp.find("div",class_='article-body')
                #print(content.select('p'))
                
                with open(titlepath,'a', encoding='UTF-8') as f:
                    f.write(news_list[j].select('div')[0].find(class_='title').text+'\n')  #寫入title
                    news_dict[news_list[j].select('div')[0].find(class_='title').text] = 1
                    
                new_article = ""
                for k in content.select('p'):  #抓新聞內容
                    if len(k)!=0:
                        #print(k.text)
                        if k != content.select('p')[len(content.select('p'))-1]:
                            new_article += k.text

                        #
                #DO preprocess action
                
                        
                
                if __name__ == '__main__':
                    dic = load_dictionary()
                    translator = Translator()
                    try:
                        cn_new_article = translator.translate(new_article, dest='zh-CN').text #轉換簡體
                    except:
                        continue
                    #DO preprocess action
                    art_list = preprocess.article_preprocess(cn_new_article)

                    #由後
                    new_word_1 = []
                    for w in art_list:
                        #print('------')
                        #print(w)
                        for ww in combine.combine(forward_segment(w, dic)): ##分詞後合併
                            #print(ww)
                            new_word_1.append(ww)
                    word = backward_segment(cn_new_article, dic)
                    '''
                    for k in new_word_1:
                        if word_dict.get(k) != None:
                            word_dict[k] = word_dict.get(k) + 1
                        else:
                            word_dict[k] = 1
                    '''
                    #print(word)
                    print(new_word_1)

                    #由前
                    new_word_2 = []
                    for w in art_list:
                        #print('------')
                        #print(w)
                        for ww in combine.combine(backward_segment(w, dic)): ##分詞後合併
                            #print(ww)
                            new_word_2.append(ww)
                    '''
                    for k in new_word_2:
                        if word_dict.get(k) != None:
                            word_dict[k] = word_dict.get(k) + 1
                        else:
                            word_dict[k] = 1
                    '''
                    print(new_word_2)

                    word_name = []
                    word1_num = []
                    word2_num = []

                    for k in new_word_1:
                        if k in word_name:
                            for l in range(len(word_name)):
                                if word_name[l] == k:
                                    word1_num[l] += 1
                                    break
                        else:
                            word_name.append(k)
                            word1_num.append(1)
                            word2_num.append(0)
                    for k in new_word_2:
                        if k in word_name:
                            for l in range(len(word_name)):
                                if word_name[l] == k:
                                    word2_num[l] += 1
                                    break
                        else:
                            word_name.append(k)
                            word1_num.append(0)
                            word2_num.append(1)
                    for k in range(len(word_name)):
                        print(word_name[k],word1_num[k],word2_num[k])
                    for k in range(len(word_name)):
                        if word1_num[k]>=word2_num[k] and word2_num[k]!=0:
                            if word_dict.get(word_name[k]) != None:
                                word_dict[word_name[k]] = word_dict.get(word_name[k]) + word2_num[k]
                            else:
                                word_dict[word_name[k]] = word2_num[k]
                        elif word1_num[k]<word2_num[k] and word1_num[k]!=0:
                            if word_dict.get(word_name[k]) != None:
                                word_dict[word_name[k]] = word_dict.get(word_name[k]) + word1_num[k]
                            else:
                                word_dict[word_name[k]] = word1_num[k]
                                    
            if (i+1)%5==0:
                temp_dict = {}
                for k in word_dict:
                    if word_dict[k]>1:
                        temp_dict[k] = word_dict[k]
                word_dict = temp_dict
                with open(newwordpath,'w', encoding='UTF-8') as f:
                    for k in word_dict:
                        f.write("{0} {1}".format(k,word_dict[k])+'\n')  #寫入title
                print("寫入檔案")
            print("第",i,"結束")
            time.sleep(3)

except:
    pass
with open(newwordpath,'w', encoding='UTF-8') as f:
    for i in word_dict:
        f.write("{0} {1}".format(i,word_dict[i])+'\n')  #寫入title
'''
for i in word_dict:
    if word_dict[i]>1:
        print("{0} {1}".format(i,word_dict[i]))
'''
        
'''
s_url = url
for j in point_word.encode(encoding='utf-8'):
    s_url += "%" + hex(j)[2:]
s_url += url1 + str(page)

print(s_url)
html = requests.get(s_url)
print(html.text)
sp = BeautifulSoup(html.text,'lxml')
#article = sp.select(".article-left")
#print(article)
#, class_="special-format"
new_list = sp.find_all("div",class_='col')
print(len(new_list))
#print(link[0].select('a')) 抓到標題與網址
print(new_list[0].select('a')[0].text)
print(new_list[0].select('a')[0].get("href"))
'''


'''
for i in range(0,1):
    s_url = url + str(offset*i) + point
    for j in point_word.encode(encoding='utf-8'):
        s_url += "%" + hex(j)[2:]
    print(s_url)
    html = requests.get(s_url)
    for j in range(len(json.loads(html.text))):
        print(json.loads(html.text)[j]['title'])
        print(json.loads(html.text)[j]['url'])
        title = json.loads(html.text)[j]['title']
        new_url = json.loads(html.text)[j]['url']
        
        new_html = requests.get(yahoo_url+new_url)
        sp = BeautifulSoup(new_html.text,'lxml')
        link = sp.select(".caas-body")
        print(len(link))
        for k in link[0].find_all('p')[0:-1]:
            print(k.text)
        time.sleep(1)
    time.sleep(3)
'''
