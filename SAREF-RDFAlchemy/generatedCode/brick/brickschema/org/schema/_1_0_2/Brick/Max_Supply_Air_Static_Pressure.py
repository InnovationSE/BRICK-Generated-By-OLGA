from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Static_Pressure_Max import Static_Pressure_Max
from brick.brickschema.org.schema._1_0_2.Brick.Supply_Air_Static_Pressure import Supply_Air_Static_Pressure


class Max_Supply_Air_Static_Pressure(Static_Pressure_Max,Supply_Air_Static_Pressure):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Max_Supply_Air_Static_Pressure
	
	
