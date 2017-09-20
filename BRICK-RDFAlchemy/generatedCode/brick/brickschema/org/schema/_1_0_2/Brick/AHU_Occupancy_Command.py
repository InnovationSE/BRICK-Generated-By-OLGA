from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Occupied_Command import Occupied_Command
from brick.brickschema.org.schema._1_0_2.Brick.Occupancy_Command import Occupancy_Command


class AHU_Occupancy_Command(Occupied_Command,Occupancy_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Occupancy_Command
	
	
