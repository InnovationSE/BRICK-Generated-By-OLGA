from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Leaving_Water_Temperature_Sensor import Leaving_Water_Temperature_Sensor


class Preheat_Coil_Leaving_Water_Temperature_Sensor(Leaving_Water_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Preheat_Coil_Leaving_Water_Temperature_Sensor
	
	
