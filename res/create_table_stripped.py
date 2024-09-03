# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:31:02 2024

@author: Omnis
"""

indices = [
        '字頭',       #0
        '聲紐',       #1
        '攝',         #2
        '韻部',       #3
        '等',         #4
        '呼',         #5
        '聲調',       #6
        'A/B類分析',  #7
        '反切',       #8
        '聲旁',       #9
        '切韻擬音',   #10
        '釋義',       #11
        '釋義補充',   #12
        '字類',       #13
        '形聲-形',    #14
        '形聲-聲',    #15
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
        prn = ''.join(items[1:7])
        if items[7] != '':
            prn += '（' + items[7] + '）'
        prn += ' ' + items[8] + '切　' + items[9] + '聲 ' + items[10]
        
        
        expList = []
        if items[12] != '':
            expList.append('"' + items[11] + '（' + items[12] + '）"')
        else:
            expList.append('"' + items[11] + '"')
        if items[13] == '':
            items[13] = '形聲'
        expList.append('"' + items[13] + '字◎' + items[14] + items[15] + '"')
        if items[16] != '':
            expList.append('"' + indices[16] + '：' + items[16] + '"')
        
        o.write('["' + keyChr + '","' + prn + '","","",[' + ','.join(expList) + '],{}],')
    o.write(']')
