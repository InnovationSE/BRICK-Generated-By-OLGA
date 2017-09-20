from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Mixed_Air import Mixed_Air
from brick.brickschema.org.schema._1_0_2.Brick.Damper_Position_Sensor import Damper_Position_Sensor


class Mixed_Air_Damper_Position_Sensor(Mixed_Air,Damper_Position_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Mixed_Air_Damper_Position_Sensor
	
	
