from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Return_Fan import Return_Fan


class Return_Fan_VFD_Speed(Return_Fan):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Return_Fan_VFD_Speed
	
	
