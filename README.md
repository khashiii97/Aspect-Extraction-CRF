# Aspect-Extraction-CRF
##  NLP Extracting opinion targets from the SentiPers dataset using Conditional Random Fields
This repository hosts an implementation of the paper "Extracting Opinion Targets in a Single- and Cross-Domain Setting
with Conditional Random Fields" as stated in the [original paper](https://aclanthology.org/D10-1101.pdf). It is used to develop a model for extracting aspects in a given review sentence, trained on
the [SentiPers](https://github.com/phosseini/SentiPers) dataset.

SentiPers consists of numerous reviews, each having their opinions and targets labeled, thus being very beneficial for Sentiment Analysis.

Adhering to the paper, all the mentioned features for each word have been extracted, namely Token, POS, Short Dependency Path, Word Distance, and Opinion Sentence.

For POS tagging, I have to thank @minasmz for her [LSTM-based POS tagger](https://github.com/minasmz/Persian-POSTagger-with-LSTM). 
Note that the sentipers dataset consists of many slang words and informal written words, thus a colossal amount of preprocessing was required to clean the data.
also, after the POS tagging, many cases had to be manually modified. The final POS tags and dependencies lie in their respective repositories, and
all sort of help in improving them for future use is highly appreciated.

The results of the experiment are in the results directory. If you want to run the code, please first run Feature-creation.py and then training.py.

