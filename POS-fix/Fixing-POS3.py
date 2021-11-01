POS_tags = [] #POS tags of each token in a sentence
with open('POS-tags.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("@@@")
    for i in range(len(strings) - 1):
        POS_tags.append(eval(strings[i]))

sentences = [] #each element will be in the form of text,aspects,opinions,english words,numbers

with open('sentences.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("@@@")
    for i in range(len(strings) - 1):
        sentences.append(eval(strings[i]))
changes = set()
adjectives = ['معرکه','استیل','حرفه ای','سریعی','مبتدیانه','اینترنتی','کیبردی','لمسی','نرمی','خفن']
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  in adjectives:
            changes.add(p)
            POS_tag[i][1] = 'AJ'




for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'متاسفانه':
            changes.add(p)
            POS_tag[i][1] = 'ADV'




for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'دست':
            changes.add(p)
            POS_tag[i][1] = 'N'

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'مگاپیکسلی':
            POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'مبتدیانه':
            changes.add(p)
            POS_tag[i][1] = 'AJ'


for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'کرد'  and i > 0 :
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'V'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'هایی'  and i > 0 :
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']


for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'می\u200cگیره'  and i > 0 and POS_tag[i-1][0] ==  'فیلم':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'V'
            POS_tag[i][0] = 'eliminate'
        elif  POS_tag[i][0] ==  'نمونه'  and i > 0 and POS_tag[i-1][0] ==  'عقب':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'V'
            POS_tag[i][0] = 'eliminate'
        elif  POS_tag[i][0] ==  'شده'  and i > 0 and POS_tag[i-1][0] ==  'کشیده':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'V'
            POS_tag[i][0] = 'eliminate'
        elif POS_tag[i][0] ==  'است'  and i > 0 and POS_tag[i-1][0] ==  'ورزیده':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'V'
            POS_tag[i][0] = 'eliminate'
        elif POS_tag[i][0] ==  'میکنه'  and i > 0 and POS_tag[i-1][0] ==  'رد':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'V'
            POS_tag[i][0] = 'eliminate'
        elif POS_tag[i][0] ==  'باش'  and i > 0 and POS_tag[i-1][0] ==  'آماده':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'N'
            POS_tag[i][0] = 'eliminate'
        elif POS_tag[i][0] ==  'دارد'  and i > 0 and POS_tag[i-1][0] ==  'وجود':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'V'
            POS_tag[i][0] = 'eliminate'
        elif POS_tag[i][0] ==  'میدین'  and i > 0 and POS_tag[i-1][0] ==  'دارین':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'V'
            POS_tag[i][0] = 'eliminate'
        elif POS_tag[i][0] == 'دست' and i > 0 and POS_tag[i - 1][0] == 'به':
                changes.add(p)
                POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0] + " " + POS_tag[i + 1][0]
                POS_tag[i - 1][1] = 'V'
                POS_tag[i][0] = 'eliminate'
                POS_tag[i + 1][0] = 'eliminate'
        elif POS_tag[i][0] ==  'پلیر'  and i > 0 and POS_tag[i-1][0] ==  'موزیک':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'N'
            POS_tag[i][0] = 'eliminate'
        elif 'ندار' in POS_tag[i][0] and i > 0 and POS_tag[i-1][0] ==  'صورت':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'V'
            POS_tag[i][0] = 'eliminate'
        elif POS_tag[i][0] ==  'بندی'  and i > 0 and POS_tag[i-1][0] ==  'جمع':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'N'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

print("heyyyyyy")

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'کنید'  and i > 0:
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'V'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']








for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] == 'شده' and i > 0 and POS_tag[i-1][0].endswith('ه'):
            if i < len(POS_tag) - 1 and POS_tag[i][0] == 'است':
                changes.add(p)
                POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0] + " " + POS_tag[i + 1][0]
                POS_tag[i - 1][1] = 'V'
                POS_tag[i][0] = 'eliminate'
                POS_tag[i + 1][0] = 'eliminate'
            else:
                changes.add(p)
                POS_tag[i - 1][0] = POS_tag[i - 1][0] + " " + POS_tag[i][0]
                POS_tag[i - 1][1] = 'V'
                POS_tag[i][0] = 'eliminate'


