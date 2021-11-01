from sklearn.model_selection import train_test_split



POS_tags = []
short_dependency_paths = []
word_distances = []
opinion_sentence = []
beginning_of_aspects = []
inside_of_aspects = []

def extract_features_from_file(file,destination,split_token = '@@@'):
    path = "../features/" + file
    with open(path, encoding='utf-8') as in_file:
        strings = in_file.read().split(split_token)
        for i in range(len(strings) - 1):
            destination.append(eval(strings[i]))


########################
#extracting the features

extract_features_from_file('POS-tags.txt',POS_tags)
extract_features_from_file('dependency-paths.txt',short_dependency_paths)
extract_features_from_file('word-distances.txt',word_distances)
extract_features_from_file('opinion-sentences.txt',opinion_sentence)
extract_features_from_file('aspect-Bs.txt',beginning_of_aspects)
extract_features_from_file('aspect-Is.txt',inside_of_aspects)


######################################
# defining function to extract  and prepare the feature vectors
def featurise(sentence_idx,token_idx):
    """
        extracts a feature vector(dictionary) for a token
        :param sentence_idx int the index of the sentence
        :param token_idx int the index of the token in that sentence
        :return features a dictionary that represents the feature vector of this token
    """
    token = POS_tags[sentence_idx][token_idx][0]
    pos = POS_tags[sentence_idx][token_idx][1]
    dln = False
    if token_idx in short_dependency_paths[sentence_idx]:
        dln = True
    wrdDist = False
    if token_idx in word_distances[sentence_idx]:
        wrdDist = True
    sSn = opinion_sentence[sentence_idx][token_idx]
    return {'token':token,'pos':pos,'dln':dln,'wrdDist':wrdDist,'sSn':sSn}
def featurise_sentence(sentence_idx):
    """
            creates the feature vector for each token in a sentence
            :param sentence_idx int the index of the sentence
            :return features a list containing the feature vector of each token of that sentence
            :return labels the label of each token
    """
    features = [featurise(sentence_idx,token_idx) for token_idx in range(len(POS_tags[sentence_idx]))]
    labels = ['' for i in range(len(POS_tags[sentence_idx]))]
    for i in beginning_of_aspects[sentence_idx]:
        labels[i] = 'B'
    for i in inside_of_aspects[sentence_idx]:
        labels[i] = 'I'
    for i in range(len(labels)):
        if labels[i]== '':
            labels[i] = 'O'
    return features,labels

def featurise_dataset():
    """
        creates the feature vector for all tokens in all sentences
        :return all_sequences  the features all sequences
        :return all_labels the label of each token
    """
    all_sequences = []
    all_labels = []
    for sentence_idx in range(len(POS_tags)):
        features,labels = featurise_sentence(sentence_idx)
        all_sequences.append(features)
        all_labels.append(labels)
    return all_sequences,all_labels


all_sequences,all_labels = featurise_dataset()

############################
#from this part on, I used the code from Antonio Feregrino from dev.to to create the model because it was extensively suitable to my needs.

# creating train sets and test(verification) sets
train_docs, test_docs, train_labels, test_labels = train_test_split(all_sequences, all_labels)
print("training data length: ",len(train_docs))
print("test data length: ",len(test_docs))



import pycrfsuite

trainer = pycrfsuite.Trainer(verbose=False)

trainer.set_params({
    'c1': 1.0,   # coefficient for L1 penalty
    'c2': 1e-3,  # coefficient for L2 penalty
    'max_iterations': 200,

    'feature.possible_transitions': True
})


# We are feeding our training set to the algorithm here.
for xseq, yseq in zip(train_docs, train_labels):
    trainer.append(xseq, yseq)

trainer.train('../model/Aspect-detection.crfsuite')

#################
#evaluation

crf_tagger = pycrfsuite.Tagger()
crf_tagger.open('model/Aspect-detection.crfsuite')

from sklearn.metrics import classification_report

all_true, all_pred = [], []

for i in range(len(test_docs)):
    all_true.extend(test_labels[i])
    all_pred.extend(crf_tagger.tag(test_docs[i]))
result = classification_report(all_true, all_pred)
with open('Results/result.txt','w') as file:
    file.write(result)








