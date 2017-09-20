from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Output_Frequency_Sensor import Output_Frequency_Sensor


class VFD_Output_Frequency_Sensor(Output_Frequency_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VFD_Output_Frequency_Sensor
	
	
