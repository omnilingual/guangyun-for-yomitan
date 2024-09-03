# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:31:02 2024

@author: Omnis
"""

indices = [
        '字頭',       #0
        '反切',       #1
        '切韻擬音',   #2
        '字類',       #3
        '聲形-聲',    #4
        '聲形-形',    #5
        '小韻首字',   #6
        '釋義',       #7
        '釋義補充',   #8
        '聲紐',       #9
        '攝',         #10
        '韻部',       #11
        '等',         #12
        '呼',         #13
        '聲調',       #14
        '聲旁',       #15
        'A/B類分析',  #16
        '聲形析微',   #17
    ]

raw = open('guangyun_stripped.csv', 'r', encoding='utf-8')
lines = raw.readlines()
raw.close()

with open('kanji_bank_1.json', 'w', encoding='utf-8') as o:
    o.write('[')
    for line in lines:
        items = line.strip().split(',')
        keyChr = items[0]
        prn = items[1] + '切　' + items[2]
        
        
        expList = []
        if items[3] == '':
            items[3] = '形聲'
        expList.append('"' + items[3] + '字，' + items[5] + items[4] + '"')
        if items[6] != '':
            expList.append('"' + indices[6] + '"')
        if items[8] != '':
            expList.append('"' + items[7] + '（' + items[8] + '）"')
        else:
            expList.append('"' + items[7] + '"')
        expList.append('"' + ''.join(items[9:15]) + '　' + items[15] + '聲"')
        if items[16] != '':
            expList.append('"※' + indices[16] + '：' + items[16] + '"')
        if items[17] != '':
            expList.append('"' + indices[17] + '：' + items[17] + '"')
        
        o.write('["' + keyChr + '","' + prn + '","","",[' + ','.join(expList) + '],{}],')
    o.write(']')
