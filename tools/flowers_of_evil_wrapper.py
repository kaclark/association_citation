import random
poem_metadata = [('', (0,0)), #1-indexing to match book
         ('The Blessing',(7,237)),
         ('The Albatross',(10,240)),
         ('Elevation',(11,240)),
         ('Correspondences',(12,241)),
         ('I love the thought...',(13,242)),
         ('Beacons',(14,243)),
         ('The Sick Muse',(16,245)),
         ('The Venal Muse',(17,246)),
         ('The Wicked Monk',(18,246)),
         ('The Ruined Garden',(18,247)),
         ('Ill Luck',(19,248)),
         ('A Former Life',(20,248)),
         ('Gypsies on the Road',(21,249)),
         ('Man and the Sea',(21,250)),
         ('Don Juan in Hell',(22,250)),
         ('The Punishment of Pride',(23,251)),
         ('Beauty',(24,252)),
         ('The Ideal',(25,253)),
         ('Giantess',(26,253)),
         ('Jewels',(26,254)),
         ('The Mask',(28,255)),
         ('Hymn to Beauty',(30,257)),
         ('Exotic Perfume',(31,258)),
         ('Her Hair',(32,259)),
         ('You whom I worship',(33,260)),
         ('Youd take to bed the whole world...',(34,260)),
         ('Sed non Satiata',(35,261)),
         ('Robed in a siklen robe...',(35,262)),
         ('The Dancing Serpent',(36,262)),
         ('A Carrion',(38,264)),
         ('De Profundis Clamavi',(40,266)),
         ('The Vampire',(40,266)),
         ('Lethe',(42,267)),
         ('A hideous Jewess lay with me...',(43,268)),
         ('The Remorse of the Dead',(43,269)),
         ('The Cat(Come, beautiful creature...)',(44,270)),
         ('Duellum',(45,270)),
         ('The Balcony',(46,271)),
         ('The Possessed',(47,272)),
         ('A Phantom',(48,273)),
         ('If by some freak of fortune',(50,275)),
         ('Semper Eadem',(51,276)),
         ('All in One',(52,277)),
         ('What shall you say tonight',(53,278)),
         ('The Living Torch',(54,278)),
         ('To One Who Is Too Gay',(54,278)),
         ('Reversibility',(56,280)),
         ('The Confession',(57,281)),
         ('The Spiritual Dawn',(59,283)),
         ('Evening Harmony',(60,284)),
         ('The Flask',(61,284)),
         ('The Poison',(62,286)),
         ('Misty Sky',(63,287)),
         ('The Cat(A fine strong gentle cat...)',(64,287)),
         ('The Splendid Ship',(66,289)),
         ('Invitation to the Voyage',(67,291)),
         ('The Irreparable',(69,292)),
         ('Conversation',(71,294)),
         ('Song of Autumn',(72,295)),
         ('To a Madonna',(73,296)),
         ('Afternoon Song',(75,298)),
         ('Sisina',(77,299)),
         ('Praises of My Frances',(77,300)),
         ('To a Creole Lady',(79,301)),
         ('Moesta et Errabunda',(80,302)),
         ('The Ghost',(81,303)),
         ('Sonnet of Autumn',(82,304)),
         ('The Sadness of the Moon',(82,304)),
         ('Cats',(83,305)),
         ('The Owls',(84,306)),
         ('The Pipe',(85,306)),
         ('Music',(85,307)),
         ('Burial',(86,308)),
         ('Fantastic Engraving',(87,308)),
         ('The Gladly Dead',(88,309)),
         ('The Cask of Hate',(88,310)),
         ('The Cracked Bell',(89,310)),
         ('Spleen: Old Pluvius, month of rains...',(90,311)),
         ('Spleen: I have more memories...',(91,312)),
         ('Spleen: When the low heavy sky...',(92,313)),
         ('Obsession',(93,314)),
         ('The Thirst for Extinction',(94,315)),
         ('Alchemy of Grief',(95,316)),
         ('Sympathetic Horror',(96,316)),
         ('Heautontimoroumenos',(97,317)),
         ('The Irremediable',(98,318)),
         ('The Clock',(100,320)),
         ('A Landscape',(105,325)),
         ('The Sun',(106,326)),
         ('The Red-Haired Beggar Girl',(107,326)),
         ('The Swan',(109,329)),
         ('The Seven Old Men',(111,331)),
         ('The Little Old Women',(113,333)),
         ('The Blind',(117,336)),
         ('To a Passer-by',(118,337)),
         ('Skeletons Digging',(118,338)),
         ('Comes the Charming Evening',(120,339)),
         ('The Gaming Table',(121,340)),
         ('The Dance of Death',(123,341)),
         ('The Love of Lies',(125,344)),
         ('I have not forgotten',(126,345)),
         ('The Servant',(127,345)),
         ('Mists and Rains',(128,346)),
         ('Parisian Dream',(129,347)),
         ('Morning Twilight',(131,349)),
         ('The Soul of Wine',(135,353)),
         ('The Ragpickers Wine',(136,354)),
         ('The Murderers Wine',(137,355)),
         ('The Solitarys Wine',(140,357)),
         ('Lovers Wine',(140,358)),
         ('Destruction',(145,361)),
         ('The Martyr',(146,361)),
         ('Lesbos',(148,364)),
         ('Lesbians:Delphine and Hippolyta',(151,366)),
         ('Lesbians (like pensive cattle...)',(155,370)),
         ('The Two Good Sisters',(157,371)),
         ('The Fountain of Blood',(157,372)),
         ('An Allegory',(158,373)),
         ('My Beatrice',(159,373)),
         ('The Metamorphoses of a Vampire',(160,375)),
         ('Voyage to Cythera',(161,376)),
         ('Love and  the Skull',(164,378)),
         ('The Denial of Saint Peter',(167,383)),
         ('Abel and Cain',(168,384)),
         ('Litany to Satan',(170,386)),
         ('The Death of Lovers',(175,391)),
         ('The Death of the Poor',(175,391)),
         ('The Death of Artists',(176,392)),
         ('The End of the Day',(177,393)),
         ('Dream of a Curious Person',(178,393)),
         ('The Voyage',(179,394))
]

def print_poem(title, content):
    print(title.upper(), "\n")
    comma_conv = content.replace("*",",")
    newlines = comma_conv.replace("\\n", "\n")
    print(newlines)
    print("\n")

def load_poem_csv():
    with open("english_flowers_of_evil.csv", "r") as flowers_in:
        lines = [l.split('\n')[0] for l in flowers_in.readlines()]
        poems = {}
        for line in lines:
            title, content = line.split(",")
            poems[title] = content
    return poems

metadata = random.choice(poem_metadata)
poem_title, poem_lookup = metadata
recorded_poems = load_poem_csv()
if poem_title in recorded_poems:
    print_poem(poem_title, recorded_poems[poem_title])
else:
    poem_title, poem_lookup = metadata
    en_page, fr_page = poem_lookup
    print(poem_title, "see pg." ,en_page)

#print(print_poem("Man and the Sea", load_poem_csv()["Man and the Sea"]))

