from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Lowest_Zone_Temperature_Sensor import Lowest_Zone_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Coldest_Zone_Temperature_Sensor import Coldest_Zone_Temperature_Sensor


class HVAC_Coldest_Zone_Temperature_Sensor(Lowest_Zone_Temperature_Sensor,Coldest_Zone_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').HVAC_Coldest_Zone_Temperature_Sensor
	
	
