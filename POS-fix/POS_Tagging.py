"""
The POS labels for each sentence have been obtained and saved in the Tagged-sentences Directory.
The credits for pos tagging go to minasmz for her work in https://github.com/minasmz/Persian-POSTagger-with-LSTM
In this file, we will manually resolve the inconsistencies that occurred in the POS tagging.
"""
import os
import operator
sentences = [] #each element will be in the form of text,aspects,opinions,english words,numbers

with open('sentences.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("@@@")
    for i in range(len(strings) - 1):
        sentences.append(eval(strings[i]))
weird_hehs = []
with open('weird-hehs.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("\n")
    for i in range(len(strings) - 1):
        weird_hehs.append(strings[i])
weird_hehs = weird_hehs[:-1]



main_path = "../Tagged-sentences/"
POS_tags = [] # the sentences have been pos tagged with the tagger module and the result lies in the Tagged-sentences directory (every txt file has 400 sentences)
for path in os.listdir(main_path):
    full_path = os.path.join(main_path, path)
    if os.path.isfile(full_path) and full_path.endswith(".txt"):
        print(full_path)
        with open(full_path,encoding="utf8") as file:
            strings = file.read().split("@@@")
            for i in range(len(strings) - 1):
                POS_tags.append(eval(strings[i]))
word_tag = [] # each sentence will be saved as a collection of tupples in the form of (word,tag)
#the rest of this code is extremely unclean! because I had to handle the discrepancies between the taggings and the original text manually
words_with_ist = {}
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        POS_tag[i] = POS_tag[i].replace('\n','')
        POS_tag[i] = POS_tag[i].split('/')
    for i in range(len(POS_tag)):
        if len(POS_tag[i]) == 3:
            POS_tag[i] = POS_tag[i][0:2]
    POS_tags[p] = [x for x in POS_tag if len(x) > 1]
tags = {}
del POS_tags[217]
del POS_tags[5371]
del POS_tags[5889]
del POS_tags[6392]
# dict_keys(['P', 'N', 'ADJ', 'DELM', 'V', 'CON', 'DET', 'NUM', 'ADV', 'PRO', 'CLITIC', 'PREV', 'INT', '', 'FW'])
#Aj,ClITIC = POSTPو,DELM = PUNC, CON = CONJ,PREV = P,'' = RES, for making it compatible to HAZM library
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] == ('هستش'):
            POS_tag[i][1] = 'V'
        elif POS_tag[i][0] == ('میدن'):
            POS_tag[i][1] = 'V'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][1] == 'ADJ':
            POS_tag[i][1] = 'AJ'
        elif POS_tag[i][1] == 'CLITIC':
            POS_tag[i][1] = 'POSTP'
        if POS_tag[i][1] == 'DELM':
            POS_tag[i][1] = 'PUNC'
        if POS_tag[i][1] == 'CON':
            POS_tag[i][1] = 'CONJ'
        if POS_tag[i][1] == 'PREV':
            POS_tag[i][1] = 'P'
        if POS_tag[i][1] == '' and POS_tag[i][0] == '':
            POS_tag[i][1] = 'RES'
            POS_tag[i][0] = '/'
        if POS_tag[i][1] == 'FW':
            POS_tag[i][1] = 'ADV'
        if POS_tag[i][1] == 'INT':
            if POS_tag[i][0] == 'ای':
                POS_tag[i-1][0] = POS_tag[i-1][0] + ' ای'
                if POS_tag[i-1][0] == 'حرفه ای':
                    POS_tag[i - 1][1] = 'AJ'
                POS_tag[i][0] = 'eliminate'
            if POS_tag[i][0] == 'وای':
                if POS_tag[i+1][0] == 'فای':
                    POS_tag[i + 1][0] = 'وای ' + POS_tag[i + 1][0]
                POS_tag[i][0] = 'eliminate'
            else:
                POS_tag[i][1] = 'N'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
