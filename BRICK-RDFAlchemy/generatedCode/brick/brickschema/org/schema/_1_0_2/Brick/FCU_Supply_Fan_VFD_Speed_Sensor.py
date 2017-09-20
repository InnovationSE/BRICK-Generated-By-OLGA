from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Fan_VFD_Speed_Sensor import Supply_Fan_VFD_Speed_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Fan_VFD_Speed_Sensor import Discharge_Fan_VFD_Speed_Sensor


class FCU_Supply_Fan_VFD_Speed_Sensor(Supply_Fan_VFD_Speed_Sensor,Discharge_Fan_VFD_Speed_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').FCU_Supply_Fan_VFD_Speed_Sensor
	
	
