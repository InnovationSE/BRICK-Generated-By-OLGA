from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Entering_Water_Temperature_Sensor import Entering_Water_Temperature_Sensor


class Ice_Tank_Entering_Water_Temperature_Sensor(Entering_Water_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Ice_Tank_Entering_Water_Temperature_Sensor
	
	
