from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heating_Command import Heating_Command
from brick.brickschema.org.schema._1_0_2.Brick.Valve_Command import Valve_Command


class Heating_Valve_Command(Heating_Command,Valve_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Heating_Valve_Command
	
	