for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'گرفتن'  and i > 0 and POS_tag[i-1][0] ==  'دست':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'N'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']




print("heyyyy")




for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if   'پذیرد' in POS_tag[i][0] :
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'V'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'گیگا'  and i > 0 and i < len(POS_tag) - 1:
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0] + " " + POS_tag[i+1][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
            POS_tag[i+1][0] = 'eliminate'
        elif POS_tag[i][0] ==  'میلی'  and i > 0 and i < len(POS_tag) - 1:
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0] + " " + POS_tag[i+1][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
            POS_tag[i+1][0] = 'eliminate'
        elif POS_tag[i][0] ==  'سانتی'  and i > 0 and i < len(POS_tag) - 1:
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0] + " " + POS_tag[i+1][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
            POS_tag[i+1][0] = 'eliminate'
        elif POS_tag[i][0] ==  'کیلو'  and i > 0 and i < len(POS_tag) - 1:
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0] + " " + POS_tag[i+1][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
            POS_tag[i+1][0] = 'eliminate'
        elif 'روز' in POS_tag[i][0]   and i > 0 and POS_tag[i-1][0] ==  'به':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
        elif 'رسانه' in POS_tag[i][0]   and i > 0 and POS_tag[i-1][0] ==  'چند':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']








for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  'گردد' in POS_tag[i][0]   and i > 0 :
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
measures = ['میلیمتری','میلیمتر','سانتیمتری','سانتیمتر','اینچی','اینچ','متری','متر','کیلومتری','کیلومتر' ,'گیگاهرتز','گیگاهرتزی']
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if   POS_tag[i][0] in measures and i > 0 :
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']



for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'افزار'  and i > 0 and POS_tag[i-1][0] ==  'نرم':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'N'
            POS_tag[i][0] = 'eliminate'
        elif POS_tag[i][0] ==  'مانندی'  and i > 0 and POS_tag[i-1][0] ==  'استیل':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'N'
            POS_tag[i][0] = 'eliminate'
        elif POS_tag[i][0] ==  'استیل'  and i > 0 and POS_tag[i-1][0] ==  'خوش':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
        elif (POS_tag[i][0] ==  'ارزون' or POS_tag[i][0] ==  'ارزان' )  and i < len(POS_tag) - 1 and 'قیمت' in POS_tag[i+1][0] :
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i+1][0]
            POS_tag[i][1] = 'AJ'
            POS_tag[i+1][0] = 'eliminate'
        elif POS_tag[i][0] ==  'پرستیژ'  and i > 0 and POS_tag[i-1][0] ==  'با':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
        elif POS_tag[i][0] ==  'نمایش'  and i > 0 and POS_tag[i-1][0] ==  'صفحه':
            changes.add(p)
            if 'صفحه ی نمایش'in sentences[p][0]:
                POS_tag[i-1][0] = 'صفحه ی نمایش'
            else:
                POS_tag[i - 1][0] = 'صفحه نمایش'
            POS_tag[i - 1][1] = 'N'
            POS_tag[i][0] = 'eliminate'
        elif POS_tag[i][0] ==  'انگیز'  and i > 0 :
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']


for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'شگفت'  and i < len(POS_tag)-1 :
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i+1][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'






for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  'کنی' in POS_tag[i][0] and i > 0:
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'V'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

with open('POS-tags.txt', 'w',encoding='utf-8') as f:
    for POS_tag in POS_tags:
        f.write(str(POS_tag))
        f.write("@@@")

# for p,POS_tag in enumerate(POS_tags):
#     for i in range(len(POS_tag)):
#         if  POS_tag[i][1] ==  'V'  and i > 0 and POS_tag[i-1][1] ==  'V' and POS_tag[i-1][1] !=  'ممنون':
#             if POS_tag[i-1][0] == 'بپردازید' or POS_tag[i-1][0] == 'کنیم' or POS_tag[i][0] == 'خریدم' or POS_tag[i][0] == 'نمی\u200cتواند'
#             changes.add(p)
#             POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
#             POS_tag[i - 1][1] = 'N'
#             POS_tag[i][0] = 'eliminate'
#     POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']