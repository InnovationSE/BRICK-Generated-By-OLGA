from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water_Discharge_Temperature_Sensor import Chilled_Water_Discharge_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Water_Temperature_Sensor import Supply_Water_Temperature_Sensor
from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water_Supply_Temperature_Sensor import Chilled_Water_Supply_Temperature_Sensor


class CWS_Chilled_Water_Discharge_Temperature_Sensor(Chilled_Water_Discharge_Temperature_Sensor,Supply_Water_Temperature_Sensor,Chilled_Water_Supply_Temperature_Sensor):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CWS_Chilled_Water_Discharge_Temperature_Sensor
	
	
