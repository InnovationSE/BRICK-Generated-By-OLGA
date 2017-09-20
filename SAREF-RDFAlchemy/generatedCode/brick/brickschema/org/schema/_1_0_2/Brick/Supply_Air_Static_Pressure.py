from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air import Supply_Air
from brick.brickschema.org.schema._1_0_2.Brick.Static_Pressure import Static_Pressure


class Supply_Air_Static_Pressure(Supply_Air,Static_Pressure):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Supply_Air_Static_Pressure
	
	
