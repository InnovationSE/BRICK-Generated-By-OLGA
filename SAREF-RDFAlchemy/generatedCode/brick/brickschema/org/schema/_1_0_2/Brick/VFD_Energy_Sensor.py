from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Energy_Sensor import Energy_Sensor


class VFD_Energy_Sensor(Energy_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Energy_Sensor
	
	
