from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.CO2_Sensor import CO2_Sensor


class FCU_CO2_Sensor(CO2_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').FCU_CO2_Sensor
	
	
