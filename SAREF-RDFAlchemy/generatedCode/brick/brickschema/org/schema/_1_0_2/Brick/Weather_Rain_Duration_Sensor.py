from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Weather_Rain_Sensor import Weather_Rain_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Rain_Duration_Sensor import Rain_Duration_Sensor


class Weather_Rain_Duration_Sensor(Weather_Rain_Sensor,Rain_Duration_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Weather_Rain_Duration_Sensor
	
	
