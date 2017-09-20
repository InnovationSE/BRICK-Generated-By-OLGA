from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.High_Temperature_Hot_Water import High_Temperature_Hot_Water


class High_Temperature_Hot_Water_Return_Temperature(High_Temperature_Hot_Water):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').High_Temperature_Hot_Water_Return_Temperature
	
	
