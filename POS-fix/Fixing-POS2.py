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
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'پائین':
            changes.add(p)
            POS_tag[i][1] = 'AJ'

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'است۳':
            changes.add(p)
            POS_tag[i][1] = 'V'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'آلومنیومی':
            changes.add(p)
            POS_tag[i][1] = 'AJ'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'مجازی':
            changes.add(p)
            POS_tag[i][1] = 'AJ'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'آخری':
            changes.add(p)
            POS_tag[i][1] = 'AJ'

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'آنقدر':
            changes.add(p)
            POS_tag[i][1] = 'ADV'

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'فروختم':
            changes.add(p)
            POS_tag[i][1] = 'V'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'می\u200cخری':
            changes.add(p)
            POS_tag[i][1] = 'V'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'آسان':
            changes.add(p)
            POS_tag[i][1] = 'AJ'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'مرغوب':
            changes.add(p)
            POS_tag[i][1] = 'AJ'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'متوسط':
            changes.add(p)
            POS_tag[i][1] = 'AJ'

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'پاسخگو':
            changes.add(p)
            POS_tag[i][1] = 'AJ'

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'عریض':
            changes.add(p)
            POS_tag[i][1] = 'AJ'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'مفیدی':
            changes.add(p)
            POS_tag[i][1] = 'AJ'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'استایلیش':
            changes.add(p)
            POS_tag[i][1] = 'AJ'

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'متمایز':
            changes.add(p)
            POS_tag[i][1] = 'AJ'

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'گیرا':
            changes.add(p)
            POS_tag[i][1] = 'AJ'

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'بالا':
            changes.add(p)
            POS_tag[i][1] = 'AJ'

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  'قدرتمند' in POS_tag[i][0]  :
            changes.add(p)
            POS_tag[i][1] = 'AJ'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  'زیبای' in POS_tag[i][0]  :
            changes.add(p)
            POS_tag[i][1] = 'AJ'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  'مختلف' in POS_tag[i][0]  :
            changes.add(p)
            POS_tag[i][1] = 'AJ'

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  'باریک' in POS_tag[i][0]  :
            changes.add(p)
            POS_tag[i][1] = 'AJ'

for p, POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if 'عجولان' in POS_tag[i][0]:
            changes.add(p)
            POS_tag[i][1] = 'AJ'


for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  'متناسبی' in POS_tag[i][0]  :
            changes.add(p)
            POS_tag[i][1] = 'AJ'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'آرگونومیک':
            changes.add(p)
            POS_tag[i][1] = 'AJ'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'مدگرا':
            changes.add(p)
            POS_tag[i][1] = 'AJ'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'استثنایی':
            changes.add(p)
            POS_tag[i][1] = 'AJ'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'دیجی'  and i < len(POS_tag) - 1 and POS_tag[i + 1][0] == 'کالا':
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'تلفن'  and i < len(POS_tag) - 1 and POS_tag[i + 1][0] == 'همراه':
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'العاده'  and i > 0 :
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i-1][0] + " " + POS_tag[i][0]
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'همراه'  and i < len(POS_tag) - 1 and POS_tag[i + 1][0] == 'بانک':
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i][1] = 'N'
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']




for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'دوست'  and i < len(POS_tag) - 1 and POS_tag[i + 1][0] == 'داشتنی':
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i][1] = 'AJ'
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'چنگی'  and i < len(POS_tag) - 1 and POS_tag[i + 1][0] == 'به':
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0] + " " + POS_tag[i + 2][0] + " " + POS_tag[i + 3][0]
            POS_tag[i][1] = 'V'
            POS_tag[i + 1][0] = 'eliminate'
            POS_tag[i + 2][0] = 'eliminate'
            POS_tag[i + 3][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'پر'  and i < len(POS_tag) - 1 :
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i][1] = 'ADJ'
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'در'  and i < len(POS_tag) - 1 and POS_tag[i + 1][0] == 'دسترس':
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i][1] = 'AJ'
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'ایده'  and i < len(POS_tag) - 1 and POS_tag[i + 1][0] == 'آل':
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i][1] = 'AJ'
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']


for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'آزار'  and i < len(POS_tag) - 1 and POS_tag[i + 1][0] == 'دهنده':
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i][1] = 'AJ'
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']


for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'برق'  and i < len(POS_tag) - 1 and POS_tag[i + 1][0] == 'گرفتگی':
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i][1] = 'N'
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'سیستم'  and i < len(POS_tag) - 1 and POS_tag[i + 1][0] == 'عامل':
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i][1] = 'N'
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'آسیب'  and i < len(POS_tag) - 1 and POS_tag[i + 1][0] == 'پذیر':
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i][1] = 'AJ'
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

ba_words = ['حال','حالی','حاله','سابقه','صرفه','صرفه تر','قدرت','قدرتی']
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'با'  and i < len(POS_tag) - 1 and POS_tag[i + 1][0] in ba_words:
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i][1] = 'AJ'
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] == 'کنندست':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i - 1][0] + " " + "کنند"
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'ست'
            POS_tag[i][1] = 'V'

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] == 'متری':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i - 1][0] + " " + "متری"
            POS_tag[i - 1][1] = 'AJ'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] == 'ایش':
            changes.add(p)
            POS_tag[i-1][0] = POS_tag[i - 1][0] + " " + "ایش"
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] == 'ضد':
            changes.add(p)
            POS_tag[i][0] = POS_tag[i][0] + " " + POS_tag[i + 1][0]
            POS_tag[i][1] = 'AJ'
            POS_tag[i + 1][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']


for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'آماده'  and i < len(POS_tag) - 2 and POS_tag[i + 1][0] ==  'به' and POS_tag[i + 1][0] ==  'کار':
            changes.add(p)
            POS_tag[i-2][0] = "آماده به کار"
            POS_tag[i-2][1] = 'AJ'
            POS_tag[i -1][0] = 'eliminate'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']

for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'نقل'  and i < len(POS_tag) - 2 and POS_tag[i + 1][0] ==  'و' and POS_tag[i + 1][0] ==  'نقل':
            changes.add(p)
            POS_tag[i-2][0] = "حمل و نقل"
            POS_tag[i-2][1] = 'AJ'
            POS_tag[i -1][0] = 'eliminate'
            POS_tag[i][0] = 'eliminate'
    POS_tags[p] = [tag for tag in POS_tag if tag[0] != 'eliminate']


for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0] ==  'بسیار'  :
            changes.add(p)
            POS_tag[i][1] = 'ADV'
            POS_tag[i + 1][1] = 'AJ'
for p,POS_tag in enumerate(POS_tags):
    for i in range(len(POS_tag)):
        if  POS_tag[i][0]  == 'زیادم':
            changes.add(p)
            POS_tag[i][1] = 'AJ'
print(len(changes))
with open('POS-tags.txt', 'w',encoding='utf-8') as f:
    for POS_tag in POS_tags:
        f.write(str(POS_tag))
        f.write("@@@")

with open('changes2.txt', 'w',encoding='utf-8') as f:
    for change in changes:
        f.write(str(change))
        f.write("\n")

