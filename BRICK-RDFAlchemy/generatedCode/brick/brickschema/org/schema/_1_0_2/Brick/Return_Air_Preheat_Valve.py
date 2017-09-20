from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Preheat_Valve import Preheat_Valve
from brick.brickschema.org.schema._1_0_2.Brick.Return_Air import Return_Air


class Return_Air_Preheat_Valve(Preheat_Valve,Return_Air):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Return_Air_Preheat_Valve
	
	
