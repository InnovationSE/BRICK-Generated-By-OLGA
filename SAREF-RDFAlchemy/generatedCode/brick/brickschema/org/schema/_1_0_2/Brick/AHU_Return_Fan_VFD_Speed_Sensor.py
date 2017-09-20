from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Return_Fan_VFD_Speed_Sensor import Return_Fan_VFD_Speed_Sensor


class AHU_Return_Fan_VFD_Speed_Sensor(Return_Fan_VFD_Speed_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Return_Fan_VFD_Speed_Sensor
	
	
