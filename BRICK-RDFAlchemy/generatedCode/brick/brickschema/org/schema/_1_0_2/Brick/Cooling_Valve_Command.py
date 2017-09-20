from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Cooling_Command import Cooling_Command
from brick.brickschema.org.schema._1_0_2.Brick.Valve_Command import Valve_Command


class Cooling_Valve_Command(Cooling_Command,Valve_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Cooling_Valve_Command
	
	
