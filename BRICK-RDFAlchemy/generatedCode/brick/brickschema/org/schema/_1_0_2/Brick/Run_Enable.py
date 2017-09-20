from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Run import Run
from brick.brickschema.org.schema._1_0_2.Brick.Enable import Enable


class Run_Enable(Run,Enable):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Run_Enable
	
	
