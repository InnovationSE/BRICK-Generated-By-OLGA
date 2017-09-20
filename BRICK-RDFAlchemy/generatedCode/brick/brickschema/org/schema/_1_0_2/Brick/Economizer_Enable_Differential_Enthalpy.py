from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Enable import Enable
from brick.brickschema.org.schema._1_0_2.Brick.Economizer import Economizer


class Economizer_Enable_Differential_Enthalpy(Enable,Economizer):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Economizer_Enable_Differential_Enthalpy
	
	
