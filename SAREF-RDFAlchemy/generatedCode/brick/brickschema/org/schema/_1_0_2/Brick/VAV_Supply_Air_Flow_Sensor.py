from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Air_Flow_Sensor import Discharge_Air_Flow_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Flow_Sensor import Supply_Air_Flow_Sensor


class VAV_Supply_Air_Flow_Sensor(Discharge_Air_Flow_Sensor,Supply_Air_Flow_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Supply_Air_Flow_Sensor
	
	