tars = {}
allowed_tars = ['متر','شاتر','بستر','کامپیوتر','توییتر','کاتر','تیتر','میلیمتر','فیلتر','اکستر','پرینتر','۳متر','هلیکوپتر','دفتر','باتر','سنتر' ,
                'کاراکتر','آمتر']
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0].endswith('تر') and POS_tag[i][1] != 'AJ' and ('\u200c' in POS_tag[i][0] or POS_tag[i][0] not in allowed_tars):
            POS_tag[i][1] = 'AJ'


# for p,POS_tag in enumerate(POS_tags):
#     for i in range(len(POS_tag)):
#         if POS_tag[i][0].endswith('تر') and POS_tag[i][1] != 'AJ':
#             # POS_tag[i][1] = 'AJ'
#             # ints[POS_tag[i][0]] = True
#             # print(sentences[p][0])
#             if POS_tag[i][0] not in tars.keys():
#                 tars[POS_tag[i][0]]  = 1
#             else:
#                 tars[POS_tag[i][0]] += 1
#             # print(POS_tag[i-2])
#             # print(POS_tag[i-1])
#             # print(POS_tag[i+1])
# print(tars)
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0].endswith('ترین'):
            POS_tag[i][1] = 'AJ'

vas = {}
false_vas =['وگردن','وبررسی','وتشخیص','وخسته','ویک','وفقط','وامکانات','واصغرهستی','ومن','وصفحه','وطوفانیه','وکمتر','وخیلی','وافزودن','ودر']
false_vas_adj =['وخسته','وخیلی','وطوفانیه','وکمتر']
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] in false_vas:
            original_word = POS_tag[i][0][1:]
            POS_tag.insert(i+1,[])
            POS_tag[i+1].append(original_word)
            if POS_tag[i][0] in false_vas_adj:
                POS_tag[i+1].append('AJ')
            elif POS_tag[i][0] == 'ومن':
                POS_tag[i + 1].append('PRO')
            elif POS_tag[i][0] == 'واصغرهستی':
                POS_tag[i + 1].append('N')
                POS_tag[i + 1][0] = 'اصغر'
                POS_tag.insert(i + 2, [])
                POS_tag[i + 2].append('هستی')
                POS_tag[i + 2].append('V')
            else:
                POS_tag[i + 1].append('N')
            POS_tag[i][0] = 'و'
            POS_tag[i][1] = 'CONJ'

allowed_taris = ['باتری','متری','مشتری','۳میلیمتری','کامپیوتری','نانومتری','خیرباتری','میلیمتری', 'فیلتری', 'صداتری', 'برتری','پرینتری']
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0].endswith('تری') and POS_tag[i][1] != 'AJ' and ('\u200c' in POS_tag[i][0] or POS_tag[i][0] not in allowed_taris):
            POS_tag[i][1] = 'AJ'


for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] == 'میکنهکیفیت':
            POS_tag.insert(i + 1, [])
            POS_tag[i + 1].append('کیفیت')
            POS_tag[i + 1].append('N')
            POS_tag[i][0] = 'میکنه'
            POS_tag[i][1] = 'V'

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] == 'باز':
            if  POS_tag[i+1][0] == 'هم':
                POS_tag[i][1] = 'ADV'
