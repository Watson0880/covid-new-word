from pyhanlp import *
from googletrans import Translator

def load_dictionary():
    """
    加载HanLP中的mini词库
    :return: 一个set形式的词库
    """
    IOUtil = JClass('com.hankcs.hanlp.corpus.io.IOUtil')
    path = HanLP.Config.CoreDictionaryPath.replace('.txt', '.mini.txt')
    dic = IOUtil.loadDictionary([path])
    return set(dic.keySet())

def load_covid_dic():
    dic = []
    with open("result_word.txt", encoding='UTF-8') as f:
        for line in f.readlines():
            dic.append(line.rstrip('\n'))
    return set(dic)

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

def backward_segment_2dic(text, dic,dic_2):
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
            if word in dic_2:
                if len(word) > len(longest_word):   # 越长优先级越高
                    longest_word = word
                    break
        word_list.insert(0, longest_word)           # 逆向扫描，所以越先查出的单词在位置上越靠后
        i -= len(longest_word)
    return word_list


dic = load_dictionary()
dic_covid = load_covid_dic()
string = "BF.7为Omicron BA.5变异株的分支，因蔓延速度快BF.7成为3大新型变异株中最受关注的，而医疗应变组副组长罗一钧也表示，BF.7不只在中国、德国、法国、丹麦、英国等多个国家迅速蔓延，就连美国疾病管制与预防中心（CDC）的专家都发出警告，BF.7有可能会成为下一波造成全球肆虐的新威胁。 BF.7常见症状与其他Omicron变异株相似，包含头痛、胸痛、嗅觉改变、咳嗽、丧失听力、颤抖等，其他新冠常见症状则有，疲劳、流鼻水、喉咙痛、腹部疼痛、腹泻等。 BQ.1与BQ.1.1变异株也属于BA.5的分支，根据CDC近期的预估指出，1个月前正式命名的Omicron新亚型变异株BQ.1及其亚系BQ.1.1，目前已占新确诊病例的10％以上。而白宫首席防疫专家佛奇（Anthony Fauci）认为，BQ.1和BQ.1.1变异株以目前的传播倍增速度来看，相当棘手。"
word = backward_segment(string, dic)
word_2 = backward_segment_2dic(string, dic,dic_covid)
print(word)
print()
print(word_2)

string = 'BF.7,为,Omicron, ,BA.5,变异株,的,分支,，,因,蔓延,速度,快,BF.7,成为,3,大,新型,变异株,中,最,受,关注,的,，,而,医疗,应变组,副组长,罗一钧,也,表示,，,BF.7,不只,在,中国,、,德国,、,法国,、,丹麦,、,英国,等,多,个,国家,迅速,蔓延,，,就,连,美国疾病管制与预防中心,（,CDC,）,的,专家,都,发出,警告,，,BF.7,有,可能,会,成为,下一波,造成,全球,肆虐,的,新,威胁,。 ,BF.7,常见,症状,与,其他,Omicron,变异株,相似,，,包含,头痛,、,胸痛,、,嗅觉,改变,、,咳嗽,、,丧失,听力,、,颤抖,等,，,其他,新冠,常见,症状,则,有,，,疲劳,、,流鼻水,、,喉咙痛,、,腹部疼痛,、,腹泻,等,。 ,BQ.1,与,BQ.1.1,变异株,也,属于,BA.5,的,分支,，,根据,CDC,近期,的,预估,指出,，,1,个,月,前,正式,命名,的,Omicron,新,亚型,变异株,BQ.1,及,其,亚系,BQ.1.1,，,目前,已,占,新,确诊,病例,的,10％,以上,。 ,而,白宫,首席,防疫,专家,佛奇,（,Anthony Fauci,）,认为,，,BQ.1,和,BQ.1.1,变异株,以,目前,的,传播,倍增,速度,来看,，,相当,棘手,。'
trueS = string.split(',')
#print('分詞:',new_word)
#print('正確分詞:',trueS)
totallen = len(trueS)
print("一般分詞:",len(word))
print("加入COVID語料庫分詞:",len(word_2))
print("正確分詞:",totallen)
yes = 0
for i in trueS:
    if i in word:
        yes += 1
yes_2 = 0
for i in trueS:
    if i in word_2:
        yes_2 += 1
print("True: {0}/{1}".format(yes,totallen))
print("True: {0}/{1}".format(yes_2,totallen))
