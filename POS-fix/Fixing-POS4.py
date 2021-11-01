POS_tags = [] #POS tags of each token in a sentence
with open('POS-tags.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("@@@")
    for i in range(len(strings) - 1):
        POS_tags.append(eval(strings[i]))


changed = [17, 98, 140, 186, 265, 284, 514, 588, 605, 617, 620, 632, 637, 642, 658, 668, 750, 774, 778, 848, 899, 924, 970, 989, 1114, 1175, 1211, 1302, 1325, 1327, 1328, 1466, 1484, 1513, 1515, 1524, 1525, 1527, 1535, 1539, 1552, 1553, 1558, 1567, 1581, 1685, 1686, 1689, 1728, 1777, 1788, 1907, 1938, 2002, 2020, 2025, 2057, 2076, 2082, 2110, 2149, 2177, 2180, 2198, 2229, 2234, 2303, 2348, 2371, 2407, 2484, 2520, 2529, 2543, 2559, 2603, 2719, 2725, 2804, 2810, 2888, 2894, 2973, 2974, 3015, 3107, 3108, 3131, 3286, 3437, 3438, 3440, 3441, 3463, 3548, 3567, 3662, 3663, 3779, 3793, 3828, 3837, 3925, 3936, 3990, 4042, 4097, 4150, 4152, 4306, 4675, 4690, 4857, 4956, 4998, 5081, 5082, 5098, 5108, 5243, 5249, 5279, 5413, 5425, 5447, 5459, 5470, 5519, 5532, 5611, 5612, 5662, 5698, 5782, 5854, 6069, 6111, 6177, 6178, 6305, 6338, 6346, 6432, 6506, 6669, 6744, 6962, 7028, 7119, 7137, 7181, 7230, 7264, 7265, 7435, 7476, 7551, 7631, 7633, 7711, 7716, 7725, 7804]
for i in range(len(changed)):
    if changed[i] > 217 and changed[i] < 5371:
        changed[i] -= 1
    elif  changed[i] > 5371 and changed[i] < 5889:
        changed[i] -= 2
    elif  changed[i] > 5889 and changed[i] < 6392:
        changed[i] -= 3
    elif  changed[i] > 6392:
        changed[i] -= 4
print(changed)
for i in changed:
    for t,tag in enumerate(POS_tags[i]):
        if '۳اصغر' in tag[0] :
            POS_tags[i][t][0] = POS_tags[i][t][0].replace('۳اصغر','اصغر')
POS_tags[3778][-4] = 'اصغر='
with open('POS-tags.txt', 'w',encoding='utf-8') as f:
    for POS_tag in POS_tags:
        f.write(str(POS_tag))
        f.write("@@@")
