import sys
from wiktionaryparser import WiktionaryParser
parser = WiktionaryParser()

parser.set_default_language('french')
parser.include_relation('alternative forms')
parser.include_relation("synonyms")
parser.include_relation("antonyms")
parser.include_relation("hypernyms")
parser.include_relation("hyponyms")
parser.include_relation("meronyms")
parser.include_relation("holonyms")
parser.include_relation("troponyms")
parser.include_relation("related terms")
parser.include_relation("coordinate terms")

s_word = sys.argv[1]
word_info = parser.fetch(s_word, 'french')
print(s_word, "\n")
#The word info is given as a map
for k,v in word_info[0].items():
    #definitions is the only data structure returned
    if k == 'definitions':
        #for each element in the list of defitions
        for vx in v:
            #there is a dictionary
            for ky, vy in vx.items():
                #a few entires are single words
                if not isinstance(vy, list):
                    print(ky, ":", vy, "\n")
                #each of these dictionaries holds a list
                #if this list is empty we skip
                if vy != [] and isinstance(vy, list):
                    print(ky + "\n")
                    for vw in vy:
                        print("\t" + vw)
                    print("\n")
    elif k == "etymology":
        v2 = v.replace(";", "\n\n")
        v3 = v2.replace(".", "\n\n")
        v4 = v3.replace(":", "\n\n")
        v5 = v4.replace("),", "),\n\n")
        print(k.upper(), "\n\n", v5)
    elif k == "pronunciations":
        print(k.upper(), "\n")
        for kq,vq in v.items():
            if vq != []:
                for vqq in vq:
                    print(vqq)