count = 0
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        POS_tag[i][0] = POS_tag[i][0].replace('-','-')
        if '%' in sentences[p][0]:
            POS_tag[i][0] = POS_tag[i][0].replace('٪', '%')
        if 'متاسفانه' in sentences[p][0]:
            POS_tag[i][0] = POS_tag[i][0].replace('متأسفانه', 'متاسفانه')
        if 'متأسفانه' in sentences[p][0]:
            POS_tag[i][0] = POS_tag[i][0].replace('متاسفانه'  ,'متأسفانه')
        if 'مأنوسی' in sentences[p][0]:
            POS_tag[i][0] = POS_tag[i][0].replace('مانوسی'  ,'مأنوسی')
        if 'مأیوس' in sentences[p][0]:
            POS_tag[i][0] = POS_tag[i][0].replace('مایوس'  ,'مأیوس')
        if 'مانوسی' in sentences[p][0]:
            POS_tag[i][0] = POS_tag[i][0].replace('مأنوسی', 'مانوسی')
        if 'تأخیر' in sentences[p][0]:
            POS_tag[i][0] = POS_tag[i][0].replace('تاخیر', 'تأخیر')

        if 'جرأت' in sentences[p][0]:
            POS_tag[i][0] = POS_tag[i][0].replace('جرات', 'جرأت')
        if 'ارتقأش' in sentences[p][0]:
            POS_tag[i][0] = POS_tag[i][0].replace('ارتقاش', 'ارتقأش')

        aliyeh = 'عالیــــــــــــــــــــــــــــــــــــــــه'

        if aliyeh in sentences[p][0]:
            POS_tag[i][0] = POS_tag[i][0].replace('عالیه', aliyeh)
        if 'اَبَر' in sentences[p][0]:
            if POS_tag[i][0] ==  'ابر':
                POS_tag[i][0] = 'اَبَر'
        if 'میــــــگن' in sentences[p][0]:
            if POS_tag[i][0] ==  'میگن':
                POS_tag[i][0] = 'میــــــگن'
        if 'سِت' in sentences[p][0]:
            if POS_tag[i][0] ==  'ست':
                POS_tag[i][0] = 'سِت'
        if 'نویـز' in sentences[p][0]:
            if POS_tag[i][0] ==  'نویز':
                POS_tag[i][0] = 'نویـز'

        if 'تبریـز' in sentences[p][0]:
            if POS_tag[i][0] ==  'تبریز':
                POS_tag[i][0] = 'تبریـز'

        if 'بسیـار' in sentences[p][0]:
            if POS_tag[i][0] ==  'بسیار':
                POS_tag[i][0] = 'بسیـار'
        if 'اِس' in sentences[p][0]:
            if POS_tag[i][0] ==  'اس':
                POS_tag[i][0] = 'اِس'

        if '،' not in sentences[p][0]:
            POS_tag[i][0] = POS_tag[i][0].replace('،', ',')
        if '»' not in sentences[p][0]:
            POS_tag[i][0] = POS_tag[i][0].replace('»', '"')
        if '«' not in sentences[p][0]:
            POS_tag[i][0] = POS_tag[i][0].replace('«', '"')
POS_tags[894][0][0] = 'طراحی'
POS_tags[4096][20][0] = '---------------------------------------------------------------------------------'
POS_tags[6664][30][0]= '---------'
POS_tags[6664][84][0]= '--------------------'
POS_tags[7421][0][0]= '...'
POS_tags[7761][0][0]= '...'
POS_tags[489][45][0]= 'خصیصه ی'
POS_tags[505][13][0]= 'قاِئل'
POS_tags[541][5][0]= sentences[541][0][22:25]
POS_tags[586][12][0] = 'استفاده ی'
POS_tags[805][120][0] = 'شارِژ'
POS_tags[839][13][0]= 'قاِئل'
POS_tags[823][45][0]= 'خصیصه ی'
POS_tags[1304][6][0]= 'نسبتأ'
POS_tags[2093][75][0]= '۳---'
POS_tags[2093][84][0]= '۳---'
POS_tags[2093][19][0]= '۳---'
POS_tags[2093][61][0]= '۳---'
POS_tags[2093][96][0]= '۳---'
POS_tags[3380][1][0] = 'متأسفانه'
POS_tags[3380][1][0] = 'متأسفانه'

















