import pandas as pd
from src import sentipers
import os
import re
import xml.etree.ElementTree as ET
from POS.POSTagger import POSTagger
pos_tagger = POSTagger("../model/perpos.model")
from src import Utils

'''
this code will take the following steps:
1. extracting each review sentence from the main folder
2. extracting the aspect and opinion for each review
3. cleaning the sentences for more convenient pos tagging
4. saving it all in a file.
5. the obtained data will be used in feature-creation.py for creating features
'''


'''
the following datagram will be the final output of this code.
it will contain the tokenized sentence, including a list of lists containg the indexes of the aspects (each aspect
can consist of multiple parts)
'''
pd_sentences = pd.DataFrame(columns= ['tokens','aspect','opinion'])
# temp_pd = pd.DataFrame(data=[[[1,2],[3,4]]],columns= ['tokens','aspect'])
# pd_sentences = pd_sentences.append(temp_pd,ignore_index= True)
main_path = "../data/main/"
data_for_next_part = []
changed = []
for path in os.listdir(main_path):
    print(len(data_for_next_part))
    full_path = os.path.join(main_path, path)
    if os.path.isfile(full_path) and full_path.endswith(".xml"):
        print(full_path)
        with open(full_path,encoding="utf8") as file:
            sentences = {}  # (sentence_id, sentence text)
            root_aspects = {} # (element_id, aspect)
            sentence_aspects ={}#((sentence_id,[(aspect_id,[start_index,end_index])]
            sentence_opinions = {}
            tag_to_aspect ={} # {(target(i).tag,element_id)
            values = {}
            root = ET.parse(full_path).getroot()
                #getting all sentences and putting them in the sentence dictionary
            for sentence in root.iter('Sentence'):
                sentences[sentence.attrib['ID']] = sentence.text
                values[sentence.attrib['ID']] = sentence.attrib['Value']

            for tag in root.iter('Tag'):
                if tag.attrib['Type'] == 'Target(M)': #aspects
                    root_aspects[tag.attrib['ID']] = tag.attrib['Root']
                if tag.attrib['Type'] == 'Target(I)': #aspects
                    tag_to_aspect[tag.attrib['ID']] = tag.attrib['Relation']
                    coordinate = re.split('[ \[,\]]+',tag.attrib['Coordinate'])
                    if coordinate[1] not in sentence_aspects.keys():
                        sentence_aspects[coordinate[1]] = [] # coordinate[1] is the sentence id
                    sentence_aspects[coordinate[1]].append([tag.attrib['ID'],[int(coordinate[2]),int(coordinate[3])]])
                if tag.attrib['Type'] == 'Opinion':  # opinions:
                    coordinate = re.split('[ \[,\]]+', tag.attrib['Coordinate'])
                    if coordinate[1] not in sentence_opinions.keys():
                        sentence_opinions[coordinate[1]] = [] # coordinate[1] is the sentence id
                    index_of_aspect = 0 #index of aspect associated with this opinion
                    target_id = tag.attrib['Relation']
                    if coordinate[1] in sentence_aspects.keys():
                        aspects = sentence_aspects[coordinate[1]]
                        for index in range(len(aspects)):
                            if aspects[index][0] == target_id:
                                index_of_aspect = index
                                break
                        sentence_opinions[coordinate[1]].append(
                            [index_of_aspect, int(coordinate[2]), int(coordinate[3])])
                    else:
                        for keyword in root.iter('Keyword'):
                            if keyword.attrib['Coordinate'].startswith("[" +  coordinate[1]):
                                keyword_coordinate = re.split('[ \[,\]]+', keyword.attrib['Coordinate'])
                                sentence_aspects[coordinate[1]] = [[tag.attrib['ID'], [int(keyword_coordinate[2]), int(keyword_coordinate[3])]]]
                            break
                        sentence_opinions[coordinate[1]].append(
                            [0, int(coordinate[2]), int(coordinate[3])])
            for k in sentences.keys():
                aspect = []
                opinion = []
                if k in sentence_aspects.keys():
                    aspect = sentence_aspects[k]
                if k in sentence_opinions.keys():
                    opinion = sentence_opinions[k]
                data = Utils.sentence_cleaner(sentence= sentences[k],opinions=opinion,aspects=aspect)
                data_for_next_part.append(data)


for sentence in data_for_next_part:
    sentence[0] = sentence[0].replace('إ','ا')
for s in data_for_next_part:
    if '،' in s[0] and ',' in s[0]:
        s[0] = s[0].replace(',','،')
del data_for_next_part[217]
del data_for_next_part[5371]
del data_for_next_part[5889]
del data_for_next_part[6392]
with open('sentences.txt', 'w',encoding='utf-8') as f:
    for sentence in data_for_next_part:
        f.write(str(sentence))
        f.write("@@@")
print(changed)
