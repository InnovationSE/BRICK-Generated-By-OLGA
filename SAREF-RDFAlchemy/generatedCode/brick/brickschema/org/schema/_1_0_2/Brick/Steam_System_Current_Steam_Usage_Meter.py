from rdflib import Namespace, Graph, Literal, RDF, URIRef
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy import rdfSingle, rdfMultiple, rdfList

from brick.brickschema.org.schema._1_0_2.Brick.Current_Steam_Usage_Meter import Current_Steam_Usage_Meter


class Steam_System_Current_Steam_Usage_Meter(Current_Steam_Usage_Meter):
    rdf_type = Namespace('https://brickschema.org/schema/1.0.2/Brick#').Steam_System_Current_Steam_Usage_Meter
	
	