#*******************************
# these changes were made later
changes = set() # these tags will be given to the dependency parser once again
verbs_with_heh = []
with open('verb-hehs.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("\n")
    for i in range(len(strings)):
        verbs_with_heh.append(strings[i])

adjectives_with_heh = []
with open('heh-faults.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("\n")
    for i in range(len(strings)):
        adjectives_with_heh.append(strings[i])

nouns_with_heh = []
with open('noun-hehs.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("\n")
    for i in range(len(strings)):
        nouns_with_heh.append(strings[i])
adjective_asts = []
noun_asts = []
with open('asts.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("\n")
    for i in range(len(strings)):
        noun_asts.append(strings[i])

with open('adjective-asts.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("\n")
    for i in range(len(strings) ):
        adjective_asts.append(strings[i])
POS_tags[6002][23][1] = 'N'
changes.add(6002)
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] == 'فوق' and POS_tag[i + 1][0] == 'العاده':
            changes.add(p)
            if  i + 2 < len(POS_tag) and POS_tag[i + 2][1] == 'AJ':
                POS_tag[i][1] = 'ADV'
            else:
                POS_tag[i][1] = 'AJ'
            POS_tag[i][0] = 'فوق العاده'
            if i + 2 < len(POS_tag) and (POS_tag[i + 2][0] == 'ای' or POS_tag[i + 2][0] == 'ایه'):
                POS_tag[i][0] = 'فوق العاده' + " " + POS_tag[i + 2][0]
                POS_tag[i + 2][0] = 'eliminate'
            if i + 2 < len(POS_tag) and POS_tag[i + 2][0] == 'اس':
                POS_tag[i + 2][1] = 'V'
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] == 'ای' and POS_tag[i - 1][1] == 'AJ':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + "ای"
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] in verbs_with_heh:
            changes.add(p)
            POS_tag[i][1] = 'V'

print(POS_tags[2008])
print(len(POS_tags[2008]))
for p,POS_tag in enumerate(POS_tags):
    added_elements = []
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] in adjectives_with_heh:
            changes.add(p)
            POS_tag[i][1] = 'AJ'
            POS_tag[i][0] = POS_tag[i][0][0:-1]
            added_elements.append([])
            added_elements[-1].append(i+len(added_elements))
            added_elements[-1].append('است')
            added_elements[-1].append('V')
            # POS_tags[p].insert(i+1,[])
            # POS_tags[p][i+1].append('است')
            # POS_tags[p][i+1].append('V')
    for element in added_elements:
        POS_tags[p].insert(element[0],[element[1],element[2]])
for p,POS_tag in enumerate(POS_tags):
    added_elements = []
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] in adjective_asts:
            changes.add(p)
            POS_tag[i][1] = 'AJ'
            POS_tag[i][0] = POS_tag[i][0][0:-2]
            added_elements.append([])
            added_elements[-1].append(i + len(added_elements))
            added_elements[-1].append('است')
            added_elements[-1].append('V')
            # POS_tags[p].insert(i+1,[])
            # POS_tags[p][i+1].append('است')
            # POS_tags[p][i+1].append('V')
    for element in added_elements:
        POS_tags[p].insert(element[0], [element[1], element[2]])
POS_tags[7843][1][1] = 'AJ'
changes.add(7843)

for p,POS_tag in enumerate(POS_tags):
    added_elements = []
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] in nouns_with_heh:
            changes.add(p)
            POS_tag[i][1] = 'N'
            POS_tag[i][0] = POS_tag[i][0][0:-1]
            added_elements.append([])
            added_elements[-1].append(i + len(added_elements))
            added_elements[-1].append('است')
            added_elements[-1].append('V')
            # POS_tags[p].insert(i+1,[])
            # POS_tags[p][i+1].append('است')
            # POS_tags[p][i+1].append('V')
    for element in added_elements:
        POS_tags[p].insert(element[0], [element[1], element[2]])
for p,POS_tag in enumerate(POS_tags):
    added_elements = []
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] in noun_asts:
            changes.add(p)
            POS_tag[i][1] = 'N'
            POS_tag[i][0] = POS_tag[i][0][0:-2]
            added_elements.append([])
            added_elements[-1].append(i + len(added_elements))
            added_elements[-1].append('است')
            added_elements[-1].append('V')
            # POS_tags[p].insert(i+1,[])
            # POS_tags[p][i+1].append('است')
            # POS_tags[p][i+1].append('V')
    for element in added_elements:
        POS_tags[p].insert(element[0], [element[1], element[2]])
