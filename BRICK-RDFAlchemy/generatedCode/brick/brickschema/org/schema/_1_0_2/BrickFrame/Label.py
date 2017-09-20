from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.BrickFrame.Taggable import Taggable


class Label(Taggable):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/BrickFrame#').Label
	
	
    hasTokenSomeToken = rdfList(Namespace('https://brickschema.org/schema/1.0.2/BrickFrame#').hasTokenSomeToken)
    listOfhasTokenSomeToken = []

    def addhasTokenSome (self, parameter):
        self.listOfhasTokenSomeToken.append(parameter)
        self.hasTokenSomeToken = self.listOfhasTokenSomeToken
			
