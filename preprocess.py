def article_preprocess(article):
    art_list = []
    temp1 = article.split('，') #逗號排除
    temp2 = []
    for i in temp1:
        temp = i.split('。')
        for j in temp:
            if len(j)!=0:
                temp2.append(j)
    temp1 = []
    for i in temp2:
        temp = i.split('；')
        for j in temp:
            if len(j)!=0:
                temp1.append(j)
    temp2 = []
    for i in temp1:
        temp = i.split('「')
        for j in temp:
            if len(j)!=0:
                temp2.append(j)
    temp1 = []
    for i in temp2:
        temp = i.split('」')
        for j in temp:
            if len(j)!=0:
                temp1.append(j)
    temp2 = []
    for i in temp1:
        temp = i.split('（')
        for j in temp:
            if len(j)!=0:
                temp2.append(j)
    temp1 = []
    for i in temp2:
        temp = i.split('）')
        for j in temp:
            if len(j)!=0:
                temp1.append(j)
    temp2 = []
    for i in temp1:
        temp = i.split('(')
        for j in temp:
            if len(j)!=0:
                temp2.append(j)
    temp1 = []
    for i in temp2:
        temp = i.split(')')
        for j in temp:
            if len(j)!=0:
                temp1.append(j)        
    temp2 = []
    for i in temp1:
        temp = i.split('、')
        for j in temp:
            if len(j)!=0:
                temp2.append(j)
    temp1 = []
    for i in temp2:
        temp = i.split('《')
        for j in temp:
            if len(j)!=0:
                temp1.append(j)
    temp2 = []
    for i in temp1:
        temp = i.split('》')
        for j in temp:
            if len(j)!=0:
                temp2.append(j)
    temp1 = []
    for i in temp2:
        temp = i.split('』')
        for j in temp:
            if len(j)!=0:
                temp1.append(j)
    temp2 = []
    for i in temp1:
        temp = i.split('｢')
        for j in temp:
            if len(j)!=0:
                temp2.append(j)
    temp1 = []
    for i in temp2:
        temp = i.split('｣')
        for j in temp:
            if len(j)!=0:
                temp1.append(j)
    temp2 = []
    for i in temp1:
        temp = i.split('『')
        for j in temp:
            if len(j)!=0:
                temp2.append(j)
    temp1 = []
    for i in temp2:
        temp = i.split(':')
        for j in temp:
            if len(j)!=0:
                temp1.append(j)
    temp2 = []
    for i in temp1:
        temp = i.split('：')
        for j in temp:
            if len(j)!=0:
                temp2.append(j)
    art_list = temp2
    return art_list
