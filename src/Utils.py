from hazm import *
import re
def ide_al(tokens): #the word ایده آل raised some problems so I had to fix that manually
    while "آل" in tokens:
        tokens[tokens.index("آل") - 1] = "ایده آل"
        del tokens[tokens.index("آل")]
    return tokens
def jam_bandi(tokens): #the word جمع بندی raised some problems so I had to fix that manually
    while "جمع" in tokens:
        if tokens.index("جمع") + 1 < len(tokens):
            if 'بندی' in tokens[tokens.index("جمع") + 1]:
                tokens[tokens.index("جمع") + 1] = tokens[tokens.index("جمع") + 1].replace('بندی', '')
                if tokens[tokens.index("جمع") + 1] =='':
                    del tokens[tokens.index("جمع") + 1]
                tokens[tokens.index("جمع") ] = "جمع بندی"
    return tokens
def foghol_adeh(tokens): #the word فوق العاده raised some problems so I had to fix that manually
    while "فوق" in tokens:
        if tokens.index("فوق") + 1 < len(tokens):
            if 'العاده' in tokens[tokens.index("فوق") + 1]:
                tokens[tokens.index("فوق") + 1] = tokens[tokens.index("فوق") + 1].replace('العاده', '')
                if tokens[tokens.index("فوق") + 1] =='':
                    del tokens[tokens.index("فوق") + 1]
                tokens[tokens.index("فوق") ] = 'فوق العاده'
    return tokens

def delete_u200c(tokens):# nim space would be written as u200c\
    for t,token in enumerate(tokens):
        if '\u200c' in token:
            tokens[t] = token.replace('\u200c','')
            if tokens[t] == '':
                del tokens[t]
    return tokens
def tokenize(sentence,opinions,aspects):
    """
        tokenizes the given sentence
        :param sentence: sentence to be tokenized
        :param aspects: a list containing tuples in the form of(aspect_id,start,end) which indicate an aspect in the sentence
        :param opinions: a list consisting of tuples like(aspect_index,start,end) which indicate an opinion and its related aspect in the sentence
        when tokenizing, we want the opinion word to be a whole token and not be splited.
        :return tokens
    """
    tokens = word_tokenize(sentence)
    #getting the index of the tokenized words in the main sentence:
    for opinion in opinions:
        interval = opinion[1:3]
        initial = 0
        opinion_start = interval[0]
        opinion_end = interval[1]
        indexes = {}  # (start index of token in the sentence, index of token in tokens)
        print(tokens)
        for i in range(len(tokens)):
            indexes[sentence[initial:].index(tokens[i]) + initial] = i
            initial += len(tokens[i])
        if sentence[opinion_start:opinion_end] != tokens[indexes[opinion_start]]:  # the opinion word has been splited
            opinion = sentence[opinion_start:opinion_end]
            length_of_first_part_of_opinion = len(tokens[indexes[opinion_start]])
            rest_of_the_opinion = opinion.replace(' ', '')[length_of_first_part_of_opinion:]
            tokens[indexes[opinion_start]] = opinion
            i = indexes[opinion_start] + 1
            while i < len(tokens) and rest_of_the_opinion in tokens[i]:
                print(tokens[i])
                tokens[i] = tokens[i].replace(rest_of_the_opinion, '')
                i += 1
            tokens = [token for token in tokens if token != '']
    tokens = ide_al(tokens)
    tokens = jam_bandi(tokens)
    tokens = foghol_adeh(tokens)
    tokens = delete_u200c(tokens)
    return tokens

def sentence_cleaner(sentence,opinions,aspects):
    """
    removes english words from sentence and replaces them with a persian noun
    also removes numbers from sentence and replaces them with a persian word-number
    :param sentence string
    :param aspects: a list containing tuples in the form of(aspect_id,start,end) which indicate an aspect in the sentence
    :param opinions: a list consisting of tuples like(aspect_index,[start,end]) which indicate an opinion and its related aspect in the sentence
    :return cleaned_sentence
    :return aspects the updated aspects(regarding their indexes)
    :return opinions ""
    :return english_words (list of english words)
    :return numbers (list of english numbers)
    """
    extra = sentence
    english_words = re.findall(r'[A-Za-z]+[/. \d@A-za-z]*[/.\d@A-za-z]', sentence)
    english_words += re.findall(r'[\d@]+[a-zA-z][/. \d@A-za-z]*[/\d@A-za-z]', sentence)
    initial = 0
    for word in english_words:
        index = sentence[initial:].find(word)
        index += len(word)
        if len(word) > 4:
            difference = len(word) - 4
            for i, aspect in enumerate(aspects):
                if aspect[1][0] > index:
                    aspects[i][1][0] -= difference
                    aspects[i][1][1] -= difference
            for i, opinion in enumerate(opinions):
                if opinion[1] > index:
                    opinions[i][1] -= difference
                    opinions[i][2] -= difference
        elif len(word) < 4:
            difference = 4 - len(word)
            for i, aspect in enumerate(aspects):
                if aspect[1][0] > index:
                    aspects[i][1][0] += difference
                    aspects[i][1][1] += difference
            for i, opinion in enumerate(opinions):
                if opinion[1] > index:
                    opinions[i][1] += difference
                    opinions[i][2] += difference
        initial = index
    english_words = re.findall(r'[A-Za-z]+[/. \d@A-za-z]*[/.\d@A-za-z]', sentence)
    sentence= re.sub(r'[A-Za-z]+[/. \d@A-za-z]*[/.\d@A-za-z]', 'اصغر', sentence)
    english_words.append(0) #separator
    english_words += re.findall(r'[\d@]+[a-zA-z][/. \d@A-za-z]*[/\d@A-za-z]',sentence)
    sentence = re.sub(r'[\d@]+[a-zA-z][/. \d@A-za-z]*[/\d@A-za-z]','احمد',sentence)
    numbers = re.findall(r'[\d@]+[,]*[.]*[\d@]*', sentence)
    initial = 0
    for number in numbers:
        index = extra[initial:].find(number)
        index += len(number)
        if len(number) > 1:
            difference = len(number) - 1
            for i, aspect in enumerate(aspects):
                if aspect[1][0] > index:
                    aspects[i][1][0] -= difference
                    aspects[i][1][1] -= difference
            for i, opinion in enumerate(opinions):
                if opinion[1] > index:
                    opinions[i][1] -= difference
                    opinions[i][2] -= difference
        elif len(number) < 1:
            difference = 1 - len(number)
            for i, aspect in enumerate(aspects):
                if aspect[1][0] > index:
                    aspects[i][1][0] += difference
                    aspects[i][1][1] += difference
            for i, opinion in enumerate(opinions):
                if opinion[1] > index:
                    opinions[i][1] += difference
                    opinions[i][2] += difference
        initial += index
    sentence = re.sub(r'[\d@]+[,]*[.]*[\d@]*','۳',sentence)
    # sentence = sentence.replace('\n','')
    sentence = sentence.replace('\u200c',' ')
    return [sentence,aspects,opinions,english_words,numbers]
