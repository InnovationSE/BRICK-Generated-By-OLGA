from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Chilled_Water import Chilled_Water
from brick.brickschema.org.schema._1_0_2.Brick.Pump_Command import Pump_Command


class Chilled_Water_Pump_Command(Chilled_Water,Pump_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Chilled_Water_Pump_Command
	
	