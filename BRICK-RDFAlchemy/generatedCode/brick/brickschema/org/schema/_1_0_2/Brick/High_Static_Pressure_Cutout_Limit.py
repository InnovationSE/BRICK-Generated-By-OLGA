from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Static_Pressure import Static_Pressure


class High_Static_Pressure_Cutout_Limit(Static_Pressure):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').High_Static_Pressure_Cutout_Limit
	
	
