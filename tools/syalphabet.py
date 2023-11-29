import eng_to_ipa as p
import sys

syriac_letters = {
        "0x251":"\u0710", #ɑ: Alep
        "0x62":"\u0712", #b: Bet
        "0x67":"\u0713", #g: Gamal
        "0x64":"\u0715", #d: Dalat
        "0x259":"\u0739", #ə: scwha*(0744) -> e
        "0x6e":"\u0722", #n: Nun
        "0x72":"\u072A", #r: Res
        "0x74":"\u072C", #t: Taw
        "0x26a":"\u0738", #ɪ: e*
        "0x73":"\u0723", #s: Semkat
        "0x6c":"\u0720", #l: Lamad
        "0x69":"\u071D\u073C", #i: Yod-lec*
        "0x6b":"\u071F", #k: Kap
        "0x70":"\u0726", #p: Pe
        "0x25b":"\u0738", #ɛ: ehr* 
        "0x61":"\u0732", #a: * 
        "0x254":"\u0718\u073F", #o: Waw-lec* 
        "0x6f":"\u0718\u073F", #o: Waw-lec* 
        "0x3b8":"\u072C\u073C", #t: Taw-soft
        "0x28a":"\u0718\u073C", #ʊ -> u: Waw-lec-below
        "0x65":"\u0739", #e: *
        "0x2a4":"\u0713", #g~ -> g: Gamal
        "0x14b":"\u0725", #ŋ: Ē
        "0x68":"\u0717", #h: Het
        "0x6d":"\u0721", #m: Mim
        "0xf0":"\u0715\u073C", #ð 
        "0xe6":"\u0732", #æ -> a
        "0x77":"\u0718", #w: Waw
        "0x75":"\u0718\u073C", #u: Waw-lec-below
        "0x76":"\u0712\u073C", #v: Bet-soft
        "0x283":"\u072B", #ʃ sh: Sin
        "0x66":"\u0726\u073C", #f, Pe-soft
        "0x7a":"\u0719", #z: Zayn
        "0x2a7":"\u071F\u071A",  #ʧ ch: k~ -> ch
        "0x6a":"\u071D", #j: Yod
        "0x20":"\u0020", #space
}

skip_codes = set()
#skip stress notation
skip_codes.add("0x2c8")
skip_codes.add("0x2cc")

def phonetic_transliteration(textflow, verbose):
    sink = []
    maxflow = True
    phonetic_form = p.convert(textflow)
    if verbose:
        print(textflow, "->", phonetic_form)

    hexes = [(ch, hex(ord(ch))) for ch in phonetic_form]
    for hexi in hexes:
        ch, hexv = hexi
        if hex(ord(ch)) not in skip_codes:
            try:
                syl = syriac_letters[hexv]
                sink.append(syl)
                if verbose:
                    print("\t",ch,"->", syl)
            except KeyError:
                maxflow = False
                sink.append("¿")
                if verbose:
                    print(ch, "<-?->", "∆"+str(hex(ord(ch))))
    if verbose:
        sink.reverse()
        if maxflow:
            print("".join(sink), "<-", textflow)
        else:
            print("".join(sink), "<-?->", textflow)
    else:
        return "".join(sink)

def print_syriac_alphabet():
    for rph, sl in syriac_letters.items():
        ph = chr(int(rph, 16))
        print(ph, sl)
        
trans_text = sys.argv[1]
if trans_text == "@":
    print_syriac_alphabet()
else:
    if " " in trans_text:
        print(phonetic_transliteration(trans_text, verbose=False))
    else:
        phonetic_transliteration(trans_text, verbose=True)
