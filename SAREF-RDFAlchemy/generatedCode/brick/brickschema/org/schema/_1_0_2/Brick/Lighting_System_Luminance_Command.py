from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Luminance_Command import Luminance_Command


class Lighting_System_Luminance_Command(Luminance_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Lighting_System_Luminance_Command
	
	
