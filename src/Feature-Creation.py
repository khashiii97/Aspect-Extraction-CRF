"""
This file is for creating the feature vector for each word in our sentences
the POS tagged sentences lie in the POS-tags.txt file.
the parsing tree dependencies lie in the Dependencies directory
"""
import  os
import pandas as pd
sentences = [] #each element will be in the form of text,aspects,opinions,english words,numbers
with open('sentences.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("@@@")
    for i in range(len(strings) - 1):
        sentences.append(eval(strings[i]))


POS_tags = [] #POS tags of each token in a sentence
with open('POS-fix/POS-tags.txt', 'r', encoding='utf-8') as in_file:
    strings = in_file.read().split("@@@")
    for i in range(len(strings) - 1):
        POS_tags.append(eval(strings[i]))
dependencies = []
with open('Dependencies-v3.txt',encoding="utf8") as file:
    strings = file.read().split("@@@")
    for i in range(len(strings) - 1):
        dependencies.append(eval(strings[i]))
for d in dependencies:
    for deps in d:
        for i in range(len(deps)):
            deps[i] = deps[i] - 1
# del dependencies[217]
# del dependencies[5371]
# del dependencies[5889]
# del dependencies[6392]

print(len(dependencies))
print(len(sentences))
print(len(POS_tags))
# for i,dep in enumerate(dependencies):
#     if len(POS_tags[i]) != len(dependencies[i]):
#         print(len(dependencies[i]))
#         print(len(POS_tags[i]))
#         print(len(POS_tags[i + 1]))
#         print("*************")

index_interval_of_tokens =[] # indicating the start and end index of each token in each sentence
counter = 0
for s,sentence in enumerate(sentences):
    index_interval_of_tokens.append([])
    current_index = 0
    # print(s)
    # print(sentence[0])
    # print(POS_tags[s])
    # print("+++++")
    for t,token in enumerate(POS_tags[s]):
        # print(token)
        # print(t)
        # print(sentence[0][current_index])
        while sentence[0][current_index] != token[0][0]:
            # print(current_index)
            # print(token[0])
            # print(sentence[0][current_index])
            # print("####")
            # print(token[0][0])
            # print("______________")
            current_index += 1
        length = len(token[0])
        if token[0].replace('\u200c',' ') != sentence[0][current_index: current_index + length]:
            temp_token = token[0].replace('\u200c',' ')
            while temp_token[-1] != sentence[0][current_index: current_index + length][-1]:# some spaces have extended the actual word in the sentence
                length += 1
            if temp_token.replace(' ', '') != sentence[0][current_index: current_index + length].replace(' ', ''):
                print("alertttttt")
                print(s)
                print(token[0])
                print(sentence[0][current_index:current_index + length])
                print(sentence[0])
                print(current_index)
                print(length)
                print("----------")
        index_interval_of_tokens[-1].append([])
        index_interval_of_tokens[-1][-1].append(current_index)
        index_interval_of_tokens[-1][-1].append(current_index + length)
        # if temp_token.replace(' ','') != sentence[0][current_index: current_index + length].replace(' ',''):
        #     print("alertttttt")
        #     print()

                # counter += 1
                # print(token[0])
                # print(sentence[0][current_index:current_index + length])
                # print(sentence[0])
                # print(current_index)
                # print(length)
                # print("+++++++++++")


            # break

        current_index += length
# since we will label the tokens conforming to the IOB scheme, we will indicate the beginning aspects and inside aspects in each sentence
beginning_of_aspects =[[] for s in sentences] # comprises of lists which each demonstrate the tokens that start an aspect in a sentence
inside_of_aspects = [[] for s in sentences]# # comprises of lists which each demonstrate the tokens that reside inside an aspect in a sentence

for s,sentence in enumerate(sentences):
    aspect_intervals = sentence[1]
    for t,token_interval in enumerate(index_interval_of_tokens[s]):
        start = token_interval[0]
        for intervals in aspect_intervals:
            if intervals[1][0] == start:
                beginning_of_aspects[s].append(t)
                break
            if intervals[1][0] < start and intervals[1][1] >= start:
                inside_of_aspects[s].append(t)
                break
# p = 170
# print(POS_tags[p])
# print(sentences[p])
# print(index_interval_of_tokens[p])
# for t,tag in enumerate(POS_tags[p]):
#     if t in beginning_of_aspects[p]:
#         print(tag[0]," : B")
#     elif t in inside_of_aspects[p]:
#         print(tag[0], " : I")
#     else:
#         print(tag[0], " : O")
# print("*****")

opinion_tokens = [[] for s in sentences] #comprises of lists which each demonstrate the tokens that are a part of an opinion word

for s,sentence in enumerate(sentences):
    opinion_intervals = sentence[2]
    for t,token_interval in enumerate(index_interval_of_tokens[s]):
        start = token_interval[0]
        for intervals in opinion_intervals:
            if intervals[1] <= start <= intervals[2]  :
                opinion_tokens[s].append(t)
                break
# for it in se:
#     print(it)
# p = 1800
# print(sentences[p])
# print(index_interval_of_tokens[p])
# for t,tag in enumerate(POS_tags[p]):
#     if t in opinion_tokens[p]:
#         print(tag[0])
not_useful = ['است','دارد','ولی','البته','']
short_dependency_paths = [set() for s in sentences]# indicates the tokens in a sentence that have a direct a link to an opinion word, as stated in the paper. these will have a dln label of true
degree_two_deps = [set() for s in sentences]
for s,sentence in enumerate(sentences):
    deps = dependencies[s]
    for t,token in enumerate(POS_tags[s]):
        if t in opinion_tokens[s]   :
            continue
        added = False
        for node in deps[t]:# each node is the number of a token which t has a direct link to it
            if node in opinion_tokens[s]:
                short_dependency_paths[s].add(t)
                added = True
                break
        if added == True:
            continue
        for opinion_token in opinion_tokens[s]:# check weather a path from an opinion token to this token exists
            if t in deps[opinion_token]:
                if POS_tags[s][t][0] == 'است' and t in inside_of_aspects[s] + beginning_of_aspects[s] :
                    print("heyyyyy")
                    print(POS_tags[s][t-1][0])
                    print(POS_tags[s][t][0])
                short_dependency_paths[s].add(t)
                break

for s,sentence in enumerate(sentences):
    deps = short_dependency_paths[s]
    for d in deps:
        for t, token in enumerate(POS_tags[s]):
            if t not in opinion_tokens[s] and t not in short_dependency_paths[s] and (t in dependencies[s][d] or d in dependencies[s][t]) :
                degree_two_deps[s].add(t)
    short_dependency_paths[s] = list(short_dependency_paths[s])
    short_dependency_paths[s] += list(degree_two_deps[s])
a = 0
# for p,path in enumerate(short_dependency_paths):
#     for s,sh in enumerate(path):
#         if POS_tags[p][sh]
short_dependency_paths_temp =short_dependency_paths
short_dependency_paths = [[] for s in sentences]
for p,path in enumerate(short_dependency_paths_temp):
    for s,sh in enumerate(path):
        if POS_tags[p][sh][0] in not_useful:
            short_dependency_paths_temp[p][s] = -1
    short_dependency_paths[p] = [i for i in short_dependency_paths_temp[p] if i != -1]
print(short_dependency_paths[9])


for s,sentence in enumerate(sentences):
    for t,tag in enumerate(POS_tags[s]):
        if t > 0 and 'ترین' in POS_tags[s][t-1][0] and POS_tags[s][t][1] == 'N':
            if t not in short_dependency_paths[s]:
                short_dependency_paths[s].append(t)

counter_rights = 0
counter_all = 0
counter_allr = 0
for p,path in enumerate(short_dependency_paths):
    counter_allr += len(path)
    counter_all += len(beginning_of_aspects[p])
    counter_all += len(inside_of_aspects[p])
    for token in path:
        if token in beginning_of_aspects[p] or token in inside_of_aspects[p] :
            counter_rights += 1
print(counter_rights)
print(counter_all)
print((counter_rights/counter_all) * 100)
print("****")
print(counter_allr)
print((counter_rights/counter_allr) * 100)

p = 6857
print(POS_tags[p])
print(sentences[p])
print(index_interval_of_tokens[p])
for t,tag in enumerate(POS_tags[p]):
    if t in beginning_of_aspects[p]:
        print(tag[0]," : B")
    elif t in inside_of_aspects[p]:
        print(tag[0], " : I")
    else:
        print(tag[0], " : O")
print("*****")
for s in short_dependency_paths[p]:
    print(POS_tags[p][s][0])

word_distances = [set() for s in sentences]# tokens that are the closest noun phrase to an opinion word. noun phrases are a group of noun and modifiers
for s,sentence in enumerate(sentences):
    for opinion_token in opinion_tokens[s]:
        distance_before_token = 0 # the distance of the closest noun phrase before the opinion word
        distance_after_token = 0
        before_tokens = set()
        after_tokens = set()
        t = opinion_token - 1
        found = False
        while t >= 0 :
            if (POS_tags[s][t][1] == 'N' or POS_tags[s][t][1] == 'PRO') :
                if t not in opinion_tokens[s]:
                    before_tokens.add(t)
                    if found == False:
                        found = True
                else:
                    distance_before_token += 1
                t -= 1
            else:
                if found == True:
                    break
                else:
                    if POS_tags[s][t][0] == '.':
                        break # sentence has ended
                    t -= 1
                    distance_before_token += 1
        t = opinion_token + 1
        found = False
        while t < len(POS_tags[s]) :
            if (POS_tags[s][t][1] == 'N' or POS_tags[s][t][1] == 'PRO') :
                if t not in opinion_tokens[s]:
                    after_tokens.add(t)
                    if found == False:
                        found = True
                else:
                    distance_after_token += 1
                t += 1
            else:
                if found == True:
                    break
                if POS_tags[s][t][0] == '.':
                    break  # sentence has ended
                else:
                    t += 1
                    distance_after_token += 1
        if len(before_tokens) > 0:
            if len(after_tokens)== 0:
                for i in before_tokens:
                    word_distances[s].add(i)
            else:
                if distance_before_token < distance_after_token:
                    for i in before_tokens:
                        word_distances[s].add(i)
                else:
                    for i in after_tokens:
                        word_distances[s].add(i)
        elif len(after_tokens)!= 0:
            for i in after_tokens:
                word_distances[s].add(i)
for w in range(len(word_distances)):
    word_distances[w] = list(word_distances[w])
# print(word_distances)
# print("************")
# for w in word_distances[p]:
#     print(POS_tags[p][w][0])
# counter_rights = 0
# counter_all = 0
# for p,path in enumerate(word_distances):
#     # counter_all += len(path)
#     counter_all += len(beginning_of_aspects[p])
#     counter_all += len(inside_of_aspects[p])
#     for token in path:
#         if token in beginning_of_aspects[p] or token in inside_of_aspects[p]:
#             counter_rights += 1
# print(counter_rights)
# print(counter_all)
# print((counter_rights/counter_all) * 100)

# counter = 0
# counter1 = 0
# counter2 = 0
# for s in range(len(short_dependency_paths)):
#     counter1 += len(word_distances[s])
#     counter2 += len(short_dependency_paths[s])
#     for d in word_distances[s]:
#         if d in short_dependency_paths[s] and d in inside_of_aspects[s] + beginning_of_aspects[s]:
#             counter += 1
# print(counter)
# print(counter2)
# print(counter1)
opinion_sentence = [True for i in range(len(sentences))] #sSn
for s,sentence in enumerate(sentences):
    if len(sentence[2]) == 0: # the sentence doesn't contain an opinion expression
        opinion_sentence[s] = False
# print(opinion_sentence)


for s in range(len(POS_tags)):
    for t in beginning_of_aspects[s] + inside_of_aspects[s]:
        if POS_tags[s][t][0] == 'این':
            print("hey")
            print(s)
            print(sentences[s])
            print(POS_tags[s][t-1][0])
            print(POS_tags[s][t][0])
            print(POS_tags[s][t+1][0])
            print("*********")

for p,pos in enumerate(POS_tags):
    pointer = 0
    num_pointer = 0
    for t,tag in enumerate(pos):
        if tag[0] == 'اصغر' :
            POS_tags[p][t][0] = sentences[p][3][pointer]
            pointer += 1
        # elif tag[1] == 'NUM' :
        #     POS_tags[p][t][0] = sentences[p][4][num_pointer]
        #     num_pointer += 1
# sentence_features = {}
# feature_dataFrames = pd.Panel(sentence_features)
# for s,sentence in enumerate(sentences):
#     token = [POS_tags[s][i][0] for i in range(len (POS_tags[s]))]
#     pos = [POS_tags[s][i][1] for i in range(len (POS_tags[s]))]
#     dln = [False for i in range(len(POS_tags[s]))]
#     for path in short_dependency_paths[s]:
#         dln[path] = True
#     wrdDist = [False for i in range(len(POS_tags[s]))]
#     for dist in word_distances[s]:
#         wrdDist[dist] = True
#     sSn = opinion_sentence[s]
#     label = ['' for i in range(len(POS_tags[s]))]
#     for i in beginning_of_aspects[s]:
#         label[i] = 'B'
#     for i in inside_of_aspects[s]:
#         label[i] = 'I'
#     for i in range(len(label)):
#         if label[i]== '':
#             label[i] = 'O'
#     data ={'token':token,'pos':pos,'dln':dln,'wrdDist':wrdDist,'sSn':sSn,'label':label}
#     tokens = pd.DataFrame(data)
#     sentence_features[s] = tokens
#
# print(feature_dataFrames)
with open('features/token_intervals.txt', 'w',encoding='utf-8') as f:
    for interval in index_interval_of_tokens:
        f.write(str(interval))
        f.write("@@@")

with open('features/dependency-paths.txt', 'w',encoding='utf-8') as f:
    for path in short_dependency_paths:
        f.write(str(path))
        f.write("@@@")
with open('features/word-distances.txt', 'w',encoding='utf-8') as f:
    for dist in word_distances:
        f.write(str(dist))
        f.write("@@@")
with open('features/opinion-sentences.txt', 'w',encoding='utf-8') as f:
    for opinion in opinion_sentence:
        f.write(str(opinion_sentence))
        f.write("@@@")
with open('features/aspect-Bs.txt', 'w',encoding='utf-8') as f:
    for beginning in beginning_of_aspects:
        f.write(str(beginning))
        f.write("@@@")

with open('features/aspect-Is.txt', 'w',encoding='utf-8') as f:
    for inside in inside_of_aspects:
        f.write(str(inside))
        f.write("@@@")






