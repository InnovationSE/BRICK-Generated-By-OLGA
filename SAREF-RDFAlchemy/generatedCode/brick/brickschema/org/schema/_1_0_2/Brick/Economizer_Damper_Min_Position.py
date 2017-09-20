from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Damper_Position import Damper_Position
from brick.brickschema.org.schema._1_0_2.Brick.Economizer_Damper import Economizer_Damper


class Economizer_Damper_Min_Position(Damper_Position,Economizer_Damper):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Economizer_Damper_Min_Position
	
	
