def combine(word):
    ban_word = ['％','%','Q：','A：','年','月','日','岁','例','路','成','吧','阿','啊','党','分','批','家','村','弄','名','县','约','区']
    jump = ['与','或','在','为','的','但','也','而','和','昨','有','今','就','是','以','第','妳','你','她','他','吗','却','很','让','被','了','既','这','且','?','!','？','！','应',
            '我','仍','如','及','市','各','給','至','说','●','近','从','到','要','将','因','对','都','据','】','【','◎','件','更多','百万','移入','上','万人','已','每','过','另','★',
            '中时','那又','那','之','遭','们','则','据','首度','案','于','把','它','还','称','只','致','／','打','像','/','籍''么', '了', '与', '不', '且', '之', '为', '兮', '其', '到',
            '云', '阿', '却', '个', '们', '价', '似', '讫', '诸', '取', '若', '得', '逝', '将', '夫', '头', '只', '吗', '向', '吧', '呗', '呃', '呀', '员', '呵', '呢', '哇', '咦', '哟',
            '哉', '啊', '哩', '啵', '唻', '啰', '唯', '嘛', '噬', '嚜', '家', '如', '掉', '给', '维', '圪', '在', '尔', '惟', '子', '赊', '焉', '然', '旃', '所', '见', '斯', '者', '来',
            '欤', '是', '毋', '曰', '的', '每', '看', '着', '矣', '罢', '而', '耶', '粤', '聿', '等', '言', '越', '馨','的', '之', '在', '於', '從', '自', '打', '由', '朝', '向', '往',
            '沿著', '當', '於', '對', '對於', '關於', '至於', '和', '跟', '同', '與', '為', '給', '替', '將', '叫', '讓', '被', '比','按', '按照', '依', '依照', '照', '據', '根據', '以',
            '憑', '論', '由於', '為', '為了', '為著連', '除了', '趁','和', '跟', '与', '同', '及', '而', '况', '则', '乃', '就', '而', '是', '至于', '说到', '此外', '像', '如', '一般',
            '比方', '却', '但是', '然而', '而', '偏偏', '只是', '不过', '至于', '致', '不料', '岂知', '原来', '因为', '由于', '以便', '因此', '所以', '是故', '以致', '或', '抑', '若',
            '如果', '若是', '假如', '假使', '倘若', '要是', '譬如', '像', '好比', '如同', '似乎', '等于', '不如', '不及', '虽然', '固', '然', '尽管', '纵然', '即使', '可是','啊', '咦',
            '嘿', '嗨', '嚯', '吓', '哟', '哈', '嘻', '呵', '哈哈', '嘻嘻', '呵呵', '唉', '哎', '嗨', '哎呀', '呸', '啐', '哼', '吓', '唉', '嗨', '嚯', '吓', '乌', '阿', '偌', '得', '叱',
            '吓', '吁', '呔', '呐', '呜', '呀', '呵', '哎', '咄', '咍', '呣', '呶', '呸', '呦', '哈', '哑', '咦', '哟', '咨', '啊', '唉', '唗', '哦', '哼', '唦', '喏', '啧', '嗏', '喝',
            '嗟', '喂', '喔', '嗄', '嗳', '嗤', '嘟', '嗨', '嗐', '嗯', '嘘', '嘿', '噢', '嘻', '噫', '嚄', '嚯', '猗', '於', '欸', '思', '恶', '罢', '阿呀', '啊哈', '啊呀', '啊哟',
            '啊唷', '哎哈', '哎呀', '哎也', '哎哟', '挨也', '嗳呀', '嗳哟', '嗳呦', '咨虖', '啧啧', '吁嗟', '于嗟', '于戏', '乎', '铄', '于皇', '唷喂', '噫嘻嚱', '猗与', '噫嗟', '已矣',
            '噫乎', '噫兴', '噫嘻', '噫吁嚱', '噫嚱', '噫吁哉', '耶嚛', '也那', '耶耶', '呀呀呼', '嘻嚱', '喔唷', '乌戏', '惟兮', '维兮', '乌乎', '呜呼', '嘻嘻', '叹辞', '别忙', '波查',
            '哈哈', '呃嚱', '咄咄', '恶乎', '呵呵', '嘿哎', '哼唷', '乖乖', '好家伙', '哈呀', '伙颐', '咍吁', '嗬唷', '嗟嗟', '嗟哉', '嗟来', '嗟乎', '吭唷', '哦呵', '哦嗬', '诺已',
            '给力','你', '我', '他', '它', '她', '俺', '自己', '你们', '我们', '咱们', '她们', '他们', '它们', '俺们', '大家', '近指', '这', '这儿', '这么', '这里', '这会儿', '这样',
            '这么样', '远指', '那', '那边', '那儿', '那里', '那样', '那么', '那会儿', '那么样', '其它', '每', '各', '某', '另', '谁', '哪', '几', '什么', '怎么', '哪里','串', '事', '册',
            '丘', '乘', '下', '丈', '丝', '两', '举', '具', '美', '包', '厘', '刀', '分', '列', '则', '剂', '副', '些', '匝', '队', '陌', '陔', '部', '出', '个', '介', '令', '份', '伙',
            '件', '任', '倍', '儋', '卖', '亩', '记', '双', '发', '叠', '节', '茎', '莛', '荮', '落', '蓬', '蔸', '巡', '过', '进', '通', '造', '遍', '道', '遭', '对', '尊', '头', '套',
            '弓', '引', '张', '弯', '开', '床', '座', '庹', '帖', '帧', '席', '常', '幅', '幢', '口', '句', '号', '台', '只', '吊', '合', '名', '吨', '和', '味', '响', '骑', '门',
            '间', '阕', '宗', '客', '家', '彪', '层', '尾', '届', '声', '扎', '打', '扣', '把', '抛', '批', '抔', '抱', '拨', '担', '拉', '抬', '拃', '挂', '挑', '挺', '捆', '掬', '排',
            '捧', '掐', '搭', '提', '握', '摊', '摞', '撇', '撮', '汪', '泓', '泡', '注', '浔', '派', '湾', '溜', '滩', '滴', '级', '纸', '线', '组', '绞', '统', '绺', '综', '缕', '缗',
            '场', '块', '坛', '垛', '堵', '堆', '堂', '塔', '墩', '回', '团', '围', '圈', '孔', '贴', '点', '煎', '熟', '车', '轮', '转', '载', '辆', '料', '卷', '截', '户', '房', '所',
            '扇', '炉', '炷', '觉', '斤', '笔', '本', '朵', '杆', '束', '条', '杯', '枚', '枝', '柄', '栋', '架', '根', '梃', '样', '株', '桩', '梭', '桶', '棵', '榀', '槽', '犋', '爿',
            '片', '版', '歇', '手', '拳', '段', '沓', '班', '曲', '替', '股', '肩', '脬', '腔', '支', '步', '武', '瓣', '秒', '秩', '钟', '钱', '铢', '锊', '铺', '锤', '锭', '锱',
            '章', '盆', '盏', '盘', '眉', '眼', '石', '码', '砣', '碗', '磴', '票', '罗', '畈', '番', '窝', '联', '缶', '耦', '粒', '索', '累', '緉', '般', '艘', '竿', '筥', '筒', '筹',
            '管', '篇', '箱', '簇', '角', '重', '身', '躯', '酲', '起', '趟', '面', '首', '项', '领', '顶', '颗', '顷', '袭', '群', '袋','乃', '乌', '乍', '了', '一', '万', '无', '不',
            '专', '业', '东', '且', '世', '两', '习', '也', '乱', '举', '公', '共', '其', '具', '勿', '匆', '决', '况', '净', '历', '分', '初', '刚', '划', '列', '则', '别', '刬', '剩',
            '兀', '允', '光', '先', '兜', '亏', '互', '亘', '亟', '匪', '匿', '阳', '阴', '阿', '除', '陡', '险', '都', '隐', '兹', '兼', '几', '凡', '即', '却', '再', '罔', '力', '加',
            '务', '动', '劣', '勤', '从', '今', '会', '佥', '仅', '仍', '休', '但', '何', '侪', '便', '俄', '俪', '侵', '信', '俶', '倒', '健', '俱', '倏', '假', '偶', '偏', '偷', '偕',
            '傍', '傥', '傻', '全', '单', '卒', '南', '亢', '交', '亦', '亲', '亶', '讫', '讵', '许', '识', '诚', '该', '试', '询', '诮', '诺', '谛', '谟', '又', '及', '反', '取', '叠',
            '芴', '茀', '苟', '苦', '荐', '蓦', '蔑', '径', '很', '徒', '得', '微', '迄', '还', '近', '连', '迭', '迥', '逆', '适', '递', '通', '造', '逐', '逼', '遂', '逾', '遽',
            '寻', '将', '大', '夫', '太', '奉', '奇', '奈', '奄', '飞', '干', '平', '并', '幸', '巨', '巧', '左', '差', '弥', '强', '底', '庚', '庶', '庸', '廑', '已', '希', '常', '可',
            '叵', '只', '合', '各', '同', '向', '否', '咋', '哪', '咸', '哿', '唯', '啻', '善', '嗣', '嘣', '噎', '驯', '骊', '骎', '骤', '间', '阑', '阖', '宁', '安', '定', '审', '实',
            '宛', '害', '容', '宿', '寔', '寝', '寡', '好', '妄', '姑', '姗', '始', '委', '娄', '犹', '独', '狠', '猝', '猛', '岂', '岗', '崭', '尽', '层', '展', '屡', '饱', '才',
            '扔', '扩', '挺', '捴', '擅', '汔', '沉', '泛', '没', '浑', '活', '洒', '洵', '浸', '浪', '混', '渐', '深', '滋', '滚', '溘', '滥', '溜', '满', '漫', '潜', '约', '纯', '终',
            '给', '绝', '统', '绷', '缕', '在', '坏', '坚', '均', '垂', '填', '增', '固', '多', '少', '尚', '忝', '尝', '快', '怫', '怪', '恒', '恍', '恰', '恬', '恂', '惟', '慌', '愣',
            '慎', '慢', '憬', '尤', '就', '备', '复', '夐', '子', '孔', '孛', '财', '赆', '贼', '赖', '比', '毕', '焉', '煞', '长', '较', '辄', '死', '殆', '殊', '斗', '危', '方', '旅',
            '旋', '风', '成', '或', '所', '烂', '斩', '断', '老', '毫', '本', '未', '权', '杀', '杂', '极', '条', '果', '枚', '枉', '棐', '概', '横', '特', '改', '放', '故', '敢', '欻',
            '日', '早', '昆', '明', '是', '晃', '暂', '暗', '暴', '手', '拜', '永', '毋', '必', '忒', '忽', '总', '恶', '恚', '恐', '恣', '悉', '愈', '憙', '更', '曷', '曾', '最',
            '朅', '有', '肯', '朋', '胡', '胜', '胥', '脱', '腾', '臆', '止', '正', '此', '白', '的', '皆', '登', '甚', '私', '稍', '稀', '稔', '立', '竟', '端', '竭', '盍', '益', '盛',
            '盗', '盖', '每', '直', '相', '真', '睋', '瞥', '痛', '生', '砀', '确', '硬', '碜', '磕', '申', '畅', '略', '率', '究', '空', '窃', '突', '窘', '甫', '蚤', '蛮', '聊', '良',
            '虚', '类', '粗', '精', '紧', '素', '綦', '齐', '舒', '覃', '覆', '行', '翻', '肆', '肇', '至', '致', '笃', '第', '等', '簇', '自', '臭', '重', '身', '躬', '豫', '酣', '酷',
            '貌', '赵', '起', '越', '足', '跃', '踽', '非', '雅', '魆', '首', '黕', '默', '黩', '齁', '顾', '须', '颇', '顶', '顿', '频', '顺', '裁','做','疑']
    c_word = []
    len_over1 = []
    if len(word[0])==1:
        len_over1.append(-1)
    for i in range(len(word)):
        if len(word[i]) > 1:
            len_over1.append(i)
    if len(word[len(word)-1])==1:
        len_over1.append(len(word))
    for i in range(len(len_over1)-1):
        if len_over1[i+1] - len_over1[i] == 1:
            continue
        new_w = ""
        for j in range(len_over1[i]+1,len_over1[i+1]):
            can_join = 1
            if word[j] in jump:
                can_join = 0
            if can_join == 1:
                new_w += word[j]
        new_w = new_w.lstrip(' ')
        new_w = new_w.rstrip(' ')
        #print(new_w)
        ban = 0
        for j in ban_word:
            if j in new_w:
                ban = 1
        if len(new_w)<=1:
            pass
        elif 48<= ord(new_w[0]) <= 57:
            pass
        elif ban == 1:
            pass
        elif new_w[len(new_w)-1] == '等':
            if len(new_w[:-1])>1:
                new_w = new_w[:-1]
            else:
                pass
        else:
            c_word.append(new_w)     
   
    return c_word

