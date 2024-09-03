# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:31:02 2024

@author: Omnis
"""

indices = [
        '字頭',       #0
        '反切',       #1
        '切韻擬音',   #2
        '聲紐',       #3
        '攝',         #4
        '韻部',       #5
        '等',         #6
        '呼',         #7
        '聲調',       #8
        'A/B類分析',  #9
        '聲旁',       #10
        '字類',       #11
        '形聲-形',    #12
        '形聲-聲',    #13
        '釋義',       #14
        '釋義補充',   #15
        '聲形析微',   #16
    ]

raw = open('guangyun_stripped.csv', 'r', encoding='utf-8')
lines = raw.readlines()
raw.close()

with open('kanji_bank_1.json', 'w', encoding='utf-8') as o:
    o.write('[')
    for line in lines:
        items = line.strip().split(',')
        keyChr = items[0]
        prn = items[1] + '切 ' + items[2]
        
        
        expList = []
        if items[9] != '':
            expList.append('"' + ''.join(items[3:9]) + '（' + items[9] + '）　' + items[10] + '聲"')
        else:
            expList.append('"' + ''.join(items[3:9]) + '　' + items[10] + '聲"')
        if items[11] == '':
            items[11] = '形聲'
        expList.append('"' + items[11] + '字　' + items[12] + items[13] + '"')
        if items[15] != '':
            expList.append('"' + items[14] + '（' + items[15] + '）"')
        else:
            expList.append('"' + items[14] + '"')
        if items[16] != '':
            expList.append('"' + indices[16] + '：' + items[16] + '"')
        
        o.write('["' + keyChr + '","' + prn + '","","",[' + ','.join(expList) + '],{}],')
    o.write(']')
