from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Demand_Sensor import Demand_Sensor


class Peak_Power_Demand_Sensor(Demand_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Peak_Power_Demand_Sensor
	
	
