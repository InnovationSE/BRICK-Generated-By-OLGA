from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Air_Damper_Position import Air_Damper_Position


class Air_Damper_Min_Position(Air_Damper_Position):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Air_Damper_Min_Position
	
	
