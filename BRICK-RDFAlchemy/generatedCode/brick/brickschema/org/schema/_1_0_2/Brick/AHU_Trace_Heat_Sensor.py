from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Trace_Heat_Sensor import Trace_Heat_Sensor


class AHU_Trace_Heat_Sensor(Trace_Heat_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Trace_Heat_Sensor
	
	