for p,POS_tag in enumerate(POS_tags):
    added_elements = []
    for i in range(len(POS_tag)):
        if  POS_tag[i][0].endswith('ترینه'):
            changes.add(p)
            POS_tag[i][1] = 'AJ'
            POS_tag[i][0] = POS_tag[i][0][0:-1]
            added_elements.append([])
            added_elements[-1].append(i + len(added_elements))
            added_elements[-1].append('است')
            added_elements[-1].append('V')
            # POS_tags[p].insert(i+1,[])
            # POS_tags[p][i+1].append('است')
            # POS_tags[p][i+1].append('V')
    for element in added_elements:
        POS_tags[p].insert(element[0], [element[1], element[2]])

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] == 'ترین':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] == 'تره':
            changes.add(p)
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + 'تره'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
bad_tares = ['گستره', 'استره']
for p,POS_tag in enumerate(POS_tags):
    added_elements = []
    for i in range(len(POS_tag)):
        if POS_tag[i][0].endswith('تره') and POS_tag[i][0] not in bad_tares:
            changes.add(p)
            POS_tag[i][1] = 'AJ'
            POS_tag[i][0] = POS_tag[i][0][0:-1]
            if POS_tag[i][0] == 'بخش تر':
                POS_tag[i - 1][0]= POS_tag[i-1][0] + " " + POS_tag[i][0]
                POS_tag[i-1][1] = 'AJ'
                POS_tag[i][1] = 'V'
                POS_tag[i][0] = 'است'
            else:
                added_elements.append([])
                added_elements[-1].append(i + len(added_elements))
                added_elements[-1].append('است')
                added_elements[-1].append('V')
                # POS_tags[p].insert(i+1,[])
                # POS_tags[p][i+1].append('است')
                # POS_tags[p][i+1].append('V')
    for element in added_elements:
        POS_tags[p].insert(element[0], [element[1], element[2]])


for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] == 'تر':
            changes.add(p)
            POS_tag[i - 1][1] = 'AJ'
            if POS_tag[i - 1][0] != 'بخش':
                POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + 'تر'
                POS_tag[i][0] = 'eliminate'
            else:
                POS_tag[i - 2][0] = POS_tag[i - 2][0] + " " + POS_tag[i - 1][0] +' '+ 'تر'
                POS_tag[i - 2][1] = 'AJ'
                POS_tag[i-1][0] = 'eliminate'
                POS_tag[i][0] = 'eliminate'

    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] == ('بی') :
            if i > 0 and POS_tag[i - 1][0] == ('اس'):
                continue
            changes.add(p)
            POS_tag[i][1] = 'AJ'
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] == ('نظیر') and  i > 0 and POS_tag[i - 1][0] == ('کم'):
            changes.add(p)
            POS_tag[i-1][1] = 'AJ'
            POS_tag[i-1][0] = 'کم نظیر'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  'صرفه' in POS_tag[i][0] and  i > 0 and POS_tag[i - 1][0] == ('به'):
            changes.add(p)
            if i > 2 and POS_tag[i - 1][0] == ('مقرون'):
                POS_tag[i - 2][0] = POS_tag[i - 2][0] + " "+POS_tag[i - 1][0] + " " + POS_tag[i][0]
                POS_tag[i - 2][1] = "AJ"
                POS_tag[i - 1][0] = 'eliminate'
                POS_tag[i ][0] = 'eliminate'
            else:
                POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i ][0]
                POS_tag[i - 1][1] = "AJ"
                POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] == ('جابه') :
            changes.add(p)
            POS_tag[i][1] = 'AJ'
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  'کیفیت' in POS_tag[i][0] and  i > 0 and POS_tag[i - 1][0] == ('با'):
            changes.add(p)
            POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = "AJ"
            POS_tag[i][0] = 'eliminate'
        POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'اند' :
            changes.add(p)
            if POS_tag[i - 1][1] == "AJ":
                POS_tag[i][1] = "V"
            else:
                POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
                POS_tag[i - 1][1] = "V"
                POS_tag[i][0] = 'eliminate'
        POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  'پسند' in POS_tag[i][0] and  i > 0:
            changes.add(p)
            POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = "AJ"
            POS_tag[i][0] = 'eliminate'
        POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  'نقص' in POS_tag[i][0] and  i > 0 and  (POS_tag[i - 1][0] == 'بدون' or POS_tag[i - 1][0] == 'کم'):
            changes.add(p)
            POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = "AJ"
            POS_tag[i][0] = 'eliminate'
        POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  'ارزش' in POS_tag[i][0] and  i > 0 and  (POS_tag[i - 1][0] == 'بدون' or POS_tag[i - 1][0] == 'کم' or
                                                     POS_tag[i - 1][0] == 'با'):
            changes.add(p)
            POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = "AJ"
            POS_tag[i][0] = 'eliminate'
        POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  'قبول' in POS_tag[i][0] and  i > 0 and  (POS_tag[i - 1][0] == 'قابل' or POS_tag[i - 1][0] == 'غیرقابل'):
            changes.add(p)
            POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = "AJ"
            POS_tag[i][0] = 'eliminate'
        POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] ==  'العادست' :
            changes.add(p)
            POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + "العاده"
            POS_tag[i - 1][1] = "AJ"
            POS_tag[i][0] = 'است'
            POS_tag[i][1] = 'V'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'ایم' :
            changes.add(p)
            POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = "V"
            POS_tag[i][0] = 'eliminate'
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'اید' :
            changes.add(p)
            POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = "V"
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'ام' :
            if POS_tag[i-1][1] == 'N' or POS_tag[i-1][1] == 'V':
                changes.add(p)
                POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
                POS_tag[i][0] = 'eliminate'
            elif POS_tag[i-1][0] == 'راضی' :
                changes.add(p)
                POS_tag[i][1] = 'V'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
