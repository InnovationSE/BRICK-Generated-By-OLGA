from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Temperature_Sensor import Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Mixed_Air import Mixed_Air


class Mixed_Air_Temperature_Sensor(Temperature_Sensor,Mixed_Air):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Mixed_Air_Temperature_Sensor
	
	
