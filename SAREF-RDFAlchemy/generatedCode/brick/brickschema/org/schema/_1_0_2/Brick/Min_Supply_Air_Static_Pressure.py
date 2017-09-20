from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Static_Pressure import Supply_Air_Static_Pressure
from brick.brickschema.org.schema._1_0_2.Brick.Static_Pressure_Min import Static_Pressure_Min


class Min_Supply_Air_Static_Pressure(Supply_Air_Static_Pressure,Static_Pressure_Min):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Min_Supply_Air_Static_Pressure
	
	
