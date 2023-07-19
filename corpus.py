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

    def get_description(self):
        return self.description

    def get_bib(self):
        return self.bib

    def get_invocations(self):
        return self.invocations

