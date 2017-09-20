from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Fan_Piezoelectric_Sensor import Supply_Fan_Piezoelectric_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Fan_Piezoelectric_Sensor import Discharge_Fan_Piezoelectric_Sensor


class AHU_Discharge_Fan_Piezoelectric_Sensor(Supply_Fan_Piezoelectric_Sensor,Discharge_Fan_Piezoelectric_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Discharge_Fan_Piezoelectric_Sensor
	
	
