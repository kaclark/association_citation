#usage: python fr2en.py mot1 mot2 mot3 ...
from PyMultiDictionary import MultiDictionary
import sys

#input_words = sys.argv[1].split(",")

input_words = sys.argv[1:]
dictionary=MultiDictionary()
dictionary.set_words_lang('fr') 

for iword in input_words:
    trans = dictionary.translate('fr', iword)
    trans_map = {x[0]:x[1] for x in trans}
    print(iword, "->", trans_map["en"])
    with open("fr2en.csv", "a") as track_trans:
        track_trans.write(iword + "," + trans_map["en"] + "\n")