adjectives_with_yeh = ['حرفه','نقره','هسته','سلیقه','چندرسانه','معرکه','شخصی', 'ژله' ,'کننده','شیشه']
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'ای' :
            changes.add(p)
            if POS_tag[i-1][0] in  adjectives_with_yeh:
                if POS_tag[i-1][0] != 'کننده' and POS_tag[i-1][0] != 'هسته':
                    POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
                    POS_tag[i][1] = "AJ"
                    POS_tag[i][0] = 'eliminate'
                else:
                    POS_tag[i - 2][0] = POS_tag[i - 2][0] + " " + POS_tag[i - 1][0] + ' ' + 'ای'
                    POS_tag[i - 2][1] = 'AJ'
                    POS_tag[i - 1][0] = 'eliminate'
                    POS_tag[i][0] = 'eliminate'
            else:
                POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
                POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] ==  'العادس' :
            changes.add(p)
            POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + "العاده"
            POS_tag[i - 1][1] = "AJ"
            POS_tag[i][0] = 'است'
            POS_tag[i][1] = 'V'
ignored_verbs = []
with open('verb-flaws.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("\n")
    for i in range(len(strings)):
        ignored_verbs.append(strings[i])

for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] in  ignored_verbs :
            changes.add(p)
            POS_tag[i][1] = 'V'


for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] == 'هسته ای' :
            changes.add(p)
            POS_tag[i][1] = 'AJ'
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] == 'ی' :
            if POS_tag[i-1][0].endswith('ا'):
                changes.add(p)
                POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + "ی"
                POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']





counts = {}



del POS_tags[542][14]
changes.add(542)
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] == 'یه' and i > 0 and  POS_tag[i-1][0] !='.':
            changes.add(p)
            POS_tag[i][0] = 'یک'
del POS_tags[3518][-1]
changes.add(3518)
del POS_tags[3777][3]
changes.add(3777)

POS_tags[3778][10][0] = 'اصغر=۳'
del POS_tags[3778][9]
POS_tags[3778][8][0] = '=' + POS_tags[3778][8][0]
del POS_tags[3778][7]
del POS_tags[3778][1]
changes.add(3778)

del POS_tags[4526][-1]
changes.add(4526)




POS_tags[1492][-1] = []
POS_tags[1492][-1].append('شما')
POS_tags[1492][-1].append ('PRO')
POS_tags[1492].append([])
POS_tags[1492][-1].append('است')
POS_tags[1492][-1].append('V')
POS_tags[1492].append([])
POS_tags[1492][-1].append('۳')
POS_tags[1492][-1].append('NUM')
changes.add(1492)

for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] == 'داغ' :
            changes.add(p)
            POS_tag[i][1] = 'AJ'

