from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water_Discharge_Flow_Sensor import Chilled_Water_Discharge_Flow_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water_Supply_Flow_Sensor import Chilled_Water_Supply_Flow_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Water_Flow_Sensor import Supply_Water_Flow_Sensor


class CWS_Chilled_Water_Supply_Flow_Sensor(Chilled_Water_Discharge_Flow_Sensor,Chilled_Water_Supply_Flow_Sensor,Supply_Water_Flow_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CWS_Chilled_Water_Supply_Flow_Sensor
	
	
