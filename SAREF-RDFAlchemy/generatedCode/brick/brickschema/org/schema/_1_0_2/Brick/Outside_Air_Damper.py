from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Damper import Damper


class Outside_Air_Damper(Damper):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Outside_Air_Damper
	
	
