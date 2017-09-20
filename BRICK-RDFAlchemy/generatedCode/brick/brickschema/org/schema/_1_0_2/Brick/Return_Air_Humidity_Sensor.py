from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Return_Air import Return_Air
from brick.brickschema.org.schema._1_0_2.Brick.Humidity_Sensor import Humidity_Sensor


class Return_Air_Humidity_Sensor(Return_Air,Humidity_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Return_Air_Humidity_Sensor
	
	
