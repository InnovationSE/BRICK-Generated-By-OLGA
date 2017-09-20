from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Enable_Status import Enable_Status
from brick.brickschema.org.schema._1_0_2.Brick.Pump_Status import Pump_Status


class Pump_Enable_Status(Enable_Status,Pump_Status):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Pump_Enable_Status
	
	
