from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Return_Air_CO2 import Return_Air_CO2


class Max_Return_Air_CO2(Return_Air_CO2):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Max_Return_Air_CO2
	
	
