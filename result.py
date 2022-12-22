ct_word_dict = {}
ttv_word_dict = {}
newwordpath = 'ct_new_word.txt'

with open(newwordpath, encoding='UTF-8') as f:
    for line in f.readlines():
        #print(line.rstrip('\n'))
        s = ""
        for i in line.rstrip('\n').split(' ')[:-1]:
            s += i + ' '
        s = s.rstrip(' ')
        try:
            ct_word_dict[s] = int(line.rstrip('\n').split(' ')[-1])
        except:
            pass

newwordpath = 'ttv_new_word.txt'

with open(newwordpath, encoding='UTF-8') as f:
    for line in f.readlines():
        #print(line.rstrip('\n'))
        s = ""
        for i in line.rstrip('\n').split(' ')[:-1]:
            s += i + ' '
        s = s.rstrip(' ')
        try:
            ttv_word_dict[s] = int(line.rstrip('\n').split(' ')[-1])
        except:
            pass

name = []
num = []

for i in ct_word_dict:
    if i in name:
        for j in range(len(name)):
            if name[j]==i:
                num[j] += ct_word_dict[i]
                break
    else:
        name.append(i)
        num.append(ct_word_dict[i])

for i in ttv_word_dict:
    if i in name:
        for j in range(len(name)):
            if name[j]==i:
                num[j] += ttv_word_dict[i]
                break
    else:
        name.append(i)
        num.append(ttv_word_dict[i])

with open("result_word.txt",'w', encoding='UTF-8') as f:
    for i in range(len(name)):
        if num[i] > 29:
            f.write(name[i]+'\n')

with open("result_new_word.txt",'w', encoding='UTF-8') as f:
    for i in range(len(name)):
        f.write("{0} {1}".format(name[i],num[i])+'\n')  #寫入title