POS_tags[5898][27] = []
POS_tags[5898][27].append('سرتر')
POS_tags[5898][27].append('AJ')
POS_tags[5898].insert(28,[])
POS_tags[5898][28].append('است')
POS_tags[5898][28].append('V')

POS_tags[5898].insert(29,[])
POS_tags[5898][29].append('اصغر')
POS_tags[5898][29].append('N')

POS_tags[5898].insert(30,[])
POS_tags[5898][30].append('ولی')
POS_tags[5898][30].append('CONJ')

POS_tags[5898].insert(31,[])
POS_tags[5898][31].append('بی')
POS_tags[5898][31].append('P')
POS_tags[5898][32][0] = 'شیکی'
changes.add(5898)


POS_tags[5918][0][0] = 'عالیــــــــــــــــــــــــــــــــــــــــ'
POS_tags[5918][0][1] = 'AJ'
POS_tags[5918][1][0] = 'است'
POS_tags[5918][1][1] = 'V'
for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if POS_tag[i][0] == 'بخش' and i > 0 and POS_tag[i-1][1] =='N':
            changes.add(p)
            POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if    POS_tag[i][0] == 'قابل'  and i < len(POS_tag) - 1:
            changes.add(p)
            if POS_tag[i+1][0] != 'باز' and POS_tag[i+1][0] != 'درست':
                POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i+1][0]
                POS_tag[i][1] = 'AJ'
                POS_tag[i+1][0] = 'eliminate'
            else:
                POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0] + " " + POS_tag[i + 2][0]
                POS_tag[i][1] = 'AJ'
                POS_tag[i + 1][0] = 'eliminate'
                POS_tag[i + 2][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']


POS_tags[6093][2] = []
POS_tags[6093][2].append('خوب')
POS_tags[6093][2].append('AJ')
POS_tags[6093].insert(3,[])
POS_tags[6093][3].append('است')
POS_tags[6093][3].append('V')
POS_tags[6093].insert(4,[])
POS_tags[6093][4].append('٫')
POS_tags[6093][4].append('PUNC')
POS_tags[6093][38] = []
POS_tags[6093][38].append('با')
POS_tags[6093][38].append('P')
POS_tags[6093].insert(39,[])
POS_tags[6093][39].append('کیفیت')
POS_tags[6093][39].append('N')
changes.add(6093)

del POS_tags[6664][24]
changes.add(6664)

# for p, POS_tag in enumerate(POS_tags):
#     for i in range(len(POS_tag)):
#         if POS_tag[i][0] == 'قابل':
#             print(sentences[p][0])
#             print(len(POS_tag))
#             print(POS_tag[i - 1])
#             print(POS_tag[i])
#             if i < len(POS_tag) - 1:
#                 print(POS_tag[i + 1])
print(len(changes))
with open('POS-tags.txt', 'w',encoding='utf-8') as f:
    for POS_tag in POS_tags:
        f.write(str(POS_tag))
        f.write("@@@")

with open('changes.txt', 'w',encoding='utf-8') as f:
    for change in changes:
        f.write(str(change))
        f.write("\n")















































# POS_tags = []
# dependencies = []
# with open('POS-tags.txt', 'r', encoding='utf-8') as in_file:
#     strings = in_file.read().split("@@@")
#     for i in range(len(strings) - 1):
#         POS_tags.append(eval(strings[i]))
# counter = 0
# import time
# first = time.time()
# t = time.time()
# for POS_tag in POS_tags[0:100]:
#     dep_of_this_tag =
#     dependencies.append([])
#     for d in dep_of_this_tag:
#         dependencies[-1].append(d.)
#     counter += 1
#         if counter %10 == 0:
#             duration = time.time() - t
#             t = time.time()
#             print(str(int(duration)) + " seconds")
#             print(counter)
# with open('DependenciesA.txt', 'w',encoding='utf-8') as f:
#     for deps in dependencies:
#         f.write(str(deps))
#         f.write("@@@")
# dur_passed = int((time.time() - first)/60)
# print(str(dur_passed) + " minutes")










