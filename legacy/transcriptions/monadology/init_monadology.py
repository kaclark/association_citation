#import tools
import sys
sys.path.append("../../transcriptions/")
from tools import *

#perform basic read operation
from os.path import exists
from sympy import *
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
'''

def graph_repr():
    arg = nx.Graph() 
    arg.add_edge("monad", "simpleSubstance", byDefinition="is")
    #Now there exists simple substance
    arg.add_edge("monad", "hasExtension", byArgument="isFalse")
    arg.add_edge("monad", "hasShape", byArgument="isFalse")
    arg.add_edge("monad", "Divisible", byArgument="isFalse")
    #Yet this simple substance has neither extension, nor shape, nor is it divisible
    arg.add_edge("monad", "~endsNaturally", byCorollary="simpleSubstance")
    arg.add_edge("monad", "~beginsNaturally", byCorollary="simpleSubstance")
    #simple substance neither begins nor ends
    arg.add_edge("monad", "isCausallyIndependent", byArgument="isTrue")
    arg.add_edge("monad", "hasQualities", byArgument="isTrue")
    arg.add_edge("monad", "hasDifferentQualities", byArgument="isTrue")
    arg.add_edge("beings", "identityOfIndiscernibles", byAxiom="~exactlyAlike")
    arg.add_edge("identityOfIndiscernibles", "monads", byCorollary="~exactlyAlike")
    arg.add_edge("monad", "subjectToChange", byPostulate="isTrue")
    arg.add_edge("subjectToChange", "change", byPostulate="where")
    arg.add_edge("change", "continual", byPostulate="isTrue")
    arg.add_edge("change", "isCausuallyIndependent", byCorollary="isForAll")
    arg.add_edge("change", "InternalPrinciple", byCorollary="isOf")
    arg.add_edge("monads", "CompleteSpecChanges", byPostulate="contain")
    arg.add_edge("monads", "PrincipleofChange", byPostulate="contain")
    arg.add_edge("CompleteSpecChanges", "pluralityWithinUnity", byArgument="includes")
    arg.add_edge("perception", "pluralityWithinUnity", byDefinition="representationOf")
    arg.add_edge("pluralityWithinUnity", "monad", byCollarary="basicStateOf")
    arg.add_edge("appetite", "InternalPrinciple", byDefinition="actionOf")
    arg.add_edge("simpleSubstance", "perception", byArgument="onlySourceOf")
    #simple substance though has qualities of difference
    save_graph(arg, "data/arg.png", edgelabels=True)

def logic_repr():
    monad, simpleSubstance = symbols('monad,simpleSubstance')
    def1 = Equivalent(monad, simpleSubstance)
    print(def1)

logic_repr()
