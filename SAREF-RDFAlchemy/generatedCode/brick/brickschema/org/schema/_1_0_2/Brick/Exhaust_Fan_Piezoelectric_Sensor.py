from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Piezoelectric_Sensor import Piezoelectric_Sensor


class Exhaust_Fan_Piezoelectric_Sensor(Piezoelectric_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Fan_Piezoelectric_Sensor
	
	