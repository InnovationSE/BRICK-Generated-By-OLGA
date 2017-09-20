from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Pump_Lead_Lag_Status import Pump_Lead_Lag_Status
from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water_Pump_Status import Chilled_Water_Pump_Status


class Chilled_Water_Pump_Lead_Lag_Status(Pump_Lead_Lag_Status,Chilled_Water_Pump_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Chilled_Water_Pump_Lead_Lag_Status
	
	
