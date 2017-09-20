from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Run_Time_Sensor import Run_Time_Sensor


class VFD_Run_Time_Sensor(Run_Time_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Run_Time_Sensor
	
	
