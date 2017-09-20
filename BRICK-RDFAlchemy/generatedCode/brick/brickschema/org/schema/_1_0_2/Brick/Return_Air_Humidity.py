from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Return_Air import Return_Air
from brick.brickschema.org.schema._1_0_2.Brick.Air_Humidity import Air_Humidity


class Return_Air_Humidity(Return_Air,Air_Humidity):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Return_Air_Humidity
	
	
