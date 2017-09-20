from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Hot_Water_Valve_Command import Hot_Water_Valve_Command


class VAV_Hot_Water_Valve_Command(Hot_Water_Valve_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').VAV_Hot_Water_Valve_Command
	
	
