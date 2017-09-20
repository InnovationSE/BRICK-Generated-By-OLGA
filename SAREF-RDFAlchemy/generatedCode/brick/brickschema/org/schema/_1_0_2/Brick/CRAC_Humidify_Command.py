from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Humidify_Command import Humidify_Command


class CRAC_Humidify_Command(Humidify_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').CRAC_Humidify_Command
	
	
