from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Discharge_Fan_Command import Discharge_Fan_Command
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Fan_Command import Supply_Fan_Command


class AHU_Discharge_Fan_Command(Discharge_Fan_Command,Supply_Fan_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').AHU_Discharge_Fan_Command
	
	
