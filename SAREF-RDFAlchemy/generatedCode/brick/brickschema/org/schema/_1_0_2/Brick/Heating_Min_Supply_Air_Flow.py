from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Heating_Supply_Air_Flow import Heating_Supply_Air_Flow
from brick.brickschema.org.schema._1_0_2.Brick.Min_Air_Flow import Min_Air_Flow


class Heating_Min_Supply_Air_Flow(Heating_Supply_Air_Flow,Min_Air_Flow):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Heating_Min_Supply_Air_Flow
	
	