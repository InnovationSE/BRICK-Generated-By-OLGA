from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Highest_Zone_Cooling_Command import Highest_Zone_Cooling_Command


class AHU_Highest_Zone_Cooling_Command(Highest_Zone_Cooling_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Highest_Zone_Cooling_Command
	
	
