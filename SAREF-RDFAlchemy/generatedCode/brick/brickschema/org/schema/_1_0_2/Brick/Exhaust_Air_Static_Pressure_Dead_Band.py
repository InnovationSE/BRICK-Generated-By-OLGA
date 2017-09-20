from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Exhaust_Air_Static_Pressure import Exhaust_Air_Static_Pressure


class Exhaust_Air_Static_Pressure_Dead_Band(Exhaust_Air_Static_Pressure):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Exhaust_Air_Static_Pressure_Dead_Band
	
	
