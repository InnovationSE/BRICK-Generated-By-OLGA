from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Current_Sensor import Current_Sensor


class Photovoltaic_Current_Output_Sensor(Current_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Photovoltaic_Current_Output_Sensor
	
	
