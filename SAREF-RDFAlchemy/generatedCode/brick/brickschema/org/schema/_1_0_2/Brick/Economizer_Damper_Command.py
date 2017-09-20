from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Damper_Command import Damper_Command


class Economizer_Damper_Command(Damper_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Economizer_Damper_Command
	
	
