class Concept:

    def __init__(self, name):
        self.name = name
        self.quotes = [] 
        self.bib = {}
        self.description = ""
        self.invocations = set()
    
    #TODO: make source class(maybe store text pointer)
    def add_quote(self, quote, source):
        #parameters
        #quote: string
        #source: string
        self.quotes.append(quote)
        self.bib[quote] = source
    
    def add_to_description(self, blurb):
        #add comments and summaries
        #unordered string concat
        self.description += blurb + "\n"
 
    def invoke(self, inscription_id):
        #record usage via inscription_id
        #inscription_id: string
        self.invocations.add(inscription_id)
        #later use this in html generation to yeild a:hover div of condensed summary
        return self.name

    def get_description(self):
        return self.description

    def get_bib(self):
        return self.bib

    def get_invocations(self):
        return self.invocations

    def full_summary(self):
        return self.name + "\n\n" + \
                self.description + "\n" + \
                "\n\n".join([k + " (" + v + ")" for k,v in self.get_bib().items()])

class Author:

    def __init__(self, name):
        self.name = name
        self.works = {}
        self.description = ""
        self.invocations = set()

    def get_name(self):
        return self.name

    def add_work(self, work_title, work_text):
        #work_title: string
        #work_text: file link, string
        self.works[work_title] = work_text

    def get_works(self):
        return self.works

    def add_to_description(self, blurb):
        self.description += blurb + "\n"

    def invoke(self, inscription_id):
        #record usage via inscription_id
        #inscription_id: string
        self.invocations.add(inscription_id)
        #later use this in html generation to yeild a:hover div of condensed summary
        return self.name

    def get_invocations(self):
        return self.invocations

    def full_summary(self):
        return self.name + "\n\n" + \
                self.description + "\n" + \
                "\n\n".join([k for k,v in self.get_works().items()])

class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.description = ""
        #quotes will get generated ids
        self.id_seed = 1
        self.quotes = {}

    def get_name(self):
        return self.name

    def add_to_description(self, blurb):
        self.description += blurb + "\n"

    def add_quote(self, quote, pg, note=""):
        inc = self.id_seed
        self.quotes[self.id_seed] = {"quote": quote, "pg": pg , "note": note}
        self.id_seed += 1

    def get_quotes(self):
        return self.quotes
    
    def parse_quote(self, quote):
        if quote["note"] != "":
            return quote["quote"] + " " + str(quote["pg"]) + "\n" + str(quote["note"])
        else:
            return quote["quote"] + " " + str(quote["pg"]) 

    def full_summary(self):
        return self.name + ", " + self.author.get_name() + "\n\n" + \
                self.description + "\n" + \
                        "\n\n".join([self.parse_quote(q) for q in self.get_quotes().values()])


def test_book():
    Gadamer = Author("Hans-Georg Gadamer")
    Gadamer.add_work("Truth and Method", "https://web.mit.edu/kaclark/www/gadamer_truth_and_method.pdf")
    Gadamer.add_to_description("Works out a theory of aesthetics from Hegel and carries the project Heidegger started into Hermenutics")
    #print(Gadamer.full_summary())
    Truth_and_Method = Book('Truth and Method', Gadamer)
    Truth_and_Method.add_to_description("1960: Gadamers Major work which deploys the concept of hermenutics from Being and Time")
    with open("./notes/gadamer_truth_and_method.note", "r") as note_in:
        for line in [l.split("\n")[0] for l in note_in.readlines()]:
            pg_num = line.split(",")[-1]
            quote = "".join(line.split(",")[:-1])
            Truth_and_Method.add_quote(quote, pg_num)
    print(Truth_and_Method.full_summary())

test_book()

def test_concept():
    Intuition = Concept("Intuition")
    Intuition.add_quote("It follows from this that an absolute could only be given in an intuition whilst everything else falls within the province of analysis. By intuition is meant the kind of intellectual sympathy by which one places oneself within an object in order to coincide with what is unique in it and consequently inexpressible.", "[Bergson] Introduction to Metaphysics pg 2")
    Intuition.add_to_description("Emil Cioran wrote his thesis on this concept in Herni Bergson")
    Intuition.add_to_description("Gilles Deleuze works closely with Herni Bergson drawing much of his metaphysics from him and interfaces it with post-einstein geometry and chaos theory. Some have argued that Deleuze draws his intutionism from Shestov and Bergson")


    #TODO: Haecceity from scotus, Prehension from Whitehead via Didier
    #Intuition.add_to_description("Intuition can be thought of as" + Prehension.invoke() + "via" + Haecceity.invoke())
    
    #TODO: workout textfile format convention to load from csv type data structure to reduce code bloat
    Intuition.add_quote("In its eternally unsatisfied desire to embrace the object around which it is compelled to turn, analysis multiplies without end the number of its points of view in order to complete its always incomplete representation, and ceaselessly varies its symbols that it may perfect the always imperfect translation. It goes on, therefore, to infinity. But intuition, if intuition is possible, is a simple act.", "[Bergson] Introduction to Metaphysics pg 3")

    Intuition.add_quote("If there exists any means of possessing a reality absolutely instead of knowing it relatively, of placing oneself within it instead of looking at it from outside points of view, of having the intuition instead of making the analysis: in short, of seizing it without any expression, translation, or symbolic representation - metaphysics is that means. Metaphysics, then, is the science which claims to dispense with symbols.", "[Bergson] Introduction to Metaphysics pg 3")

    Intuition.add_quote("There is one reality, at least, which we all seize from within, by intuition and not by simple analysis. It is our own personality in its flowing through time - our self which endures. We may sympathize intellectually with nothing else, but we certainly sympathize with our own selves.", "[Bergson] Introduction to Metaphysics pg 3")

    Intuition.add_quote("Either metaphysics is only this play of ideas, or else, if it is a serious occupation of the mind, if it is a science and not simply an exercise, it must transcend concepts in order to reach intuition.", "[Bergson] Introduction to Metaphysics pg 5")

    Intuition.add_quote("Certainly, concepts are necessary to it, for all the other sciences work as a rule with concepts, and metaphysics cannot dispense with the other sciences. But it is only truly itself when it goes beyond the concept, or at least when it frees itself from rigid and ready-made concepts in order to create a kind very different from those which we habitually use; I mean supple, mobile, and almost fluid representations, always ready to mould themselves on the fleeting forms of intuition.", "[Bergson] Introduction to Metaphysics pg 5")

    Intuition.add_quote("our duration can be presented to us directly in an intuition, that it can be suggested to us indirectly by images, but that it can never - if we confine the word concept to its proper meaning - be enclosed in a conceptual representation.", "[Bergson] Introduction to Metaphysics pg 6")

    Intuition.add_quote("Every feeling, however simple it may be, contains virtually within it the whole past and present of the being experiencing it, and, consequently, can only be separated and constituted into a 'state' by an effort of abstraction or of analysis.", "[Bergson] Introduction to Metaphysics pg 6") 

    Intuition.add_quote("philosophy is the search for a unique intuition from which we can descend with equal ease to different concepts", "[Bergson] Introduction to Metaphysics pg 9")

    Intuition.add_quote("What is really important for philosophy is to know exactly what unity, what multiplicity, and what reality superior both to abstract unity and multiplicity the multiple unity of the self actually is. Now philosophy will know this only when it recovers possession of the simple intuition of the self by the self.", "[Bergson] Introduction to Metaphysics pg 9")

    print(Intuition.full_summary())
