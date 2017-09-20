from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Preheat_Valve_Command import Preheat_Valve_Command


class AHU_Preheat_Valve_Command(Preheat_Valve_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Preheat_Valve_Command
	
	
