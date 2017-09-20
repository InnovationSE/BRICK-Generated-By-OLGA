from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Booster_Fan_Air_Flow_Sensor import Booster_Fan_Air_Flow_Sensor


class VAV_Booster_Fan_Air_Flow_Sensor(Booster_Fan_Air_Flow_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Booster_Fan_Air_Flow_Sensor
	
	
