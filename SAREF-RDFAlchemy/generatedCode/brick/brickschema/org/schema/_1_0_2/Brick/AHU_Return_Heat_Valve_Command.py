from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Return_Heat_Valve_Command import Return_Heat_Valve_Command


class AHU_Return_Heat_Valve_Command(Return_Heat_Valve_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Return_Heat_Valve_Command
	
	
