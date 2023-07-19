class Concept:

    def __init__(self, name):
        self.name = name
        self.quotes = [] 
        self.bib = {}
        self.description = ""
        self.invocations = set()

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
                "\n".join([k + ", " + v for k,v in self.get_bib().items()])


Intuition = Concept("Intuition")
Intuition.add_quote("It follows from this that an absolute could only be given in an intuition whilst everything else falls within the province of analysis. By intuition is meant the kind of intellectual sympathy by which one places oneself within an object in order to coincide with what is unique in it and consequently inexpressible.", "[Bergson] Introduction to Metaphysics pg 2")
Intuition.add_to_description("Emil Cioran wrote his thesis on this concept in Herni Bergson")
print(Intuition.full_summary())

#TODO: Haecceity from scotus, Prehension from Whitehead via Didier
#Intuition.add_to_description("Intuition can be thought of as" + Prehension.invoke() + "via" + Haecceity.invoke())
