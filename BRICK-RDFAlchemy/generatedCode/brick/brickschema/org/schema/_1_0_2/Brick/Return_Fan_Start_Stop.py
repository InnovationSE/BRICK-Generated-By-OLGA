from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Fan_Start_Stop import Fan_Start_Stop
from brick.brickschema.org.schema._1_0_2.Brick.Return_Fan import Return_Fan


class Return_Fan_Start_Stop(Fan_Start_Stop,Return_Fan):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Return_Fan_Start_Stop
	
	
