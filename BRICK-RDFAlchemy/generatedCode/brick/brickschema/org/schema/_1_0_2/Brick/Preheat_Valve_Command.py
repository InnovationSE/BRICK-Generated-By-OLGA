from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Valve_Command import Valve_Command


class Preheat_Valve_Command(Valve_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Preheat_Valve_Command
	
	
