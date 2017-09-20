from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Start_Stop import Start_Stop


class Fan_Start_Stop(Start_Stop):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Fan_Start_Stop
	
	
