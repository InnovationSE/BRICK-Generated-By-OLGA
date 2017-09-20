from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Booster_Command import Booster_Command


class Booster_Fan_Command(Booster_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Booster_Fan_Command
	
	
