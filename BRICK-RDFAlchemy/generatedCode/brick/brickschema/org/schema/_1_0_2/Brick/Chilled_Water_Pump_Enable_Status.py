from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Pump_Enable_Status import Pump_Enable_Status
from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water_Pump_Status import Chilled_Water_Pump_Status


class Chilled_Water_Pump_Enable_Status(Pump_Enable_Status,Chilled_Water_Pump_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Chilled_Water_Pump_Enable_Status
	
	