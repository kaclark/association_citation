#import tools
import sys
sys.path.append("../../transcriptions/")
from tools import *

#perform basic read operation
from os.path import exists

'''
===================================
    Structure of the Monadology
===================================
The contents of almost all of the ninety sections of the Monadology can be categorised as follows:

Definition – gives the essence or nature of a thing
Axiom – a general principle or truth, typically taken to be self-evident and so not requiring further proof
Corollary – a truth that follows from what has already been proved or supposed
Argument – a set of statements or other evidence put forward as grounds to accept a particular conclusion
Postulate – a statement assumed to be true, that is, asserted without any supporting evidence (sometimes the evidence for a postulate will be provided after the postulate)
Scholium – explanatory note

##For the purposes of writing this as code
Definition -- gives the content of a file
Axiom -- assertion (?)
Corollary -- inference (?)
Argument -- graph with edges as propositional relations
Postulate -- treated as True, but with a pointer to evidence
Scholium -- comment
'''

def define_monad():
    assert exists("data/monad.txt")
    with open("data/monad.txt", "r") as f:
        monad_definition = read_first_line(f)
    return {"monad": monad_definition}

what_exists = {} 
what_exists.update(define_monad())
assert "simple_substance" in what_exists.values()
arg0 = nx.Graph() 
arg0.add_edge("monad", "simple_substance", byDefinition="is")
arg0.add_edge("monad", "hasExtension", byArgument="isFalse")
arg0.add_edge("monad", "hasShape", byArgument="isFalse")
arg0.add_edge("monad", "Divisible", byArgument="isFalse")
save_graph(arg0, "data/arg0.png", edgelabels=True)
