from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Highest_Zone_Temperature_Sensor import Highest_Zone_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Warmest_Zone_Temperature_Sensor import Warmest_Zone_Temperature_Sensor


class HVAC_Warmest_Zone_Temperature_Sensor(Highest_Zone_Temperature_Sensor,Warmest_Zone_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').HVAC_Warmest_Zone_Temperature_Sensor
	
	
