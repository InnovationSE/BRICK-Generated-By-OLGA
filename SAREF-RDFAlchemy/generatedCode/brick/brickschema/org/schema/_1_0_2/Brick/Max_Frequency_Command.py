from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Frequency_Command import Frequency_Command


class Max_Frequency_Command(Frequency_Command):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Max_Frequency_Command
	
	
