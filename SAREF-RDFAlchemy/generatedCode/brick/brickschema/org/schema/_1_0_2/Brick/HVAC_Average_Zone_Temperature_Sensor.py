from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Average_Zone_Temperature_Sensor import Average_Zone_Temperature_Sensor


class HVAC_Average_Zone_Temperature_Sensor(Average_Zone_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').HVAC_Average_Zone_Temperature_Sensor
	
	
