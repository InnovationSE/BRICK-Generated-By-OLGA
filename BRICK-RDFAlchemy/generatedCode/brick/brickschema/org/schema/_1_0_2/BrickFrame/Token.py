from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.BrickFrame.Taggable import Taggable


class Token(Taggable):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/BrickFrame#').Token
	
	
    hasTagSomeToken = rdfList(Namespace('https://brickschema.org/schema/1.0.2/BrickFrame#').hasTagSomeToken)
    listOfhasTagSomeToken = []

    def addhasTagSome (self, parameter):
        self.listOfhasTagSomeToken.append(parameter)
        self.hasTagSomeToken = self.listOfhasTagSomeToken
			
    hasTagSetSomeTagSet = rdfList(Namespace('https://brickschema.org/schema/1.0.2/BrickFrame#').hasTagSetSomeTagSet)
    listOfhasTagSetSomeTagSet = []

    def addhasTagSetSome (self, parameter):
        self.listOfhasTagSetSomeTagSet.append(parameter)
        self.hasTagSetSomeTagSet = self.listOfhasTagSetSomeTagSet
			
